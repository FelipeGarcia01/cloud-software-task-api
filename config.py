from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    STATIC_FOLDER = "views/static/"
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY", "")
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + \
                              os.environ.get('PGSQL_USER') + ':' + \
                              os.environ.get('PGSQL_PASSWORD') + '@' + \
                              os.environ.get('PGSQL_HOST') + ':' + \
                              os.environ.get('PGSQL_PORT') + '/' + \
                              os.environ.get('PGSQL_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    ACCESS_EXPIRES = timedelta(hours=2)
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
