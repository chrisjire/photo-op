from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import configure_uploads,UploadSet,IMAGES
from flask_mail import Mail

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import ProdConfig,Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login' 
photos = UploadSet('photos',IMAGES)
mail = Mail(app)


def create_app():
  app.config.from_object(Config)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  # configure_uploads(app,photos)
  mail.init_app(app)

  return app
