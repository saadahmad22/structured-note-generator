from flask import Blueprint, render_template

view =  Blueprint("main", __name__)

@view.route("/")
def home():
    return render_template("home.html")

# receives video
@view.route("/api/home", methods=["POST"])
def receive():
    return {"result": True}