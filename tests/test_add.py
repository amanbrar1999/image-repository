import pytest

def test_add_images(client):
    response1 = client.get("/view")
    assert b"charizard.jpg" not in response1.data

    response2 = client.post("/add", json={"paths": ["charizard.png", "luxray.webp"]})
    assert response2.status_code == 200

    response3 = client.get("/view")
    assert b"charizard.png" in response3.data and b"luxray.webp" in response3.data

def test_add_image_invalid(client):
    response2 = client.post("/add")
    assert response2.status_code == 400

def test_add_duplicate_image(client):
    response2 = client.post("/add", json={"paths": ["squirtle.jpg"]})
    assert response2.status_code == 400

def test_add_image_does_not_exist(client):
    response = client.post("/add", json={"paths": ["pic.png"]})
    assert response.status_code == 400