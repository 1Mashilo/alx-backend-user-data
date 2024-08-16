#!/usr/bin/env python3
"""
A simple Flask app with user authentication features.

This module defines a basic Flask application that includes
routes for welcoming users and registering new users.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from auth import Auth

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    GET / - Root endpoint

    Returns:
        str: JSON response with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    POST /users - Register a new user

    Expects:
        - email (str): The user's email address.
        - password (str): The user's password.

    Returns:
        str: JSON response with the account creation message
        or an error message if the email is already registered.
    """
    email, password = request.form.get("email"), request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
