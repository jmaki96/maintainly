from flask import Blueprint, render_template, request

from src.extensions.database import db
from src.models.user import User
from src.session_manager import SessionManager

app_bp = Blueprint('app_bp', __name__)

@app_bp.route('/app', methods=['GET', 'POST'])
def app():

    if not SessionManager.is_logged_in():
        return render_template('login.html', msg = 'You must log in to access the app.')
    

    return render_template('app.html')
