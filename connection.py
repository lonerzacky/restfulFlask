from flaskext.mysql import MySQL
import os

from main import app

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USERNAME')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('APP_HOST')
mysql.init_app(app)
