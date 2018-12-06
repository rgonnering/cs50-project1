# application.py for Project1
# ---------------------------
# a Flask Book Application

# import packages
import os
from flask import render_template, request
from flask import Flask, session
from flask_session import Session
import requests                         # needed for Goodread API
import psycopg2                         # needed to pass variables to postgresql
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# Do this before running search_books.py:
#   $ export DATABASE_URL="postgresql://rwg:sql@localhost:5432/project1"

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# declare global empty lists for users for this Session

signedUpUsers = []			# list of registered users
logedInUsers = []			# list of logged-in users
username = ""				# session username
notes = {}  				# book notes dictionary
							# key : value
							# where value is a list of notes
							# isbn: notes[]


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form.get('email')
    usern = request.form.get('name')
    passw = request.form.get('password')
    email = request.form.get('email')
    # Check is user is already registered
    #userSelection = db.execute("SELECT (username,password,email) FROM registered where username = :user", {"user": usern}).fetchone() 
    result = db.execute("SELECT * FROM registered WHERE username = :u", {"u": usern}).fetchone()
    print("Registration: ", usern, result[1], result.username )
    if result.username == usern:
        msg = "You are already Registered"
        return render_template('form.html', email=email, username=usern, password=passw, msg=msg)
    # New Registration
    result = db.execute("INSERT INTO registered (username, password, email) VALUES (:u, :p, :e)", {"u": usern, "p": passw, "e":email})
    db.commit()
    msg = "Congratulations, you have successfully Registered!"
    return render_template('form.html', email=email, username=usern, password=passw, msg=msg)


@app.route('/login', methods=['POST'])
def login():
    # check if session['username' exists]
    if session.get('username') is None:
        session['username'] = []
    print ("login: session: ", session['username'])
    # # get login credentials
    usern = request.form.get('name')
    passw = request.form.get('password')

    # Check if username is already logged in
    if 'usern' in session:
        msg = "You are logged in."
        return render_template('search.html', username=usern, msg=msg)

    # User is not logged in, so check if user matches a Registered user
    result = db.execute("SELECT * FROM registered where username = :u", {"u": usern}).fetchone()    
    print("Login: ", usern, result[1], result.username )

    if result.username == usern:
        if result.password == passw:
            # login credentials match a registered user
            #session['username'].append(usern) 
            session['username'] = usern
            if usern in session:
                print ("Login session variable: ", usern, session['username'])
            msg = "You have successfully Logged In!."
            return render_template('search.html', username=usern, msg=msg)
    else:
        error_msg = "Please Register"
        return render_template('form.html', msg=error_msg)   


@app.route('/menu', methods=['POST'])
def menu():
    action = request.form.get('action')
    if action == "register":
        return render_template('signup.html')    
    elif action == "login":
        return render_template('login.html')
    elif action == "search":
        return render_template('search.html')
    elif action == "goodread":
        # get Goodread 
        myISBN = "1632168146"
        myKey = "KyNzMuBWuCAOoi42uosr8A"
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbn": myISBN} )

        return render_template('goodread.html', res=res)    
    else:
         return render_template('index.html', msg="Error, Unknown Action Requested")


@app.route('/search', methods=['POST'])
def search():
    username = session['username']
    print ("Search: ", username)
    isbn = request.form.get("isbn")
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")
    username = request.form.get("username")

    # execute SQL command and get all data with user constraintes 
    count = 10
    selections = db.execute("SELECT * FROM books WHERE title LIKE '%"+title+"%' and author LIKE '%"+author+"%' and year LIKE '%"+year+"%' ").fetchall()
    return render_template('list_selections.html', selections=selections, username=username)


@app.route('/book', methods=['POST'])
def book():
    username = session['username']
    print("Book - username: ", username)

    # get book data for id 
    id = request.form.get("select")  
    if id:
        session['book_id'] = id
    else:
        id = session['book_id']
    comment = request.form.get("notefield")
    print("Book Comment: ", username, id, comment)

    # get books data for id
    selection = db.execute("SELECT * FROM books where id = :id", {"id": id}).fetchone()

    # get Goodread Rating
    myISBN = selection[1]
    myKey = "KyNzMuBWuCAOoi42uosr8A"
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbns": myISBN})
    response = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbns": myISBN})
    data = response.json()
    gr_rating = (data['books'][0]['average_rating'])

    print("Book Content: ", id, username, selection.isbn, comment, gr_rating)

    # Add notes, in applicable
    if comment:
        result = db.execute("INSERT INTO bookcomments (username,isbn,mycomment,myreview) \
            VALUES (:u, :isbn, :c, :r)", \
            { "u": username, "isbn": selection.isbn, "c": comment, "r": gr_rating })
        db.commit()    


    # get books data for id
    selection = db.execute("SELECT * FROM books where id = :id", {"id": id}).fetchone()
    # get notes, if avaiable
    bookNotes = db.execute("SELECT * FROM bookcomments where isbn = :isbn", {"isbn": selection.isbn}).fetchall()

    # render book.html
    return render_template('book.html', username=username, selection=selection, notes=bookNotes, rating=gr_rating)
    print("Book Render: ", username, selection)


# logout -------------------------------------------------------
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))








# not needed
@app.route('/goodread', methods=['POST'])
def goodread():
    myISBN = "0316113573"
    myKey = "KyNzMuBWuCAOoi42uosr8A"
    response = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbns": myISBN})
    data = response.json()
    gr_rating = (data['books'][0]['average_rating'])

    return render_template('goodread.html', response=response, rating=gr_rating)
if __name__ == "__main__":
    app.run()
