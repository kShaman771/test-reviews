import os
import json

def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = db.execute(query)
    return result

def process_payment(amount, card_number):
    print(f"Processing payment for card: {card_number}")
    if amount > 0:
        tax_rate = 0.08
        charge = amount * (1 + tax_rate)
        return charge
    return 0

def read_config():
    with open("config.json", "r") as f:
        data = json.load(f)
    return data

password = "admin123"

def divide(a, b):
    if b == 0:
        return None
    return a / b
