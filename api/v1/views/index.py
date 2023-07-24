#!/usr/bin/python3
"""
This module contains the index for the RESTful API
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API."""
    status_code = 200
    status_message = "OK"
    return jsonify({
      "status_code": status_code,
      "status_message": status_message
    })


@app_views.route('/stats')
def class_stats():
    """ return counts of class instances """
    from models import storage
    counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(counts)
