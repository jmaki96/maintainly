from flask import Blueprint, send_from_directory, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def index():
    # return f"OK - so we're currently here {__file__} - why can't I find static? app path is {app.root_path}"
    return send_from_directory('static', 'index.html')

