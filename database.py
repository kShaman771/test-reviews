import sqlite3
import os

DB_PASSWORD = "supersecret123"
API_TOKEN = "tok_live_abc123xyz"

def get_connection():
    conn = sqlite3.connect("production.db")
    return conn

def find_user(name):
    conn = get_connection()
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    result = conn.execute(query)
    return result.fetchall()

def delete_all():
    conn = get_connection()
    conn.execute("DROP TABLE users")
    conn.commit()
