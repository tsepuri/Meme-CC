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
    platform = request.args.get("src","all")
    limit = (int)(request.args.get("limit",1))
    if platform.lower() == "?":
        return '<html><h1>Under construction</h1></html>'
    else:
        smclass = queries.SocialMedia()
        post = smclass.getRandom(limit=limit)
        return jsonify(post)

@blueprint.route("/search/<searched>")
@cross_origin()
def searchImage(searched):
    #templateclass = queries.Templates()
    post = queries.getBySearch(searched)
    return jsonify(post)
        