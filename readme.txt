# DSCI550-2025b-Assignment-2
Large Scale Data Extraction &amp; Analysis for Haunted Places - (Team 11) 

Team Members and Responsibillities: 
- Kirthi Chillakanti - SPaCY code troubleshooting and report generation
- Lance Vijil Dsilva - Image generation, captioning, and object recognition lead; report generation
- Rafayel Mirijanyan - Geo Topic Parser troubleshooting
- Kavi Gill - SPaCY code troubleshooting and report generation
- Hyuntae Roh - Geo Topic Parser lead; code conductor; report generation
- Ryan Norring - SPaCY code lead; report generation

# spaCy
spaCy is a robust natural language processor used to extract information from text. In this assignment, we use spaCy to identify named entities from the description column of our dataset, sorting them into 18 pre-defined categories. 

To install spaCy, follow the instructions at this [link](https://spacy.io/usage). Our code uses the "small" trained pipleine of spaCy; details on the different English-trained pipelines can be found [here](https://spacy.io/models/en#en_core_web_sm).

# GeoTopicParser
Based on a Gazetteer, a dictionary for looking up the names/places and their corresponding latitudes and longitudes, the GeoTopicParser and runs a Named Entity Recognition(NER) modeling to produce the tag of location name, latitude and logitude. 

Before running the GeoTopicParser, you should activate lucene-geo-gazetteer first. Follow the instruction of this [readme](https://github.com/Hibis5946/geotopicparser-utils/blob/master/README_tika_geo_parser.txt)

Named Entity Recognition is powered by Apache OpenNLP. Download en-ner-location.bin, which is a file of pre-trained model. Place the .bin file at this directory(org/apache/tika/parser/geo/) so that Tika can use the pre-trained model. 

Now, we have geographical dictionary to look up and NER pre-trained model. 
Based on tika-app-2.6.0.jar and tika-parser-nlp-package-2.6.0.jar, we will extract the geographical tags from the .geot files. If you have not converted your text into .geot files, please do before running Tika. 

When you are ready, run the following code(one line) in your CMD:
```
java -classpath 'root/src/tika/tika-app-2.6.0':'root/src/tika/tika-parser-nlp-package-2.6.0.jar':'root/src/location-ner-model':'root/src/geotopic-mime' org.apache.tika.cli.TikaCLI -m
```

Refer to the following code block when you are running on jupyter notebook:
```
geot_files_dir = os.path.join(project_root, 'src', 'geotopic-mime') 
tika_app_jar = os.path.join(project_root, 'src', 'tika', 'tika-app-2.6.0.jar')
tika_nlp_jar = os.path.join(project_root, 'src', 'tika', 'tika-parser-nlp-package-2.6.0.jar')
ner_model_dir = os.path.join(project_root, 'src', 'location-ner-model')

classpath = f"{tika_app_jar}:{tika_nlp_jar}:{ner_model_dir}:{geot_files_dir}"
tika_cmd_base = [
    "java", "-classpath", classpath,
    "org.apache.tika.cli.TikaCLI", "-m"
]
```



