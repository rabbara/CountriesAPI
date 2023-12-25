import pytest
import pandas as pd


@pytest.fixture()
def countries():
    return pd.read_excel("../Outputs/countries.xlsx")


def test_file_header(countries):
    valid_header = [
        "country_cca2",
        "country_cca3",
        "country_common_name",
        "country_official_name",
        "country_languages",
        "country_area",
        "country_population",
        "country_borders",
        "country_region",
        "country_subregion",
        "country_continents",
        "country_flags_alt",
        "country_flags_png",
        "country_flags_svg",
        "coat_of_arms_png",
        "coat_of_arms_svg",
        "country_independent_status",
        "country_landlocked_status",
        "country_un_member",
        "capital_name",
        "capital_lat",
        "capital_lon",
        "car_side",
        "currency_code",
        "currency_name",
        "currency_symbol"
    ]
    assert set(valid_header) == set(countries.columns)


def test_file_size(countries):
    assert countries.shape[0] == 245