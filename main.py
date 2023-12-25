import pandas as pd
import requests
import json
from tabulate import tabulate
from sqlalchemy import create_engine, text
from configparser import ConfigParser
from typing import final
import re


config = ConfigParser()
config.read('config.ini')


# Countries API URL
COUNTRY_API_URL = config.get("COUNTRY_API", "URL")


# DB Params
HOST: final = config.get("DB", "HOST")
PORT: final = config.get("DB", "PORT")
DB_USER: final = config.get("DB", "DB_USER")
DB_PWD: final = config.get("DB", "DB_PWD")
DB_NAME: final = config.get("DB", "DB_NAME")


def collect_countries_datas() -> list:
    '''
    Collect datas from CountriesAPI, Raise an error if the request code != 200.
        
        Returns:
            Countries rows (list): countries datas from the api
    '''
    pass


def save_to_json(datas: list, folder: str="Outputs") -> None:
    '''
    Save datas on file at the JSON format
        
        Paramaters:
            datas (list): json datas
            folder (str): folder to save the file, the default folder is Outputs
        
        Return:
            None    
    '''
    pass


def save_to_excel(datas: pd.DataFrame, folder: str="Outputs", engine: str="openpyxl") -> None:
    '''
    Save a dataframe datas on a Excel file
        
        Paramaters:
            datas (Dataframe):  datas
            folder (str): folder to save the file, the default folder is Outputs
            engine: Engine use for creating the file, default is openpyxl
        
        Return:
            None    
    '''


def countries_api_to_dataframe(datas: list) -> pd.DataFrame:
    '''
    Convert datas from CountriesAPI at the format JSON to a pandas dataframe
        
        Paramaters:
            datas (Dataframe):  JSON datas from CountriesAPI
        
        Return:
            countries datas (Dataframe): countries datas
    '''
    pass


def display_df(df, style="psql") -> None:
    '''
    Display dataframe datas
        
        Paramaters:
            df (Dataframe): datas
    '''
    print(tabulate(df, headers='keys', tablefmt=style))


def init_db() -> None:
    '''
    Initialize database.
    '''
    pass


def save_to_db(df: pd.DataFrame) -> None:
    '''
    Save datas on the db
    
        Paramaters:
            df (Dataframe): datas
    '''
    pass


if __name__ == "__main__":
    # Datas collection
    countries_datas: list = collect_countries_datas()

    # Saved Raw Datas
    save_to_json(countries_datas)

    # Convert to Dataframe
    countries_df: pd.DataFrame = countries_api_to_dataframe(countries_datas)

    # Display the datas table
    display_df(countries_df)

    # Save to Excel
    save_to_excel(countries_df)

    # Save to DB
    init_db()
    save_to_db(countries_df)

