import os
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    """Represents the configuration dynamically storing all configuration and data source paths.
    
    Attributes:
        project_path (str): The parent project path.
        entities_count_config_path (str):  The path leading to the entities count configuration.
        marvel_api_config_path (str): The path leading to the Marvel API configuration.
        marvel_movies_csv_path (str): The path leading to the CSV file containing information about the Marvel movies.
        characters_json_path (str): The path leading to the JSON file containing information about the Marvel characters.
    """
    project_path: Path = Path(__file__).resolve().parent

    entities_count_config_path: Path = project_path.joinpath("API_Configs", "entities-count-config.json")
    
    marvel_api_config_path: Path = project_path.joinpath("API_Configs", "marvel-api-config.json")
    
    marvel_movies_csv_path: Path = project_path.joinpath("DataSourcesCSV", "marvel.csv")
    
    characters_json_path: Path = project_path.joinpath("DataSourcesJSON", "characters.json")

