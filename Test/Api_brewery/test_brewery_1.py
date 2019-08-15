import pytest
import requests


@pytest.mark.parametrize('dict_num, id_in_response', [(0, 2), (1, 4), (2, 44)])
def test_brewery_filter(api_client, dict_num, id_in_response):
    '''
        Проверка, что UserId в списках совпадают с ожидаемыми
    '''
    response = requests.get(api_client + "/breweries")
    assert response.json()[dict_num]['id'] == id_in_response


@pytest.mark.parametrize('state_name, state_in_list', [('new_york', 'New York'),
                                                       ('nevada', 'Nevada'),
                                                       ('california', 'California')]
                         )
def test_filter(api_client, state_name, state_in_list):
    '''
        Проверка работы фильтра
    '''
    response = requests.get(api_client + f"/breweries/?by_state={state_name}")
    for item in response.json():
        assert item['state'] == state_in_list


def test_get_brewery():
    '''
        Проверка что Id пивоварни совпадает с указанным ID в урле
    '''
    response = requests.get('https://api.openbrewerydb.org/breweries/5494')
    assert response.json()['id'] == 5494
    assert response.status_code == 200


