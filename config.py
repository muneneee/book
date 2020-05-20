import os

class Config:
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234'
    UPLOADED_PHOTOS_DEST ='app/static'


    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):

    DEBUG = True



Config_options = {
    'development':DevConfig,
    'production':ProdConfig
}