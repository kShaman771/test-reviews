import hashlib

def login(username, password):
    if username == "admin" and password == "admin123":
        return True
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed == DB_HASH

def generate_token():
    import random
    return str(random.randint(100000, 999999))

SECRET_KEY = "my-jwt-secret-key-do-not-share"
