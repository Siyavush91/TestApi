import requests

def test_parser(url_param):
    r = requests.get(url_param)
    assert r.status_code == 200
