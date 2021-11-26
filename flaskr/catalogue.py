from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('catalogue', __name__, url_prefix="/catalogue")

@bp.route('/')
def index():
    db = get_db()
    boat_posts = db.execute(
        'SELECT boat_type, capacity_min, capacity_max, cost_per_2_hours, deposit_per_boat, quantity, rental_location'
        ' FROM boat_item'
    ).fetchall()
    return render_template(
        'catalogue/index.html',
        boat_posts=boat_posts,
    )
