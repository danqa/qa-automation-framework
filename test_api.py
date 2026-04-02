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

def test_create_post():
    payload = {
        "title": "QA Automation",
        "body": "Testing POST requests",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert "id" in data

def test_create_post_missing_fields():
    payload = {}
    response = requests.post(f"{BASE_URL}/posts", json=payload)

    # JSONPlaceholder is lenient but should still return 201
    # In a real API this would return 400 - document that expectation
    assert response.status_code == 201

def test_update_post():
    payload = {
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Updated Title"

@pytest.mark.xfail(reason="JSONPlaceholder echoes unknown fields back in response - API should reject or ignore unknown fields")
def test_update_post_with_invalid_fields():
    payload = {
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1,
        "blah": "test"        # unknown field
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    data = response.json()

    assert response.status_code == 200
    assert "blah" not in data

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200