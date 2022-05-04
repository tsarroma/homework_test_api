import pytest
import requests

base_url = "https://dog.ceo/api"


def test_list_all_len():
    r = requests.get(url=base_url + "/breeds/list/all")
    assert r.status_code == 200
    assert len(r.json()["message"]) == 95


def test_list_sub_breeds_hound():
    r = requests.get(url=base_url + "/breed/hound/list")
    sub_breeds = ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]
    assert r.status_code == 200
    assert r.json()["message"] == sub_breeds


def test_random_status():
    r = requests.get(url=base_url + "/breeds/image/random")
    assert r.status_code == 200
    assert r.json()["status"] == "success"


@pytest.mark.parametrize("spaniel", ["blenheim", "brittany", "cocker", "irish", "japanese", "sussex", "welsh"])
def test_sub_breed_spaniel(spaniel):
    r = requests.get(url=base_url + "/breed/spaniel/" + spaniel + "/images")
    assert r.status_code == 200


@pytest.mark.parametrize("count", ["1", "7", "50"])
def test_check_count_img(count):
    r = requests.get(url=base_url + "/breeds/image/random/" + count)
    assert r.status_code == 200
    assert str(len(r.json()["message"])) == count
