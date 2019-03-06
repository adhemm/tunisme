from flask import Blueprint, url_for, jsonify, render_template


admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')


@admin.route('/')
def admin_login():
    return(render_template('login.html'))