import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  GOOGLE_MAPS_KEY = environ["GOOGLE_MAPS_KEY"]

  SQLACHEMY_DATABASE_UI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
  MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
  MAIL_PORT = os.environ.get('MAIL_PORT') or 587
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class DevelopmentConfig(Config):
  DEBUG = True

class ProductionConfig(Config):
  DEBUG = False

class TestingConfig(Config):
  DEBUG = False
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # Temporary memory database only

