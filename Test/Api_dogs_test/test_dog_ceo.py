import pytest
import requests
import json


def test_bulldog():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    data = json.loads(r.content)
    message_value = data['message']
    bulldog_value = message_value['bulldog']
    assert bulldog_value == ['boston', 'english', 'french']


@pytest.mark.parametrize('image_num', [1, 2, 10])
def test_api_dogs_image(image_num):
    r = requests.get('https://dog.ceo/api/breeds/image/random/' + str(image_num))
    data = json.loads(r.content)
    assert r.status_code == 200
    assert data['status'] == "success"



@pytest.mark.parametrize('breed_type', ['hound', 'bulldog', 'mountain'])
def test_api_dog(breed_type):
    r = requests.get('https://dog.ceo/api/breed/'+ breed_type + '/list')
    data = json.loads(r.content)
    assert r.status_code == 200
    assert r.encoding is None
    assert "message" in data


@pytest.mark.parametrize('breed_list', ['airedale', 'basenji', 'boxer'])
def test_api_image(breed_list):
    r = requests.get('https://dog.ceo/api/breed/'+ breed_list + '/images/random')
    data = json.loads(r.content)
    data1 = json.dumps(data)
    assert (data1[13:43]) == 'https://images.dog.ceo/breeds/'
