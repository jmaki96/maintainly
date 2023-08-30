import os

# Core App Settings
APP_NAME = 'maintainly'

# MySQL
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'core_db')
MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_PASSWORD', 'localdebug')
MYSQL_DATABASE_URI = os.getenv('MYSQL_DATABASE_URI', f'mysql://root:{MYSQL_DATABASE_PASSWORD}@db:3306/{MYSQL_DATABASE}')
