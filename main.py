from flask import Flask, request
from dotenv import load_dotenv
from flask_restful import Api, Resource
from connection import connection
import utility
import os

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False


class GetVersion(Resource):
    @staticmethod
    def get():
        return utility.give_response("00", os.getenv('APP_NAME'))


class GetIdentity(Resource):
    @staticmethod
    def get():
        try:
            cursor = connection.cursor()
            cursor.execute('''select * from identity ''')
            result = [dict((cursor.description[i][0], value)
                           for i, value in enumerate(row)) for row in cursor.fetchall()]
            return utility.give_response("00", "GET IDENTITY SUKSES", result)
        except Exception as e:
            return utility.give_response("01", e)


class InsertIdentity(Resource):
    @staticmethod
    def post():
        try:
            cursor = connection.cursor()
            name = request.form["name"]
            address = request.form["address"]
            cursor.execute("""INSERT INTO identity (name,address) VALUES (%s,%s)""", (name, address))
            connection.commit()
            return utility.give_response("00", "INSERT IDENTITY SUKSES")
        except Exception as e:
            return utility.give_response("01", e)


api.add_resource(GetVersion, '/')
api.add_resource(GetIdentity, '/getIdentity')
api.add_resource(InsertIdentity, '/insertIdentity')

if __name__ == '__main__':
    app.run()
