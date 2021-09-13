from flask import Blueprint, jsonify

from src.fuel.service import fuel_prices_json

fuel_api = Blueprint("fuel_controller_api", __name__)


@fuel_api.route('/api/fuel')
def process():
    fuel_json = fuel_prices_json()
    return jsonify(fuel_json)
