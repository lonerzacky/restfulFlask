from flask import Flask, request
from dotenv import load_dotenv
import utility
from connection import *

load_dotenv()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/', methods=['GET'])
def get_version():
    return utility.give_response("00", os.getenv('APP_NAME'))


@app.route('/getIdentity', methods=['GET'])
def get_identity():
    try:
        cur = mysql.connect().cursor()
        cur.execute('''select * from identity ''')
        result = [dict((cur.description[i][0], value)
                       for i, value in enumerate(row)) for row in cur.fetchall()]
        return utility.give_response("00", "GET IDENTITY SUKSES", result)
    except Exception as e:
        return utility.give_response("01", e)


@app.route('/insertIdentity', methods=['POST'])
def insert_identity():
    try:
        name = request.form["name"]
        address = request.form["address"]
        con = mysql.connect()
        cur = con.cursor()
        cur.execute("""INSERT INTO identity (name,address) VALUES (%s,%s)""", (name, address))
        con.commit()
        return utility.give_response("00", "INSERT IDENTITY SUKSES")
    except Exception as e:
        return utility.give_response("01", e)


if __name__ == '__main__':
    app.run()
