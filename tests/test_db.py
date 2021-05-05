import sqlite3
import pytest

from image_repo.db import get_db, init_db

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute("SELECT 1")

    assert "closed" in str(e.value)

def test_init_db(app):
    """If the database contains the default images from data.sql, init_db was successful"""
    with app.app_context():
        db = get_db()
        response = db.execute("SELECT name FROM sqlite_master WHERE type='table';")
        assert "images" in response.fetchone()
        rows = db.execute("SELECT * FROM images;")
        for row in rows.fetchall():
            assert "squirtle.jpg" in tuple(row) or "lucario.webp" in tuple(row)
