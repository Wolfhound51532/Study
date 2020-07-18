import requests
import json


def c(field_name):
    raw_result = requests.get(url='https://jsonplaceholder.typicode.com/albums')
    assert raw_result.status_code == 200
    response = json.loads(raw_result.text)
    result = {item[field_name] for item in response}
    return result


def test_1():
    assert all(isinstance(item, int) for item in c('userId'))


def test_2():
    assert all(isinstance(item, int) for item in c('id'))


def test_3():
    assert all(isinstance(item, str) for item in c('title'))
