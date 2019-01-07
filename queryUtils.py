from connection import connection


# noinspection SqlResolve
def get_old_password(sysuser_id):
    cursor = connection.cursor()
    cursor.execute("""SELECT sysuser_passw FROM sys_user WHERE sysuser_id=%s""", sysuser_id)
    result = cursor.fetchone()
    return result[0]
