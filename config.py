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
    SERVER_NAME = environ.get("SERVER_NAME") or "127.0.0.1:3000"
    ORGANIZATION_NAME = "threatnote.io"
    ORGANIZATION_KEY = "temp_key_12345"

    # API Keys
    OTX_API_KEY = environ.get("OTX_API_KEY")
    SHODAN_API_KEY = environ.get("SHODAN_API_KEY")
    RISKIQ_USERNAME = environ.get("RISKIQ_USERNAME")
    RISKIQ_KEY = environ.get("RISKIQ_KEY")
    GREYNOISE_API_KEY = environ.get("GREYNOISE_API_KEY")
    EMAILREP_API_KEY = environ.get("EMAILREP_API_KEY")
    VT_API_KEY = environ.get("VT_API_KEY")
    MISP_API_KEY = environ.get("MISP_API_KEY")
    MISP_URL = environ.get("MISP_URL")
    HIBP_API_KEY = environ.get("HIBP_API_KEY")

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
        environ.get("SQLALCHEMY_DATABASE_URI")
        or f"sqlite:///{path.join(basedir, 'threatnote/db/threatnote.db')}"
    )


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://user@localhost/foo"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{path.join(basedir, 'threatnote/db/dev.db')}"
    ORGANIZATION_KEY = "dev"


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    ORGANIZATION_KEY = "testing"
    TESTING = True
    WTF_CSRF_ENABLED = False
