from flask import Blueprint, url_for, jsonify, render_template


admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='/admin/templates')


@admin.route('/')
def admin_login():
    return("</h2>Admin Login Page</h2>")