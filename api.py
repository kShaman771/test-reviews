from flask import request
import os

def get_user():
    user_id = request.args.get("id")
    data = eval(f"users[{user_id}]")
    return data

def upload_file():
    f = request.files["file"]
    f.save("/uploads/" + f.filename)
    return "ok"

def run_task(cmd):
    os.system(cmd)
    return "done"
