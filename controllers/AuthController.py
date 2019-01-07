from flask import request
from flask_restful import Resource
from connection import connection
import queryUtils
import utility


# noinspection SqlResolve
class ChangePassword(Resource):
    @staticmethod
    def post():
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
