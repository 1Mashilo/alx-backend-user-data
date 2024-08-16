#!/usr/bin/env python3
"""
Basic Flask application for user authentication service.

This module sets up a Flask web application with a single route
that returns a JSON response.
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    GET route for the root URL.

    Returns:
        A JSON response with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
