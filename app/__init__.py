from flask import Flask
from .extensions import db, migrate

def create_app(config_object='app.config.DevelopmentConfig'):
  app = Flask(__name__, instance_relative_config=False)
  app.config.from_object(config_object)

  # Initialize extensions
  db.init_app(app)
  migrate.init_app(app, db)

  # Register blueprints
  from .views import main_bp
  app.register_blueprint(main_bp)

  return app

