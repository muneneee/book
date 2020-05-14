from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE

bootstrap = Bootstrap()
#db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
from flask_sqlalchemy import SQLAlchemy
from config import Config,Config_options
from flask_bootstrap import Bootstrap

db  = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_object(Config_options[config_name])

    # Creating the app configurations
    app.config.from_object(Config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    #db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)

    return app
