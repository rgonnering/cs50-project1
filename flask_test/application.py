# <!-- flask_test -->

# get os package
import os

# get flask functions
from flask import Flask, request, url_for, render_template, session
from flask_session import Session

# get functions from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# Do this before running search_books.py:
#   $ export DATABASE_URL="postgresql://rwg:sql@localhost:5432/project1"
engine = create_engine(os.getenv("DATABASE_URL"))
# create a 'scoped session' that ensures different users' interactions with the
# database are kept separate 
db = scoped_session(sessionmaker(bind=engine))

# instantiate app
app = Flask(__name__)

# Configure the app object
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Session is a collection of data specific to me
Session(app)

# declare a global empty list for users for this Session
signedUpUsers = []
logedInUsers = []

@app.route("/")
def index():
    # return "Index"
    msg = ""
    email='roger.gonnering.us'
    return render_template('index.html', email=email, msg=msg)


@app.route('/signup', methods = ['POST'])
def signup():
    global signedUpUsers
    email = request.form.get('email')
    username = request.form.get('name')
    password = request.form.get('password')
    signedUpUsers.append([username, password, email])
    return render_template('form.html', email=email, username=username, password=password, signedUpUsers = signedUpUsers)


@app.route('/login', methods=['POST'])
def login():
    global signedUpUsers
    global logedInUsers
    # get login credentials
    username = request.form.get('name')
    password = request.form.get('password')
    
    # check if username exits
    for user in signedUpUsers:
        if user[0] == username:
            if user[1] == password:
                logedInUsers.append([username, password])
                return render_template('search.html', username=username)
    error_msg = "Please Register"
    return render_template('search.html', username=error_msg)   


@app.route('/menu', methods=['POST'])
def menu():
    action = request.form.get('action')

    if action == "register":
        return render_template('signup.html')    
    elif action == "login":
        return render_template('login.html')
    elif action == "search":
        return render_template('search.html')
    else:
         return render_template('index.html', msg="Error, Unknown Action Requested")


@app.route('/search', methods=['POST'])
def search():
    isbn = request.form.get("isbn")
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")

    # execute SQL command and get all data with user constraintes 
    selections = db.execute("SELECT * FROM books WHERE title LIKE '%"+title+"%' and author LIKE '%"+author+"%' and year LIKE '%"+year+"%' ").fetchall()
    #selections = db.execute("SELECT * FROM books WHERE title='I, Robot' ").fetchall()

    return render_template('list_selections.html', selections=selections)


if __name__ == "__main__":
    app.run()