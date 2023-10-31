from db.model import User
from service.authen import get_password_hash


def test_auth(client, db, init_db):
    user = User(
        email='mail@example.com',
        password=get_password_hash('password')
    )
    db.add(user)
    db.commit()
    response = client.post('/auth', json={
        'email': 'mail@example.com',
        'password': 'password'
    })
    assert response.status_code == 200
    token = response.json()['token']

    headers = {'Authorization': f'Bearer {token}'}
    response = client.get('/logined', headers=headers)
    assert response.status_code == 200
