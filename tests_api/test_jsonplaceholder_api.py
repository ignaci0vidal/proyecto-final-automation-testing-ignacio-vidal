import requests
import pytest


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
@pytest.mark.smoke
def test_get_post_existente():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert "title" in body
    assert "body" in body
    assert "userId" in body


@pytest.mark.api
def test_crear_post():
    payload = {
        "title": "Proyecto final Automation Testing",
        "body": "Primer test POST automatizado con Requests y Pytest",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    body = response.json()

    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


@pytest.mark.api
def test_actualizar_post_con_patch():
    payload = {
        "title": "Titulo actualizado por PATCH"
    }

    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert body["title"] == payload["title"]
    assert "body" in body
    assert "userId" in body


@pytest.mark.api
def test_eliminar_post():
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    body = response.json()

    assert body == {}