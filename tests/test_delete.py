import pytest

def test_delete_image(client):
    response1 = client.get("/view")
    assert b"squirtle.jpg" in response1.data

    response2 = client.post("/delete", data={"path": "squirtle.jpg"})
    assert response2.status_code == 200

    response3 = client.get("/view")
    assert b"squirtle.jpg" not in response3.data

def test_delete_image_invalid(client):
    response2 = client.post("/delete")
    assert response2.status_code == 400