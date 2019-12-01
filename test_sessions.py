from sessions import app


def test_creates_session_cookie_on_post():
    response = app.test_client().post('/create-session', json={'foo': 'bar'})
    assert response.status_code == 201
    print(response.headers['Set-Cookie'])
    assert response.headers['Set-Cookie']


def test_get_datareturns_data_from_session():
    client = app.test_client()
    session_data = {'foo': 'bar'}
    response = client.post('/create-session', json=session_data)
    cookie = response.headers['Set-Cookie']
    print(cookie)
    response = client.get('/session-data', headers={'Set-Cookie': cookie})
    assert response.json == session_data
