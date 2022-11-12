# Class-based Flask app configuration.
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    # Configuration from environment variables.'

    SECRET_KEY = environ.get("SECRET_KEY") or "123lkjasdkfjl1344lkjqwer"
    FLASK_ENV = environ.get("FLASK_ENV")
    FLASK_APP = "wsgi.py"
    FLASK_DEBUG = True
    # SERVER_NAME = environ.get("SERVER_NAME") or "127.0.0.1:3001"
    # SERVER_NAME = "127.0.0.1:3001"
    SERVER_NAME = "172.16.1.198:3001"
    # SERVER_NAME = "threatnote.lab:3001"
    # app.config["OTX_API_KEY"] = os.environ.get("OTX_API_KEY")

    # app.config["SHODAN_API_KEY"] = os.environ.get("SHODAN_API_KEY")

    # app.config["RISKIQ_USERNAME"] = os.environ.get("RISKIQ_USERNAME")
    # app.config["RISKIQ_KEY"] = os.environ.get("RISKIQ_KEY")
    # app.config["GREYNOISE_API_KEY"] = os.environ.get("GREYNOISE_API_KEY")
    # app.config["EMAILREP_API_KEY"] = os.environ.get("EMAILREP_API_KEY")
    # app.config["VT_API_KEY"] = os.environ.get("VT_API_KEY")
    # app.config["MISP_API_KEY"] = os.environ.get("MISP_API_KEY")
    # app.config["MISP_URL"] = os.environ.get("MISP_URL")
    # app.config["HIBP_API_KEY"] = os.environ.get("HIBP_API_KEY")

    # Flask assets
    LESS_BIN = environ.get("LESS_BIN")
    ASSETS_DEBUG = True
    LESS_RUN_IN_DEBUG = True

    # Static assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{path.join(basedir, 'threatnote/db/threatnote.db')}"
    )

    # SQLALCHEMY_DATABASE_URI = (
    # environ.get("SQLALCHEMY_DATABASE_URI")
    # or f"sqlite:///{os.path.join(basedir, '../db/threatnote.db')}"
    # )

    # API
