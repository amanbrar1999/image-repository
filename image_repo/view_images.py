from flask import Blueprint, request, render_template
from image_repo.db import get_db

bp = Blueprint('view', __name__, url_prefix='/view')

@bp.route('')
def view():
    db = get_db()
    image = request.args.get('image')
    if image:
        # query only 1 image
        rows = db.execute(
            'SELECT * FROM images WHERE filepath=?', (image,)
        ).fetchall()
        images = [row[0] for row in rows]
        return {"images": images}
    else:
        # query all images
        rows = db.execute(
            'SELECT * FROM images'
        ).fetchall()
        images = [row[0] for row in rows]
        return {"images": images}

@bp.route('/images')
def display_all():
    db = get_db()
    image = request.args.get('image')
    if image:
        # query only 1 image
        rows = db.execute(
            'SELECT * FROM images WHERE filepath=?', (image,)
        ).fetchall()
        images = [row[0] for row in rows]
        return render_template("images.html", images=images)
    else:
        # query all images
        rows = db.execute(
            'SELECT * FROM images'
        ).fetchall()
        images = [row[0] for row in rows]
        return render_template("images.html", images=images)