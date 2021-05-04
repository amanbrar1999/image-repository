from flask import Blueprint, request, flash
from image_repo.db import get_db

bp = Blueprint('delete', __name__, url_prefix='/delete')

@bp.route('', methods=["POST"])
def add():
    db = get_db()
    path = str(request.form['path'])
    print(request.form)
    print(path)
    if path is None:
        flash("path field was not provided in request form")
    db.execute(
        'DELETE FROM images WHERE filepath=?', (path,)
    )
    db.commit()
    return 'successfully removed image {}'.format(path)