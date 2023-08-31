from flask import Flask

from src.commands import db_cli
from src.extensions.bcrypt import bcrypt
from src.extensions.database import db
from src.settings import APP_NAME, MYSQL_DATABASE_URI
from src.routes import auth_bp, index_bp


def init_app() -> Flask:
    """Standard Flask app factory."""

    app = Flask(APP_NAME, static_url_path='/')

    # Configuration (should probably move to an object based config later)
    app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_DATABASE_URI
    app.config['BCRYPT_LOG_ROUNDS'] = 8  # Should probably actually tune this, but whatever

    # Initialize extensions
    bcrypt.init_app(app)
    db.init_app(app)

    with app.app_context():

        # Register routes
        app.register_blueprint(auth_bp, url_prefix='/')
        app.register_blueprint(index_bp, url_prefix='/')

        # Register commands
        app.cli.add_command(db_cli)
        
    return app
