import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"


def test_list_all_jsons():
    r = requests.get(url=base_url + "/posts")
    assert r.status_code == 200
    assert len(r.json()) == 100


def test_keys():
    expected_keys = ["userId", "id", "title", "body"]
    resource = "1"
    r = requests.get(url=base_url + "/posts/" + resource)
    keys_list = list(r.json())
    assert r.status_code == 200
    assert expected_keys == keys_list


@pytest.mark.parametrize("uid", ["1", "2", "3", "4"])
def test_uid(uid):
    r = requests.get(url=base_url + "/posts/" + uid)
    assert r.status_code == 200
    assert str(r.json()["id"]) == uid


def test_delete_metod():
    r = requests.delete(url=base_url + "/posts/1")
    assert r.status_code == 200


@pytest.mark.parametrize("title", ["foo_1", "foo_2", "foo_3"])
def test_post_req_status_code(title):
    r = requests.post(url=base_url + "/posts",
                      headers={"Content-type": "application/json; charset=UTF-8"},
                      json={"title": title, "body": "bar", "userId": 1})
    assert r.status_code == 201
    assert r.json()["title"] == title
