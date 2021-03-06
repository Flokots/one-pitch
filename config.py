import os

class Config:
  '''
  General configuration parent class
  '''
  SECRET_KEY=os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://flo:flo@localhost:5433/one_pitch'
  UPLOADED_PHOTOS_DEST='app/static/photos'

   # email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
    Config: The parent configuration class with General configuration settings.
  '''
  
  SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_GRAY_URL").replace("://", "ql://", 1)

class DevConfig(Config):
  '''
  Development configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''

  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://flo:flo@localhost:5433/one_pitch'
  

DEBUG=True

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://flo:flo@localhost:5433/one_pitch_test'


config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'test': TestConfig
}