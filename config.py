import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or os.urandom(32)
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    S3_BUCKET = os.environ.get("S3_BUCKET")
    S3_KEY = os.environ.get("S3_KEY")
    S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
    S3_LOCATION = 'http://next-clone-instagram.s3.amazonaws.com/'

class ProductionConfig(Config):
    DEBUG = False
    ASSETS_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ASSETS_DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ASSETS_DEBUG = True
