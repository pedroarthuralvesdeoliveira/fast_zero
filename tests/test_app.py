from fast_zero.schemas import UserPublic


def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == 200  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_user_exists(client, user):
    response = client.get(f'/user_exists/?username={"Teste"}')
    assert response.status_code == 400
    assert response.json() == {'detail': 'Username already registered'}


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'user': {
            'username': 'bob',
            'email': 'bob@example.com',
            'id': 1,
        }
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_read_user(client, user):
    response = client.get(f'/read_user/?user_id={1}')
    assert response.status_code == 200
    assert response.json() == {
        'user': {'id': 1, 'username': 'Teste', 'email': 'teste@test.com'}
    }


def test_read_inexistent_user(client, user):
    response = client.get(f'/read_user/?user_id={2}')
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
