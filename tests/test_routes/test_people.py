import json
from fastapi import status

data1 = {"first_name": "Jenny", "last_name": "Perez", "email": "j.perez@testmail.com"}
data2 = {"first_name": "Greg", "last_name": "Probst", "email": "g.greg.probst@gmail.com"}


def test_create_person(client):
    """Test creating person works and has expected values"""
    response = client.post("/person/", json.dumps(data1))
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == data1["email"]
    assert response.json()["person_id"] == 1
    assert response.json()["experience"] == []
    assert response.json()["interests"] == []


def test_duplicate_email_fails(client):
    """Test that email uniqueness is enforced"""
    dup_email = {"first_name": data2["first_name"], "last_name": data2["last_name"], "email": data1["email"]}
    response1 = client.post("/person/", json.dumps(data1))
    response2 = client.post("/person/", json.dumps(dup_email))
    assert response1.status_code == status.HTTP_201_CREATED
    assert response2.status_code == status.HTTP_400_BAD_REQUEST


def test_multiple_person_creates(client):
    """Test inserting multiple people"""
    response1 = client.post("/person/", json.dumps(data1))
    response2 = client.post("/person/", json.dumps(data2))
    assert response1.status_code == status.HTTP_201_CREATED
    assert response2.status_code == status.HTTP_201_CREATED
    assert response2.json()["person_id"] == 2


def test_missing_fields_rejected(client):
    """Test that a missing required field is rejected"""
    missing1 = {"last_name": data1["last_name"], "email": data1["email"]}
    missing2 = {"first_name": data1["first_name"], "email": data1["email"]}
    missing3 = {"first_name": data1["first_name"], "last_name": data1["last_name"]}
    response1 = client.post("/person/", json.dumps(missing1))
    response2 = client.post("/person/", json.dumps(missing2))
    response3 = client.post("/person/", json.dumps(missing3))
    assert response1.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response2.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response3.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
