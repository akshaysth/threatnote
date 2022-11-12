# from threatnote.config import db
# from threatnote.config import create_app
# from threatnote import api as Api

import os

from flask import Flask
from flask_login import LoginManager
from flask_redis import FlaskRedis
from flask_wtf import CSRFProtect
from config import Config


r = FlaskRedis()
loginmanager = LoginManager()
csrf = CSRFProtect()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    #    with app.app_context():

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from threatnote.models import db

    db.init_app(app)
    r.init_app(app)

    loginmanager.login_view = "auth.login"
    loginmanager.init_app(app)
    csrf.init_app(app)

    from threatnote.models import User

    @loginmanager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    with app.app_context():
        # blueprint for auth routes in our app
        from threatnote.auth import auth_bp as auth_blueprint
        from threatnote.main import main_bp as main_blueprint
        from threatnote.models import models_bp as models_blueprint
        from threatnote.requirements import reqs_bp as requirements_blueprint
        from threatnote.reports import reports_bp as reports_blueprint
        from threatnote.indicators import indicators_bp as indicators_blueprint
        from threatnote.consumers import consumers_bp as consumers_blueprint
        from threatnote.settings import settings_bp as settings_blueprint

    app.register_blueprint(models_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(requirements_blueprint)
    app.register_blueprint(reports_blueprint)
    app.register_blueprint(indicators_blueprint)
    app.register_blueprint(consumers_blueprint)
    app.register_blueprint(settings_blueprint)

    return app
