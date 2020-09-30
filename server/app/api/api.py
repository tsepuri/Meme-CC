import flask
from flask import Blueprint, render_template
from flask_cors import CORS
from . import images, file
app = flask.Flask(__name__, static_folder="../../dist/static", template_folder="../../dist")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"]
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
app.register_blueprint(images.blueprint)
app.register_blueprint(file.blueprint)
app.run(host="localhost",port=5000)
