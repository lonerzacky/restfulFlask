from flask import request
from flask_restful import Resource
from connection import connection

import utility


# noinspection SqlResolve
class GetModul(Resource):
    @staticmethod
    def get():
        global cursor
        try:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM sys_modul""")
            result = [dict((cursor.description[i][0], value)
                           for i, value in enumerate(row)) for row in cursor.fetchall()]
            connection.commit()
            return utility.give_response("00", "GET MODUL SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()


# noinspection SqlResolve
class InsertModul(Resource):
    @staticmethod
    def post():
        global cursor
        try:
            sysmodul_kode = request.form["sysmodul_kode"]
            sysmodul_nama = request.form["sysmodul_nama"]
            sysmodul_url = request.form["sysmodul_url"]
            sysmodul_icon = request.form["sysmodul_icon"]
            sysmodul_parent = request.form["sysmodul_parent"]
            if not sysmodul_parent:
                sysmodul_parent = None
            sysmodul_no_urut = request.form["sysmodul_no_urut"]
            cursor = connection.cursor()
            cursor.execute(
                """INSERT INTO sys_modul (sysmodul_kode,sysmodul_nama,sysmodul_url,sysmodul_icon,sysmodul_parent,sysmodul_no_urut) VALUES (%s,%s,%s,%s,%s,%s)""",
                (sysmodul_kode, sysmodul_nama, sysmodul_url, sysmodul_icon, sysmodul_parent, sysmodul_no_urut))
            connection.commit()
            return utility.give_response("00", "INSERT MODUL SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()


# noinspection SqlResolve
class UpdateModul(Resource):
    @staticmethod
    def put(sysmodul_kode):
        global cursor
        try:
            sysmodul_nama = request.form["sysmodul_nama"]
            sysmodul_url = request.form["sysmodul_url"]
            sysmodul_icon = request.form["sysmodul_icon"]
            sysmodul_parent = request.form["sysmodul_parent"]
            if not sysmodul_parent:
                sysmodul_parent = None
            sysmodul_no_urut = request.form["sysmodul_no_urut"]
            cursor = connection.cursor()
            cursor.execute(
                """UPDATE sys_modul SET sysmodul_nama=%s,sysmodul_url=%s,sysmodul_icon=%s,sysmodul_parent=%s,sysmodul_no_urut=%s WHERE sysmodul_kode=%s""",
                (sysmodul_nama, sysmodul_url, sysmodul_icon, sysmodul_parent, sysmodul_no_urut, sysmodul_kode))
            connection.commit()
            return utility.give_response("00", "UPDATE MODUL SUKSES")
        except Exception as e:
            return utility.give_response("01", str(e))
        finally:
            cursor.close()

