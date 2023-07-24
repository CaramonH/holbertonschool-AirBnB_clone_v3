#!/usr/bin/python3
"""
This module contains the index for the RESTful API
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """Returns OK status"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def class_stats():
    """ return counts of class instances """
    counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(counts)
