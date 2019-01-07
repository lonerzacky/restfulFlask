import hashlib

from flask import jsonify


def give_response(response_code, response_message, response_data=""):
    return jsonify(
        {'response_code': response_code, 'response_message': response_message, 'response_data': response_data})


def create_hash(var):
    return hashlib.sha1(var.encode()).hexdigest()
