# DSCI550-assignment2
Large Scale Data Extraction &amp; Analysis for Haunted Places - (Team 11) 

**Members**: 
- Kirthi Chillakanti 
- Lance Vijil Dsilva 
- Rafayel Mirijanyan 
- Kavi Gill 
- Hyuntae Roh 
- Ryan Norring


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



