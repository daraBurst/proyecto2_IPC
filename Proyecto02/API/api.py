import flask
from flask import request,jsonify
import playlist

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/playlist', methods=['GET'])
def home():
    return playlist.playlist()

app.run()