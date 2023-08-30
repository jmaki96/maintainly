import click
from flask.cli import AppGroup


db_cli = AppGroup('db')

@db_cli.command('init')
def init_db():
    print('init db!')
