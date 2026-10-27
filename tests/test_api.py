from fastapi.testclient import TestClient
from src.api import app, items

client = TestClient(app)


def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello API'}


def test_create_and_get_items():
    items.clear()  # Очищаем перед тестом
    response = client.post('/items?name=TestItem')
    assert response.status_code == 200
    assert response.json()['item'] == 'TestItem'

    response = client.get('/items')
    assert response.status_code == 200
    assert 'TestItem' in response.json()
