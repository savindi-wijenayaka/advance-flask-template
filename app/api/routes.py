from flask import Blueprint, Response

api = Blueprint('api', __name__)

@api.route("/", methods=["GET"])
def welcome():
    return Response("API for the Website", status=200,  mimetype='application/json')
