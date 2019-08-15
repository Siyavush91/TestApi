import json
import pytest
import requests



def test_bulldog():
    '''
        Проверка что в списке есть вложенный список с значениями
    '''
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    data = json.loads(response.content)
    message_value = data['message']
    bulldog_value = message_value['bulldog']
    assert bulldog_value == ['boston', 'english', 'french']



@pytest.mark.parametrize('image_num', [1, 2, 10])
def test_api_dogs_image(image_num):
    '''
        Проверяем, статус код и собщение в списке
    '''
    response = requests.get('https://dog.ceo/api/breeds/image/random/' + str(image_num))
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data['status'] == "success"



@pytest.mark.parametrize('breed_type', ['hound', 'bulldog', 'mountain'])
def test_api_dog(breed_type):
    '''
        Проверка что возвращается правильный текст в списке
    '''
    response = requests.get('https://dog.ceo/api/breed/'+ breed_type + '/list')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert response.encoding is None
    assert "message" in data


@pytest.mark.parametrize('breed_list', ['airedale', 'basenji', 'boxer'])
def test_api_image(breed_list):
    '''
        Проверка правильного URL в списке
    '''
    response = requests.get('https://dog.ceo/api/breed/'+ breed_list + '/images/random')
    data = json.loads(response.content)
    data1 = json.dumps(data)
    assert (data1[13:43]) == 'https://images.dog.ceo/breeds/'
