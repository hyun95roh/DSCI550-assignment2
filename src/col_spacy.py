""" # If running in Jupyter/Colab, execute:
!python -m spacy download en_core_web_sm 

import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm") # End of Jupyter/Colab specific."""

# If running as script from GitHub, execute:
import spacy
import pandas as pd

try:
     # If model is already downloaded, execute.
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If the model isn't found, download and load.
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm") 
# End of Script/ GitHub specific

# Following code always runs, regardless of medium:

# Ensure that the tsv file is available.
df = pd.read_csv("haunted_places.tsv", sep="\t")

# Function to extract NEs from document and creat dictionary of k:v -> label:text
def extract_entity_dict(text):
    doc = nlp(str(text))
    entity_dict = {}
    for ent in doc.ents:
        entity_dict.setdefault(ent.label_, []).append(ent.text)
    return entity_dict

# Apply function to description column. This code takes approx. 10 minutes to run.
df['entity_dict'] = df['description'].apply(extract_entity_dict)

# Get all unique entity labels from the dataset
all_labels = set()
df['entity_dict'].apply(lambda d: all_labels.update(d.keys()))

# Create separate columns for each label
for label in all_labels:
    df[label] = df['entity_dict'].apply(lambda d: d.get(label, []))

# Drop the intermediate dictionary column if not needed
df.drop(columns=['entity_dict'], inplace=True)

# Save to a new file.
ner_results = "ner_results.tsv"

df.to_csv(ner_results, sep="\t", index=False)
""" # Confirm success in Jupyter/Colab:
print(f"NER complete. Results saved to {ner_results}.") """
