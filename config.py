import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static'


    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dolphine:dolphine@localhost/book'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    pass


class DevConfig(Config):

    DEBUG = True



Config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
