from src.fuel.parser import parse_fuel


def fuel_prices_json():
    ai92, ai95, ai98, gas, dt = parse_fuel()

    return [
        {
            "id": 0,
            "name": "AI-92",
            "price": float(ai92)
        },
        {
            "id": 1,
            "name": "AI-95",
            "price": float(ai95)
        },
        {
            "id": 2,
            "name": "AI-98",
            "price": float(ai98)
        },
        {
            "id": 3,
            "name": "GAS",
            "price": float(gas)
        },
        {
            "id": 4,
            "name": "DT",
            "price": float(dt)
        }
    ]
