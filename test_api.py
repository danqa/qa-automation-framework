import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    
    assert response.status_code == 200
    assert "email" in data
    assert data["id"] == 1

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 10

def test_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999")

    assert response.status_code == 404