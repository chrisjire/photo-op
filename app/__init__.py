from flask_bootstrap import Bootstrap
from flask_login import LoginManager


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


def create_app():
  app.config.from_object(Config)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  

  return app
