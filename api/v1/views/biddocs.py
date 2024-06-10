#!/usr/bin/python3
""" objects that handles all default RestFul API actions for Amenities"""
from models.biddoc import Biddoc
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/biddocs', methods=['GET'], strict_slashes=False)
@swag_from('documentation/biddoc/all_biddocs.yml')
def get_biddocs():
    """
    Retrieves a list of all biddocs
    """
    all_biddocs = storage.all(Biddoc).values()
    list_biddocs = []
    for biddoc in all_biddocs:
        list_biddocs.append(biddoc.to_dict())
    return jsonify(list_biddocs)


@app_views.route('/biddocs/<biddoc_id>/', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/biddoc/get_biddoc.yml', methods=['GET'])
def get_biddoc(biddoc_id):
    """ Retrieves an biddoc """
    biddoc = storage.get(Biddoc, biddoc_id)
    if not biddoc:
        abort(404)

    return jsonify(biddoc.to_dict())


@app_views.route('/biddocs/<biddoc_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/biddoc/delete_biddoc.yml', methods=['DELETE'])
def delete_biddoc(biddoc_id):
    """
    Deletes an biddoc  Object
    """

    biddoc = storage.get(Biddoc, biddoc_id)

    if not biddoc:
        abort(404)

    storage.delete(biddoc)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/biddocs', methods=['POST'], strict_slashes=False)
@swag_from('documentation/biddoc/post_biddoc.yml', methods=['POST'])
def post_biddoc():
    """
    Creates an biddoc
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Biddoc(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/biddocs/<biddoc_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/biddoc/put_biddoc.yml', methods=['PUT'])
def put_biddoc(biddoc_id):
    """
    Updates an biddoc
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    biddoc = storage.get(Biddoc, biddoc_id)

    if not biddoc:
        abort(404)

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(biddoc, key, value)
    storage.save()
    return make_response(jsonify(biddoc.to_dict()), 200)
