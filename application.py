import os

# from notes
from flask import render_template, request

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=enginfrom flask import Flask e))

@app.route("/")
def index():
	return render_template("index.html")



# Make the /login route work with POST.
@app.route("/login", methods=["POST"])
def login():
	name = request.form.get("name")
	password = request.form.get("password")
	return render_template("login.html", name=name, password=password)

# Make the /login route work with POST.
@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name")
	password = request.form.get("password")
	return render_template("register.html", name=name, password=password)

