from flask import Blueprint, request, flash
from image_repo.db import get_db

bp = Blueprint('add', __name__, url_prefix='/add')

@bp.route('', methods=["POST"])
def add():
    db = get_db()
    path = str(request.form['path'])
    if path is None:
        flash("path field was not provided in request form")
    db.execute(
        'INSERT INTO images (filepath) VALUES (?)', (path,)
    )
    db.commit()
    return 'successfully added image {}'.format(path)