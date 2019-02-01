import datetime
import json
from flask import request
from connection import connection


# noinspection SqlResolve
def get_old_password(sysuser_id):
    cursor = connection.cursor()
    cursor.execute("""SELECT sysuser_passw FROM sys_user WHERE sysuser_id=%s""", sysuser_id)
    result = cursor.fetchone()
    return result[0]


# noinspection SqlResolve
def get_info_user(sysuser_nama, sysuser_passw):
    cursor = connection.cursor()
    cursor.execute("""SELECT sysuser_id,sys_role.sysrole_kode,sys_role.sysrole_nama,
    sysuser_nama,sysuser_namalengkap,sysuser_email FROM sys_user 
    INNER JOIN sys_role ON sys_user.sysrole_kode = sys_role.sysrole_kode WHERE sysuser_nama=%s AND sysuser_passw=%s""",
                   (sysuser_nama, sysuser_passw))
    result = [dict((cursor.description[i][0], value)
                   for i, value in enumerate(row)) for row in cursor.fetchall()]
    return result


# noinspection SqlResolve
def create_log(response, status):
    cursor = connection.cursor()
    now = datetime.datetime.now()
    request_time = now.strftime("%Y-%m-%d %H:%M")
    if not request.form:
        request_form = json.dumps("none")
    else:
        request_form = json.dumps(request.form)
    cursor.execute(
        """INSERT INTO logservice (uri,method,params,ip_address,request_time,response,status) VALUES (%s,%s,%s,%s,%s,%s,%s)""",
        (request.base_url, request.method, request_form, request.remote_addr, request_time, response, status))
    connection.commit()
