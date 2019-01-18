from flask_restful import Resource
from connection import connection

import utility


# noinspection SqlResolve
class GetRmodul(Resource):
    @staticmethod
    def get():
        global cursor
        try:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM sys_rmodul""")
            result = [dict((cursor.description[i][0], value)
                           for i, value in enumerate(row)) for row in cursor.fetchall()]
            connection.commit()
            return utility.give_response("00", "GET RMODUL SUKSES", result)
        except Exception as e:
            return utility.give_response("01", str(e))
