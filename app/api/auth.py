from flask import Blueprint
from flask import url_for, jsonify

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route('/')
def check_login():
    data = {
        "error":"Your are not registred user!"
    }
    return(jsonify(data))

