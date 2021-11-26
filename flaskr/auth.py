import functools
from abc import ABC, abstractmethod

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app as app
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

class Auth(ABC):
    @abstractmethod
    def register(request):
        pass

    @abstractmethod
    def login(request):
        pass

class UserAuth(Auth):
    def register(self, request):
        app.logger.info("Registering User")
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.user.login"))

        flash(error)

    def login(self, request):
        app.logger.info("Login User")
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)


class EmployeeAuth(Auth):
    def register(self, request):
        app.logger.info("Registering Employee")
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.employee.login"))

        flash(error)

    def login(self, request):
        app.logger.info("Login Employee")
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

@bp.route('/user/register', methods=('GET', 'POST'))
def user_register():
    if request.method == 'POST':
        auth = UserAuth()
        auth.register(request)
    return render_template('auth/user/register.html')

@bp.route('/user/login', methods=('GET', 'POST'))
def user_login():
    if request.method == 'POST':
        auth = UserAuth()
        auth.login(request)
    return render_template('auth/user/login.html')


@bp.route('/employee/register', methods=('GET', 'POST'))
def user_register():
    if request.method == 'POST':
        auth = EmployeeAuth()
        auth.register(request)
    return render_template('auth/employee/register.html')

@bp.route('/employee/login', methods=('GET', 'POST'))
def user_login():
    if request.method == 'POST':
        auth = EmployeeAuth()
        auth.login(request)
    return render_template('auth/employee/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view