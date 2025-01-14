from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app(config_filename="config.py"):
  app = Flask(__name__)

  app.config.from_pyfile(config_filename)

  db.init_app(app)
  csrf.init_app(app)

  from app.routes import main
  app.register_blueprint(main)

  return app
