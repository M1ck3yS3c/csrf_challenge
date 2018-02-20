# app/__init__.py


# third-party imports
from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

#importing bootstrap
from flask_bootstrap import Bootstrap

#initialize bootstrap


# db variable initialization
db = SQLAlchemy()

#login manager initialization
login_manager = LoginManager()



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')


    #Add a CSRF secret key
    app.config.update(dict(
        SECRET_KEY="C@ntg3tme!n",
        WTF_CSRF_SECRET_KEY="C@ntg3tme!n"
    ))

    #instantiating database
    db.init_app(app)

    #instantiating bootstrap
    Bootstrap(app)

    #intializing login
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"



    #Migrating our models to our database
    migrate = Migrate(app, db)

    #creating blueprints
    from app import models


    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .message import message as message_blueprint
    app.register_blueprint(message_blueprint)

    from .profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    from .secret import secret as secret_blueprint
    app.register_blueprint(secret_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
   

    return app
