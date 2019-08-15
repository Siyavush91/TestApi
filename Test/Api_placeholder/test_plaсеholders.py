import random
import pytest


@pytest.mark.parametrize('userId, userId_in_response', [(1, 1), (2, 2)])
def test_api_filtering(api_client, userId, userId_in_response):
    response = api_client.get(
        path="/posts",
        params={'userId': userId}
    )
    # Проверка что случайный пост от пользователя с ожидаемым id
    random_post_number = random.randint(0, 10)
    assert response.json()[random_post_number]['userId'] == userId_in_response


def test_api_filter(api_client):
    response = api_client.get(
        path="/posts",
        params={'userId': 2}
    )
    #Проверка, что посты принадлежат одному пользователю
    for post in response.json():
        assert post['userId'] == 2


@pytest.mark.parametrize('input_id, output_id',
                         [(10000, '10000'), (1, '1'), (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('foo', 'foo'), ('', '')])
def test_api_post_request(api_client, input_id, output_id, input_title, output_title):
    res = api_client.post(
        path="/posts",
        data={'title': input_title,
              'body': 'bar',
              'userId': input_id
              }).json()
    #Проверка, что переданные данные опубликуются в посте
    assert res['title'] == output_title
    assert res['body'] == 'bar'
    assert res['userId'] == output_id


def test_api_delete_post(api_client):
    response = api_client.delete(
        path="/posts",
        params={'userId': 10000}
    ).json()
    #Проверка, что пост пользователя удаляется
    assert response == {}
