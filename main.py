from flask import Flask, jsonify
from flaskext.mysql import MySQL
import os
from dotenv import load_dotenv

import utility

load_dotenv()

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USERNAME')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('APP_HOST')
app.config['JSON_SORT_KEYS'] = False
mysql.init_app(app)


@app.route('/', methods=['GET'])
def getVersion():
    return utility.give_response("00", os.getenv('APP_NAME'))


@app.route('/getIdentity', methods=['GET'])
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from identity ''')
    result = [dict((cur.description[i][0], value)
                   for i, value in enumerate(row)) for row in cur.fetchall()]
    return utility.give_response("00", "GET IDENTITY SUKSES", result)


if __name__ == '__main__':
    app.run()
