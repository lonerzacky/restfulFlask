from flask import Flask, jsonify
from flaskext.mysql import MySQL
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USERNAME')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('APP_HOST')

mysql.init_app(app)


@app.route('/')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from identity ''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection': r})


if __name__ == '__main__':
    app.run()
