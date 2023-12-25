import pandas as pd
import requests
import json
from tabulate import tabulate
from sqlalchemy import create_engine, text
from configparser import ConfigParser
from typing import final

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
    pass


def display_prettify(datas: dict) -> None:
    pass


def save_to_json(datas: list) -> None:
    pass


def to_dataframe(datas: list) -> pd.DataFrame:
    pass


def display_df(df, style="psql") -> None:
    pass


def init_sql_db() -> None:
    pass


def save_to_mysql_db(df: pd.DataFrame) -> None:
    pass


if __name__ == "__main__":
    # Datas collection
    countries_datas: list = collect_countries_datas()

    # Saved Raw Datas
    save_to_json(countries_datas)

    # Convert to Dataframe
    countries_df: pd.DataFrame = to_dataframe(countries_datas)

    # Display the datas table
    display_df(countries_df)

    # Save to Excel
    countries_df.to_excel("../Datas/countries.xlsx", index=False, engine="openpyxl")

    # Save to DB
    init_sql_db()
    save_to_mysql_db(countries_df)

