import os

# Core App Settings
APP_NAME = 'maintainly'
APP_SECRET_KEY = os.getenv('APP_SECRET_KEY', 'aaHbA2_a2J9ue49SOuE6xny7VrL6SV0nzlPI3tW0j_Q')  # prod should load a different key, this is just for debug

# MySQL
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'core_db')
MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_PASSWORD', 'localdebug')  # prod should load a different key, this is just for debug
MYSQL_DATABASE_URI = os.getenv('MYSQL_DATABASE_URI', f'mysql://root:{MYSQL_DATABASE_PASSWORD}@db:3306/{MYSQL_DATABASE}')
