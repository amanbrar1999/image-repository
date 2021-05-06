from flask import Blueprint, request
from image_repo.db import get_db

bp = Blueprint('delete', __name__, url_prefix='/delete')

@bp.route('', methods=["POST"])
def delete():
    db = get_db()
    data = request.get_json()
    if data is None:
        return "paths field was not provided in request form", 400
    paths = list(data['paths'])
    if paths is None:
        return "no paths were provided in paths field", 400
    
    paths = [(p,) for p in paths]
    db.executemany(
        'DELETE FROM images WHERE filepath=?', paths
    )
    db.commit()
    return 'successfully removed images {}'.format(paths)