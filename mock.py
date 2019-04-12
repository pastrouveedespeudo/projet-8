from nose.tools import assert_true
import requests


def test_request_response():
    
    path = "https://fr.openfoodfacts.org/categories"
    response = requests.get(path)

    assert_true(response.ok)
