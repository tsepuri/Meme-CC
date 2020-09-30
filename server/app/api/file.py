import flask
from flask_cors import cross_origin
from flask import Blueprint, jsonify, Response, request, send_file
from dotenv import load_dotenv
from ..util import storage
from ..db import queries
load_dotenv()

blueprint = Blueprint("file", __name__, url_prefix='/api/file')

@blueprint.route("/<filename>")
@cross_origin()
def getFile(filename):
    r_db = queries.Reddit()
    file = r_db.getFile(filename)
    if not file: 
        return jsonify({'Error': 'File does not exist'},status=404)
    try:
        image = storage.getImage(filename)
    except FileNotFoundError:
        return jsonify({'Error': 'File does not exist'},status=404)
    return send_file(image)
