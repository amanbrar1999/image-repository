from flask import Blueprint, render_template
from image_repo.db import get_db

bp = Blueprint('view', __name__, url_prefix='/view')

@bp.route('')
def view_all():
    db = get_db()
    rows = db.execute(
        'SELECT * FROM images'
    ).fetchall()
    images = [row[0] for row in rows]
    return {"images": images}

@bp.route('/images')
def display_all():
    images = view_all()["images"]
    return render_template("images.html", images=images)