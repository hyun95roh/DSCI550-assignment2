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

def extract_entities(text):
    doc = nlp(str(text)) # Ensure text is in string format
    return [(ent.label_, ent.text) for ent in doc.ents] 

# Apply NER to the 'description' column. This takes about 10 minutes.
df['entities'] = df['description'].apply(extract_entities)

# Save to a new file.
ner_results = "ner_results.tsv"

df.to_csv(ner_results, sep="\t", index=False)
""" # Confirm success in Jupyter/Colab:
print(f"NER complete. Results saved to {ner_results}.") """
