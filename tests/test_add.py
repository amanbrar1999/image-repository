import pytest

def test_add_image(client):
    response1 = client.get("/view")
    assert b"charizard.jpg" not in response1.data

    response2 = client.post("/add", data={"path": "charizard.jpg"})
    assert response2.status_code == 200

    response3 = client.get("/view")
    assert b"charizard.jpg" in response3.data

def test_add_image_invalid(client):
    response2 = client.post("/add")
    assert response2.status_code == 400