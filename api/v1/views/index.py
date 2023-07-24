#!/usr/bin/python3
"""
Retrieves the number of each objects by type
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})


@app_views.rout('/stats')
def class_stats():
    """Return 'count' of class instances"""
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
