import sqlite3
from flask import Blueprint, request
from image_repo.db import get_db
import os

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('', methods=["POST"])
def add():
    db = get_db()
    data = request.get_json()
    if data is None:
        return "paths field was not provided in request form", 400
    paths = list(data['paths'])
    if paths is None:
        return "no paths were provided in paths field", 400

    for fp in paths:
        print(os.path.isfile('image_repo/static/{}'.format(fp)))
        if not os.path.isfile('image_repo/static/{}'.format(fp)):
            return 'the following image does not exist, aborted query: {}'.format(fp), 400
    
    paths = [(p,) for p in paths]
    try:
        db.executemany(
            'INSERT INTO images (filepath) VALUES (?)', paths
        )
        db.commit()
    except sqlite3.IntegrityError:
        return "Attempted to add an image that already exists in database, aborted query", 400
    
    return 'successfully added images {}'.format(paths)