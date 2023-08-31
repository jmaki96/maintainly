from flask import Flask

from src.commands import db_cli
from src.extensions.database import db
from src.settings import APP_NAME, MYSQL_DATABASE_URI
from src.routes import index_bp


def init_app() -> Flask:
    """Standard Flask app factory."""

    app = Flask(APP_NAME, static_url_path='/')

    # Configuration (should probably move to an object based config later)
    app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_DATABASE_URI

    # Initialize extensions
    db.init_app(app)

    with app.app_context():

        # Register routes
        app.register_blueprint(index_bp, prefix='/')

        # Register commands
        app.cli.add_command(db_cli)
        
    return app
