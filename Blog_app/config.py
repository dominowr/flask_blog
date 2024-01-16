import os 
from dotenv import main
import secrets


main.load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "blog.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    SESSION_PROTECTION = os.environ.get("SESSION_PROTECTION")
    FLASK_ADMIN_SWATCH = os.environ.get("FLASK_ADMIN_SWATCH")
    SECURITY_PASSWORD_SALT = secrets.SystemRandom().getrandbits(128)
    SECURITY_REGISTERABLE = os.environ.get("SECURITY_REGISTERABLE")