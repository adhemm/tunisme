from flask import Flask 
import os




def create_app(test_config=None):
    # create app 
    app = Flask(__name__, instance_relative_config=True)

    if(test_config is None):
        # load configs from py file
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    # Ensure instance folder exist

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # register api blueprints here
    from .api.auth import auth
    from .admin.admin import admin

    app.register_blueprint(auth)
    app.register_blueprint(admin)


    return(app)
