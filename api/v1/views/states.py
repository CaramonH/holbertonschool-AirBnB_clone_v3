#!/usr/bin/python3
"""
Create a new view for State objects
that handles all default RESTFul API actions
"""

from flask import Blueprint, request, jsonify
from models.state import State

states_bp = Blueprint('states', __name__)


@states_bp.route('/api/v1/states', methods=['GET'])
def get_states():
    """Retrieves the list of all State objects."""
    states = State.query.all()
    return jsonify([state.to_dict() for state in states])


@states_bp.route('/api/v1/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Retrieves a State object."""
    state = State.query.get(state_id)
    if not state:
        raise ValueError('State not found')
    return jsonify(state.to_dict())


@states_bp.route('/api/v1/states', methods=['POST'])
def create_state():
    """Creates a State."""
    data = request.get_json()
    if not data:
        raise ValueError('Not a JSON')
    if 'name' not in data:
        raise ValueError('Missing name')
    state = State(name=data['name'])
    state.save()
    return jsonify(state.to_dict()), 201


@states_bp.route('/api/v1/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates a State object."""
    state = State.query.get(state_id)
    if not state:
        raise ValueError('State not found')
    data = request.get_json()
    if not data:
        raise ValueError('Not a JSON')
    for key, value in data.items():
        if key in ['id', 'created_at', 'updated_at']:
            continue
    setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200


@states_bp.route('/api/v1/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State object."""
    state = State.query.get(state_id)
    if not state:
        raise ValueError('State not found')
    state.delete()
    return jsonify({'message': 'State deleted'}), 200
