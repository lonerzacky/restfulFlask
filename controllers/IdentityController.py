from flask import request
from flask_restful import Resource
from connection import connection
import utility


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


class UpdateIdentity(Resource):
    @staticmethod
    def put(id_identity):
        try:
            cursor = connection.cursor()
            name = request.form["name"]
            address = request.form["address"]
            cursor.execute("""UPDATE identity SET name=%s , address=%s WHERE id=%s""", (name, address, id_identity))
            connection.commit()
            return utility.give_response("00", "UPDATE IDENTITY SUKSES")
        except Exception as e:
            return utility.give_response("01", e)


class DeleteIdentity(Resource):
    @staticmethod
    def delete(id_identity):
        try:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM identity WHERE id=%s""", (id_identity))
            connection.commit()
            return utility.give_response("00", "DELETE IDENTITY SUKSES")
        except Exception as e:
            return utility.give_response("01", e)
