#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token , jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Killua": {"username":"Killua", "password": generate_password_hash("password"), "role": "user"},
    "Netero": {"username":"Netero", "password": generate_password_hash("password"), "role": "admin"},

}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user

@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def index():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = request.data.get("username")
    password = request.data.get("password")
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity ="users") 
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid credentials"}), 401
    
if __name__ == "__main__":
    app.run()
