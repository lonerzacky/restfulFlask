from flask import request
from flask_restful import Resource
from connection import connection
import utility


# noinspection SqlResolve
class GetUser(Resource):
    @staticmethod
    def get():
        try:
            cursor = connection.cursor()
            cursor.execute("""SELECT sys_user.sysuser_id, sys_role.sysrole_kode, sys_role.sysrole_nama, 
            sys_user.sysuser_nama,sys_user.sysuser_namalengkap,sys_user.sysuser_email
            FROM sys_user 
            INNER JOIN sys_role ON sys_user.sysrole_kode = sys_role.sysrole_kode""")
            result = [dict((cursor.description[i][0], value)
                           for i, value in enumerate(row)) for row in cursor.fetchall()]
            return utility.give_response("00", "GET USER SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))


# noinspection SqlResolve
class InsertUser(Resource):
    @staticmethod
    def post():
        try:
            sysuser_id = request.form["sysuser_id"]
            sysrole_kode = request.form["sysrole_kode"]
            sysuser_nama = request.form["sysuser_nama"]
            sysuser_passw = utility.create_hash(request.form["sysuser_passw"])
            sysuser_namalengkap = request.form["sysuser_namalengkap"]
            sysuser_email = request.form["sysuser_email"]
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO sys_user(sysuser_id, sysrole_kode, sysuser_nama,
             sysuser_passw, sysuser_namalengkap, sysuser_email) 
             VALUES (%s, %s, %s, %s, %s, %s)""",
                           (sysuser_id, sysrole_kode, sysuser_nama, sysuser_passw, sysuser_namalengkap, sysuser_email))
            connection.commit()
            return utility.give_response("00", "INSERT USER SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))


# noinspection SqlResolve
class UpdateUser(Resource):
    @staticmethod
    def put(sysuser_id):
        try:
            cursor = connection.cursor()
            sysrole_kode = request.form["sysrole_kode"]
            sysuser_nama = request.form["sysuser_nama"]
            sysuser_namalengkap = request.form["sysuser_namalengkap"]
            sysuser_email = request.form["sysuser_email"]
            cursor.execute("""UPDATE sys_user SET sysrole_kode = %s, sysuser_nama = %s, 
            sysuser_namalengkap = %s, sysuser_email = %s WHERE sysuser_id = %s""",
                           (sysrole_kode, sysuser_nama, sysuser_namalengkap, sysuser_email, sysuser_id))
            connection.commit()
            return utility.give_response("00", "UPDATE USER SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))


# noinspection SqlResolve
class DeleteUser(Resource):
    @staticmethod
    def delete(sysuser_id):
        try:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM sys_user WHERE sysuser_id = %s""", sysuser_id)
            connection.commit()
            return utility.give_response("00", "HAPUS USER SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
