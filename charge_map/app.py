from flask import Flask
from charge_map.settings import ProdConfig
from charge_map.extentions import db, migrate
from charge_map.urls import api


def create_app(config_obj=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    return app

