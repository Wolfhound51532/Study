import requests
import json
from vars import url


def c(field_name):
    raw_result = requests.get(url=url+'comments')
    assert raw_result.status_code == 200
    response = json.loads(raw_result.text)
    result = {item[field_name] for item in response}
    return result


def test_1():
    for item in c('email'):
        assert item.find("@") != -1 and item.find(".") != -1
