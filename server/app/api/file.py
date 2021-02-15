import flask
from flask_cors import cross_origin
from flask import Blueprint, jsonify, Response, request, send_file, redirect, make_response
from dotenv import load_dotenv
from ..util import storage, settings
from ..db import queries
from . import api
import os
load_dotenv()

blueprint = Blueprint("file", __name__, url_prefix='/api/file')

@blueprint.route("/<filename>")
@cross_origin()
def getFile(filename):
    file = queries.getByFile(filename)
    if not file: 
        return api.FILE_NOT_FOUND
    try:
        return storage.getImage(file)
    except FileNotFoundError:
        return api.FILE_NOT_FOUND
