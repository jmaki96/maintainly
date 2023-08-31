from flask import Blueprint, render_template, request, session

from src.extensions.database import db
from src.models.user import User
from src.session_manager import SessionManager

auth_bp = Blueprint('auth_bp', __name__)
index_bp = Blueprint('index_bp', __name__)


@auth_bp.route('/logout', methods=['GET'])
def logout():
    SessionManager.log_out()
    msg = 'User logged out successfully!'

    return render_template('login.html', msg = msg)
        
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """ Handles login requests."""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user: User = db.session.execute(db.select(User).filter_by(username=username)).scalar_one_or_none()
        if not user:
            return render_template('login.html', msg = f'No user found for {username}.')

        if not user.authenticate(password):
            return render_template('login.html', msg = 'Incorrect password!')

        # Start an authenticated session
        SessionManager.log_in(user)

        return render_template('login.html', msg = 'Logged in successfully!')
    
    elif request.method == 'GET':

        msg = ''
        if SessionManager.is_logged_in():
            msg = f'User {SessionManager.get_logged_in_user_id()} is logged in.'

        return render_template('login.html', msg = msg)


@auth_bp.route('/signup', methods = ['GET', 'POST'])
def signup():
    """ Handles a new user signup request. Re-routes to login page if already exists."""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one_or_none()

        if user:
            # User already exists with this username
            return render_template('login.html', msg = f'User with username {username} already exists! Trying logging in...')

        else:
            # User does not exist - time to create
            new_user = User(
                username=username,
                email=email
            )
            new_user._set_password = password

            db.session.add(new_user)
            db.session.commit()

            return render_template('login.html', msg = 'Account created successfully! Please log in now!')
    elif request.method == 'GET':
        msg = ''
        if SessionManager.is_logged_in():
            msg = f'User {SessionManager.get_logged_in_user_id()} is logged in.'

        return render_template('signup.html', msg = msg)


@index_bp.route('/')
def index():
    return render_template('index.html')
