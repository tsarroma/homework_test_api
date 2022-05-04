import pytest
import requests

base_url = "https://api.openbrewerydb.org/"


def test_count_max_50_per_page():
    count = "51"
    r = requests.get(url=base_url + "breweries?per_page=" + count)
    assert r.status_code == 200
    assert len(r.json()) == 50


def test_keys_list():
    expected_keys = ["id", "name", "brewery_type", "street", "address_2", "address_3", "city", "state",
                     "county_province",
                     "postal_code", "country", "longitude", "latitude", "phone", "website_url", "updated_at",
                     "created_at"]
    brewery = "barrel-dog-brewing-evergreen"
    r = requests.get(url=base_url + "breweries/" + brewery)
    keys_list = list(r.json().keys())
    assert r.status_code == 200
    assert expected_keys == keys_list


def test_search_name():
    search_name = "barrel dog brewing"
    r = requests.get(url=base_url + "breweries/search?query=" + search_name)
    assert r.status_code == 200
    assert r.json()[0]["name"].lower() == search_name


@pytest.mark.parametrize("city", ["Moscow", "Evergreen", "New York"])
def test_filter_city(city):
    r = requests.get(url=base_url + "breweries?by_city=" + city)
    assert r.status_code == 200
    assert r.json()[0]["city"] == city


@pytest.mark.parametrize("brewery_type",
                         ["micro", "nano", "regional", "brewpub", "large", "planning", "bar", "contract", "closed"])
def test_filter_brewery_type(brewery_type):
    r = requests.get(url=base_url + "breweries?by_type=" + brewery_type)
    assert r.status_code == 200
    assert r.json()[0]["brewery_type"] == brewery_type
