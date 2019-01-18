from flask import request
from flask_restful import Resource
from connection import connection

import utility


# noinspection SqlResolve
class GetRole(Resource):
    @staticmethod
    def get():
        global cursor
        try:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM sys_role""")
            result = [dict((cursor.description[i][0], value)
                           for i, value in enumerate(row)) for row in cursor.fetchall()]
            return utility.give_response("00", "GET ROLE SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()


# noinspection SqlResolve
class InsertRole(Resource):
    @staticmethod
    def post():
        global cursor
        try:
            sysrole_kode = request.form["sysrole_kode"]
            sysrole_nama = request.form["sysrole_nama"]
            cursor = connection.cursor()
            cursor.execute("""INSERT sys_role (sysrole_kode,sysrole_nama) VALUES (%s,%s)""",
                           (sysrole_kode, sysrole_nama))
            connection.commit()
            return utility.give_response("00", "INSERT ROLE SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()


# noinspection SqlResolve
class UpdateRole(Resource):
    @staticmethod
    def put(sysrole_kode):
        global cursor
        try:
            sysrole_nama = request.form["sysrole_nama"]
            cursor = connection.cursor()
            cursor.execute("""UPDATE sys_role SET sysrole_nama=%s WHERE sysrole_kode=%s""",
                           (sysrole_nama, sysrole_kode))
            connection.commit()
            return utility.give_response("00", "UPDATE ROLE SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()


# noinspection SqlResolve
class DeleteRole(Resource):
    @staticmethod
    def delete(sysrole_kode):
        global cursor
        try:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM sys_role WHERE sysrole_kode=%s""", sysrole_kode)
            connection.commit()
            return utility.give_response("00", "DELETE ROLE SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()
