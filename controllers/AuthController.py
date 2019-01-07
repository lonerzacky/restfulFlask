from flask import request
from flask_restful import Resource
from connection import connection
import queryUtils
import utility


# noinspection SqlResolve
class VerifyLogin(Resource):
    @staticmethod
    def post():
        global cursor
        try:
            sysuser_nama = request.form["sysuser_nama"]
            sysuser_passw = utility.create_hash(request.form["sysuser_passw"])
            cursor = connection.cursor()
            cursor.execute("""SELECT COUNT( * ) FROM sys_user WHERE sysuser_nama = %s AND sysuser_passw = %s""",
                           (sysuser_nama, sysuser_passw))
            result_count = cursor.fetchone()
            result_row = queryUtils.get_info_user(sysuser_nama, sysuser_passw)
            if result_count[0] == 1:
                return utility.give_response("00", "LOGIN SUKSES", result_row)
            else:
                return utility.give_response("01", "LOGIN GAGAL,USERNAME ATAU PASSWORD SALAH")
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()


# noinspection SqlResolve
class ChangePassword(Resource):
    @staticmethod
    def post():
        global cursor
        try:
            sysuser_id = request.form["sysuser_id"]
            old_password_from_data = queryUtils.get_old_password(sysuser_id)
            password_lama = utility.create_hash(request.form["password_lama"])
            password_baru = utility.create_hash(request.form["password_baru"])
            if password_lama == old_password_from_data:
                cursor = connection.cursor()
                cursor.execute("""UPDATE sys_user SET sysuser_passw=%s""", password_baru)
                connection.commit()
                return utility.give_response("00", "UBAH PASSWORD SUKSES")
            else:
                return utility.give_response("01", "PASSWORD LAMA TIDAK SAMA", old_password_from_data)
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()
