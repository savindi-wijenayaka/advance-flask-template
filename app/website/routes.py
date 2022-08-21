from flask import Blueprint, render_template

website = Blueprint('website', __name__, static_folder="static", template_folder="templates")

@website.route("/", methods=["GET"])
def welcome():
    return render_template("index.html")
