import click
from flask.cli import AppGroup, with_appcontext

from src.extensions.database import db

# Probably a better place to do this import, but embrace the jank for now
from src.models.user import User

db_cli = AppGroup('db')

@db_cli.command('init')
@with_appcontext
def init_db():
    print('begining db init')

    db.create_all()

    print('db init complete')


@db_cli.command('insert_user')
@with_appcontext
def insert_user():
    test_user = User(id=1, username='username1', email='my_email@domain.com')

    db.session.add(test_user)
    db.session.commit()


@db_cli.command('get_user')
@click.argument('id')
@with_appcontext
def get_user(id: int):
    user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()

    print(user)
