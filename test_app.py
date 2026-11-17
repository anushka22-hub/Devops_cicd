from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_student():
    response = app.test_client().get('/student')
    assert response.status_code == 200