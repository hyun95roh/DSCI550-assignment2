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
<details> 
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
<details/>


# Image Generation and Processing Pipeline
<details>
    This document explains how to set up and use an AI pipeline involving image generation (Colab), captioning, and object detection (Docker).
    
    ## Setup Instructions
    
    ### Environment for Image Generation (Colab)
    
    **Mount Google Drive**:
    
    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```
    
    **Set Up Caching**:
    
    This stores model weights and dependencies on Drive, speeding up future runs.
    
    ```python
    import os
    os.environ["HF_HOME"] = "/content/drive/MyDrive/huggingface_cache"
    ```
    
    ---
    
    ## Docker Containers
    
    ### a. Image Captioning Container
    
    **Build Docker Image**:
    
    ```bash
    docker build -f Im2txtRestDockerfile -t uscdatascience/im2txt-rest-tika .
    ```
    
    **Run Container**:
    
    Replace `/path/to/your/images` with your image directory.
    
    ```bash
    docker run --platform linux/amd64 -it -p 8765:8764 -v /path/to/your/images:/data uscdatascience/im2txt-rest-tika
    ```
    
    ### b. Object Detection Container
    
    **Build Docker Image**:
    
    ```bash
    docker build -f InceptionRestDockerfile -t uscdatascience/inception-rest-tika .
    ```
    
    **Run Container**:
    
    Replace `/path/to/your/images` with your image directory.
    
    ```bash
    docker run --platform linux/amd64 -it -p 8766:8764 -v /path/to/your/images:/data uscdatascience/inception-rest-tika
    ```
    
    ---
    
    ## Serving Images via HTTP
    
    Navigate to your image directory and run:
    
    ```bash
    cd "/Users/yourname/Documents/Images"
    python -m http.server 8000
    ```
    
    Images will be accessible via:
    
    ```
    http://localhost:8000/image_0.png
    ```
    
    ---
    
    ## Usage
    
    ### Running the Jupyter Notebook
    
    1. Open `notebook.ipynb`.
    2. Update paths (TSV file, images directory, etc.).
    3. Run cells sequentially:
       - Reads TSV file.
       - Calls captioning and object detection APIs.
       - Adds results to DataFrame.
       - Saves DataFrame as a TSV file.
    
    ---
    
    ## API Endpoints
    
    ### Captioning Endpoint
    
    ```
    http://localhost:8765/inception/v3/caption/image?url=<image_url>&beam_size=3&max_caption_length=30
    ```
    
    ### Object Detection Endpoint
    
    ```
    http://localhost:8766/inception/v4/classify/image?url=<image_url>&topn=2&min_confidence=0.03
    ```
    
    Replace `<image_url>` with your image URL, for example:
    
    ```
    http://host.docker.internal:8000/image_0.png
    ```
    
    ---
    
    ## Pipeline Overview
    
    ### Image Generation
    - Uses Stable Diffusion on Colab Pro.
    - Checkpointing allows resuming from the last processed image.
    
    ### Image Captioning
    - Docker container runs a captioning model.
    - Selects captions based on highest confidence.
    
    ### Object Detection
    - Docker container runs an Inception-based detection model.
    - Extracts detected object names.
    
    ### Integration
    - Local HTTP server makes images accessible.
    - API responses processed in Jupyter Notebook.
    
    ---
    
    ## Real-World Relevance
    - **Scalability:** Dependency caching and checkpointing for large-scale tasks.
    - **Deployment:** Docker and API integrations reflecting modern industry practices.
    - **Efficiency:** Optimized workflows for cost and downtime reduction.
    - **Evaluation:** Comparing AI models for practical insights (media, advertising, surveillance).
    
    ---
    
    ## Troubleshooting
    
    ### Service Connection Issues
    - Verify container status: `docker ps`
    - Ensure correct port mapping and running HTTP server.
    
    ### File Access
    - Confirm Docker volume mounting.
    
    ### API Endpoint Verification
    - Inspect container logs to verify correct API endpoints.
    
    ### Authentication and Permissions
    - Check Google Drive mounting (for Colab).
    - Verify file permissions.

<details/>

