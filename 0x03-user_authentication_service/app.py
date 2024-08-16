#!/usr/bin/env python3
"""
Basic Flask application for user authentication service.

This module sets up a Flask web application with routes for
registering users and returning JSON responses.
"""

from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/", methods=["GET"])
def index():
    """
    GET route for the root URL.

    Returns:
        A JSON response with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def users():
    """
    POST route to register a new user.

    Expects form data fields: 'email' and 'password'.
    
    Returns:
        A JSON response with a success message if the user is created,
        or an error message if the email is already registered.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, description="Missing email or password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
