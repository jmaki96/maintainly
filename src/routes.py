from flask import Blueprint, send_from_directory, render_template, request

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/signup', methods = ['POST'])
def signup():
    """ Handles a new user signup request. May raise an exception if the user is already found."""

    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    

    return send_from_directory('static', 'index.html')

