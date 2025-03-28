from http import HTTPStatus


def test_get_root_should_return_ok(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!!!'}
