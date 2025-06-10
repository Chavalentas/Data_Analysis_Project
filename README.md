# Marvel Comics Data Analysis
This is the documentation of a project that deals with data analysis of comics data that can be accessed via an API.
In addition, a CSV data set is analyzed.

## Used technologies
![Jupyter](https://img.shields.io/badge/Jupyter-%23e7ebc7?style=for-the-badge&logo=Jupyter) 
![Python](https://img.shields.io/badge/Python-yellow?style=for-the-badge&logo=Python)
![Pandas](https://img.shields.io/badge/Pandas-%23388080?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23236363?style=for-the-badge)
![Numpy](https://img.shields.io/badge/Numpy-%23236363?style=for-the-badge&logo=numpy)
![Networkx](https://img.shields.io/badge/Networkx-%23236363?style=for-the-badge)

## To Start
Navigate to **Data_Analysis.ipynb** and execute the notebook.
Before running the script make sure to run **pipenv shell** to create the shell environment needed for the project.
All aditionally installed packages are already in Pipfile and Pipfile.lock. 
Afterwards, select the created virtual environment as the execution kernel for the Jupyter notebook.
Should you encounter some issues starting the project, you can reproduce the following steps (make sure to navigate to 
the parent directory of the project):
1. pyenv install 3.11.3
2. pyenv local 3.11.3
3. pip install pipenv
4. pipenv install --python 3.11.3
5. pipenv install pandas matplotlib numpy networkx requests
6. pipenv shell (this creates the virtual environment)
   
Make sure to use this environment to execute the Jupyter notebook.
You may be required to install the corresponding ipykernel.

## Used packages
The project uses the following packages that were aditionally installed using **pipenv install**:
* pandas
* matplotlib
* numpy
* networkx
* requests

## Data Sources
This section contains a description of the used data sources.

### Marvel API
The API has a REST architecture and consists of more GET endpoints that can be used to fetch data.
The resources of the REST-API represent more entity types.
These include:
* Comics
* Series
* Stories
* Events
* Characters

Refer to [this](#entities-count-header) subsection for more information.

### CSV
The CSV file contains all information (e.g. budget and revenue) for all Marvel movies made so far (different distributors).
Refer to [this](#csv-file-header) subsection for more information.

## The project structure
```
│   
│      
│
└───API_Configs
│   │   entities-count-config.json
│   │   marvel-api-config.json
│   
└───DataSourcesCSV
│   │   marvel.csv
│      
│   
└───DataSourcesJSON
│   │   characters.json
│
│
└───Helpers
│   │   Helper.py
│
│
└───Models
│   │   RelationshipCalculator.py 
│
│
└───Python_API_Handlers
│   │   MarvelApiHandler.py   
│
│
└───TLSAdapters
│   │ TLSAdapter.py
│   
|   config.py
│   Data_Analysis.ipynb
│   README.md
```
The individual directories are described in more detail in the following sections.

## API_Configs
This folder contains two major configurations needed to 
provide the analysis of the data: **entities-count-config.json** and **marvel-api-config.json**.
<h4 style="color:red"> NOTE: </h4> Please do not delete the above-mentioned configurations and their contents. This may cause the data analysis to show errors when running the Jupyter notebook. For entities-count-config.json, this can cause the number of individual entity types to be recalculated via API calls.
This can distort the results of the analysis when the Jupyter notebook is called repeatedly.
As the analysis was carried out statically at the time of creation, it cannot be ruled out that the number of entities for the individual entity types has changed since the time the data was analysed (i.e. it is possible that new comics or new series have been written since then, for example). <br/>
Date of the last analysis: January 09, 2024.

### <a name="entities-count-header"></a>entities-count-config.json
This configuration contains the total number of possible entity types that exist in the Marvel API.
These include:
* Comics
* Series
* Stories
* Events
* Characters

The file is recalculated during the execution of the Jupyter notebook if it does not exist or is empty.
The file has the following structure:
```json
{"totalHeroCount": "x", "totalComicsCount": "x", "totalSeriesCount": "x", "totalStoriesCount": "x", "totalEventsCount": "x"}
`````
**Comics**: the specific comics released so far. <br>
**Series**: consist of more comics. <br>
**Stories**: comics consist of stories. <br>
**Events**: huge events that comprise more series or comics. It is a big, universe-changing storyline. <br>
**Characters**: heroes or organizations that are protagonits or antagonists of the entity types mentioned above. 

### marvel-api-config.json
Contains all the connection information needed in order to connect to the Marvel API and execute the API calls.
This contains the **URL**, the **API key**, **hash (md5(ts+privateKey+publicKey))**, **ts (timestamp)** and maximal limit of data that can be fetched from the API (**dataMax**).
The file has the following structure:

```json
{
    "url": "https://gateway.marvel.com/v1/public",
    "apiKey": "PLEASE-FILL-IN",
    "hash": "PLEASE-FILL-IN",
    "ts": 1,
    "dataMax": 100
}
```

## DataSourcesCSV
This folder contains a **CSV** file containing information of all Marvel movies made so far by different distributors: **marvel.csv**.

### <a name="csv-file-header"></a>marvel.csv
The **CSV** file has the following column attributes:
```
Title,Distributor(s),Release date(United States),Bud�ge(mil�lions),Opening weekend(North America),North America,Other territories,Worldwide
```
During the data analysis, this file was imported to the Jupyter notebook using Pandas dataframe.

## DataSourcesJSON
This folder contains a **JSON** file containing information about all characters from Marvel: **characters.json**.
<h4 style="color:red"> NOTE: </h4> Please do not delete the above-mentioned file and its contents. This may cause the data analysis to show errors when running the Jupyter notebook. For characters.json, this can cause the number of characters to be recalculated via API calls.
This can distort the results of the analysis when the Jupyter notebook is called repeatedly.
As the analysis was carried out statically at the time of creation, it cannot be ruled out that the number of characters has changed since the time the data was analysed (i.e. it is possible that new characters have been created since then, for example). <br/>
Date of the last analysis: January 09, 2024. 

### characters.json
Contains all characters stored in form of JSON array consisting of JSON objects.
The file has the following structure:
```json
[
    {
        "id": 1011334,
        "name": "3-D Man",
        "description": "",
        "modified": "2014-04-29T14:18:17-0400",
        "thumbnail": {
            "path": "url",
            "extension": "jpg"
        },
        "resourceURI": "url",
        "comics": {
            "available": 12,
            "collectionURI": "colURI",
            "items": [
                {
                    "resourceURI": "url",
                    "name": "comicsName"
                },
                ...
            ],
            "returned": 12
        },
        "series": {
            "available": 3,
            "collectionURI": "colURI",
            "items": [
                {
                    "resourceURI": "url",
                    "name": "seriesName"
                },
                ...
            ],
            "returned": 3
        },
        "stories": {
            "available": 21,
            "collectionURI": "colURI",
            "items": [
                {
                    "resourceURI": "url",
                    "name": "Cover #19947",
                    "type": "cover"
                },
                ...
            ],
            "returned": 20
        },
        "events": {
            "available": 1,
            "collectionURI": "colURI",
            "items": [
                {
                    "resourceURI": "url",
                    "name": "Secret Invasion"
                }
            ],
            "returned": 1
        },
        "urls": [
            {
                "type": "detail",
                "url": "url"
            },
            {
                "type": "wiki",
                "url": "url"
            },
            {
                "type": "comiclink",
                "url": "url"
            }
        ]
    },
    ...
]
```

During the data analysis, this file was imported to the Jupyter notebook using Pandas dataframe.

## Helpers
This folder contains a class called **Helper.py**.
It encapsulates all useful functions that can be reused independent from the data analysis (e.g. function that concatenates lists).

## Models
This folder contains all functions that are useful for the data analysis and cannot be mentioned in the Jupyter notebook due to their complexity.
These are encapsulated in one or more classes.
### RelationshipCalculator.py
Class that calculates amount of all common entity types (shared appearances in comics, series, events and stories) for all pair combinations of characters.

## Python_API_Handlers
This folder contains all HTTP clients (handlers) used to commmunicate with external data sources using an API.

### MarvelApiHandler.py
This class contains all functions used to communicate with the Marvel API.
For example, this class contains functions to fetch all characters and information about the total count of different entity types.

## TLSAdapters

Contains the TLS adapters necessary to communicate with external sources using HTTPS.

### TLSAdapter.py
Adapter class used to communicate with the Marvel API via HTTPS.

## config.py
This is a configuration file that dynamically saves paths to all configuration files (JSON) and csv files.
This enables the individual file paths to be executed dynamically on all operating systems.

## Data_Analysis.ipynb
The main core of the project (Jupyter notebook).
Contains the data analysis containing important functions with their documentation and visualizations (graphs and networks).
To start, just execute this Jupyter notebook.