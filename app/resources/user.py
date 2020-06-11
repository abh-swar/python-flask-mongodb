# User resource

from app.db.config import client
from application import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
from app.utils.query_util import parse_query_params
from app.services import user_service

@app.route("/",  methods=['GET'])
def welcome():
    """REST API using Python, Flask and MongoDB"""
    
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'REST API using Python, Flask and MongoDB'
    }
    return jsonify(message)


@app.route("/api/v1/user", methods=['POST'])
def create_user():
    """
       Endpoint to create new users.
    """
    try:
        try:
            body = request.get_json()
        except Exception:
            return "Error parsing JSON", 400

        new_records = user_service.create(body)

        # Return a list of ids of all the newly created users
        if isinstance(new_records, list):
            return jsonify([str(v) for v in new_records]), 201
        else:
            return jsonify(str(new_records)), 201
    except Exception:
        # Handle Error while trying to create the resource
        return "Error while trying to create the resource", 500


@app.route("/api/v1/user", methods=['GET'])
def get_users():
    """
       Endpoint to get all the users
    """
    try:
        if user_service.count() > 0:
            return dumps(user_service.get())
        else:
            return jsonify([])
    except Exception:
        # Handle error when trying to fetch the resource
        return "Error reading from the database", 500


@app.route("/api/v1/user/<user_id>", methods=['PUT'])
def update_user(user_id):
    """
       Function to update the user.
    """
    try:
        try:
            body = request.get_json()
        except Exception:
            return "Error parsing JSON", 400

        # Updating the user by id
        user_service.update(user_id, body)

        return "Successfully updated the user", 200
    except Exception:
        return "Error occurred while updating the user", 500


@app.route("/api/v1/user/<user_id>", methods=['DELETE'])
def remove_user(user_id):
    """
       Function to remove the user.
    """
    try:
        # Delete the user by id
        user_service.delete(user_id)
        return "Successfully deleted the user", 200
    except Exception:
        return "Error occurred while deleting the user", 500