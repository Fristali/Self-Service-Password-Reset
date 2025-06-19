import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    rv = client.get('/')
    assert b'Self-Service Password Reset' in rv.data

def test_user_not_found(client):
    rv = client.post('/', data={'username': 'notarealuser'})
    assert b'User not found.' in rv.data

def test_security_questions_page(client):
    rv = client.post('/', data={'username': 'alice'}, follow_redirects=True)
    assert b'Answer Security Questions' in rv.data

def test_password_policy(client):
    from app.routes import validate_password
    with client.application.app_context():
        assert not validate_password('short')
        assert not validate_password('alllowercase1!')
        assert not validate_password('ALLUPPERCASE1!')
        assert not validate_password('NoNumber!')
        assert not validate_password('NoSpecial1')
        assert validate_password('Valid1!a')
