from flask import Blueprint, request, flash
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
    db.executemany(
        'INSERT INTO images (filepath) VALUES (?)', paths
    )
    db.commit()
    
    return 'successfully added images {}'.format(paths)