import flask
from flask_cors import cross_origin
from flask import Blueprint, jsonify, Response, request
from ..db import queries
blueprint = Blueprint("images", __name__, url_prefix='/api/images')

@blueprint.route("/")
@cross_origin()
def specifyRoutes():
    return jsonify({'Useable Routes':'images/random, images/<insertID>'})

@blueprint.route("/random")
@cross_origin()
def randomImage():
    platform = request.args.get("src","reddit")
    limit = (int)(request.args.get("limit",1))
    if platform.lower() == "twitter":
        print("here")
        return '<html><h1>Under construction</h1></html>'
    else:
        rclass = queries.Reddit()
        post = rclass.getRandom(limit=limit)
        return jsonify(post)
        