from flask import Flask, request
from dotenv import load_dotenv
from flask_restful import Api, Resource
from connection import *
import utility

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False


class GetVersion(Resource):
    def get(self):
        return utility.give_response("00", os.getenv('APP_NAME'))


class GetIdentity(Resource):
    def get(self):
        try:
            cur = mysql.connect().cursor()
            cur.execute('''select * from identity ''')
            result = [dict((cur.description[i][0], value)
                           for i, value in enumerate(row)) for row in cur.fetchall()]
            return utility.give_response("00", "GET IDENTITY SUKSES", result)
        except Exception as e:
            return utility.give_response("01", e)


class InsertIdentity(Resource):
    def post(self):
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


api.add_resource(GetVersion, '/')
api.add_resource(GetIdentity, '/getIdentity')
api.add_resource(InsertIdentity, '/insertIdentity')


if __name__ == '__main__':
    app.run()
