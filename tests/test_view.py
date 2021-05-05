import pytest

def test_view_defaults(client):
    response = client.get("/view")
    assert b"squirtle.jpg" in response.data
    assert b"lucario.webp" in response.data

def test_view_image_defaults(client):
    response = client.get("/view/images")
    assert b"squirtle.jpg" in response.data
    assert b"lucario.webp" in response.data