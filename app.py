import os
import sys
import json
import random
import time

def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    result = db.execute(query)
    return result

def process_payment(amount, card_number):
    print("Processing payment for card: " + card_number)
    if amount > 0:
        charge = amount * 1.0
        return charge

def read_config():
    f = open("config.json", "r")
    data = json.load(f)
    return data

password = "admin123"
API_KEY = "sk-1234567890abcdef"

def divide(a, b):
    return a / b
