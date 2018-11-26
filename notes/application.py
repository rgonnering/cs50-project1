# Flask application from application.py in notes folder
# Present the user with a form to fetch some data and then
# Display all messages that were entered.

# import Flask from flask
# also import render_template, request, and session modules
#   session lets us keep variable that are specific to a user
from flask import Flask, render_template, request, session

# import Session from flask_session
# Session lets us store data about the session on the server.
#   It will make any global variables in this session only applicable to me.
# If flask_session is not loaded, $ pip install Flask-Session
from flask_session import Session

# instantiate app
app = Flask(__name__)

# Configure the app object
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Session is a collection of data specific to me
Session(app)


"""
# declare a global empty list for notes for this Session
notes = []


# default route for GET and POST request methods
@app.route("/", methods=["GET", "POST"])
def index():
    # for a POST request
    if request.method == "POST":
        # get a new note from the form datafield "note"
        note = request.form.get("note")
        # append the new note to the list of notes
        notes.append(note)

    #whether there was a POST or GET request
    # render index.html and pass the list of notes
    return render_template("index.html", notes=notes)
"""


# To make the global list of notes unique to me
# default route for GET and POST request methods
@app.route("/", methods=["GET", "POST"])
def index():
    # make notes a list in my unique session
    # if "notes doesn't exist, create it.
    if session.get("notes") is None:
        session["notes"] = []
    # for a POST request
    if request.method == "POST":
        # get a new note from the form datafield "note"
        note = request.form.get("notefield")
        # append the new note to the list of session notes
        session["notes"].append(note)

    #whether there was a POST or GET request
    # render index.html and pass the list of notes
    return render_template("index.html", notes=session["notes"])
    