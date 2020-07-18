import requests
import json
import re


def c(field_name):
    raw_result = requests.get(url='https://jsonplaceholder.typicode.com/comments')
    assert raw_result.status_code == 200
    response = json.loads(raw_result.text)
    result = {item[field_name] for item in response}
    return result


def test_1():
    for item in c('email'):
        assert item.find("@") != -1 and item.find(".") != -1
    # assert all(item.find("@") != -1 for item in c('email'))