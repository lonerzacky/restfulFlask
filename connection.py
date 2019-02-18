import os
import pymysql.cursors
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

config = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('APP_DB_HOST'),
    'database': os.getenv('DB_DATABASE'),
    'unix_socket': os.getenv('DB_UNIX_SOCKET')
}
connection = pymysql.connect(**config)
