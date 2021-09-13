from flask import Flask

from src.fuel.controller import fuel_api


def create_app() -> Flask:
    app = Flask("FuelAPI")

    app.register_blueprint(fuel_api)

    return app
