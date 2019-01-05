import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

config = {
    'user'    : os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host'    : os.getenv('APP_HOST'),
    'database': os.getenv('DB_DATABASE')
}
connection = pymysql.connect(**config)
