import requests
import pytest

base_url = "https://jsonplaceholder.typicode.com"
base_url2 = "https://api.openbrewerydb.org/"

ab = []

def keys2():
    keys_list = ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state', 'county_province',
                 'postal_code', 'country', 'longitude', 'latitude', 'phone', 'website_url', 'updated_at', 'created_at']
    brewery = 'barrel-dog-brewing-evergreen'
    r = requests.get(url=base_url2 + 'breweries/' + brewery)
    keys = list(r.json().keys())
    for i in r.json():
        ab.append(i)
    print(ab)
print(keys2())


def keys():
    keys_list = ['userId', 'id', 'title', 'body']
    r = requests.get(url=base_url + '/posts/1')
    keys = list(r.json())
    print(keys)

print(keys())