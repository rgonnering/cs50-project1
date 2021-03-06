# application.py for Project1
# ---------------------------
# a Flask Book Application

# import packages
import os
from flask import render_template, request, redirect, url_for
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
    result = db.execute("SELECT * FROM registered WHERE username = :u", {"u": usern}).fetchone()
    if result:
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
    # get login credentials
    usern = request.form.get('name')
    passw = request.form.get('password')
    print ("login1: ", usern, passw)   
    # Check if username is already logged in
    if 'username' in session:
        msg = "You are already logged in."
        return render_template('search.html', username=usern, msg=msg)
    # User is not logged in, so check if user matches a Registered user
    result = db.execute("SELECT * FROM registered where username = :u", {"u": usern}).fetchone()    
    if result:
        print("Login2: ", usern, result[1], result.username )
        if result.username == usern and result.password == passw:
            # login credentials match a registered user
            #session['username'].append(usern) 
            session['username'] = usern
            if 'username' in session:
                print ("Login2 session variable: ", usern, session['username'])
            msg = "You have successfully Logged In!."
            return render_template('search.html', username=usern, msg=msg)
        else: 
            error_msg = "Username and Password do not match"
            return render_template('login.html', msg=error_msg)            
    else:
        error_msg = "Invalid Credentials. Please Try Again, or Register"
        return render_template('login.html', msg=error_msg)   


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    action = request.form.get('action')
    print("Menu - action: ", action)
    if action == "register":
        return render_template('signup.html')    
    elif action == "login":
        return render_template('login.html')
    elif action == "search":
        if 'username' in session:
             return render_template('search.html')
        else: 
            return render_template('login.html')
    elif action == "goodread":
        # get Goodread 
        myISBN = "1632168146"
        myKey = "KyNzMuBWuCAOoi42uosr8A"
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbn": myISBN} )
        return render_template('goodread.html', res=res)    
    elif action=="logout":
        print("Menu: logout")
        return redirect(url_for('logout'))


@app.route('/search', methods=['POST'])
def search():
    username = session['username']
    isbn = request.form.get("isbn")
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")
    print("Search2: ", session['username'])
    # execute SQL command and get all data with user constraintes 
    selections = db.execute("SELECT * FROM books WHERE isbn LIKE '%"+isbn+"%' and title LIKE '%"+title+"%' and author LIKE '%"+author+"%' and year LIKE '%"+year+"%' ").fetchall()
    # check if book is in the books database
    if not selections:
        return render_template('search.html', username=username, msg="Book is not in the database. Please try again.")
    # book is in database
    return render_template('list_selections.html', selections=selections, username=username)


@app.route('/book', methods=['POST'])
def book():
    username = session['username']
    # get book data for id 
    id = request.form.get("select")  
    print("Book1 ", username, id)  
    if id:
        session['book_id'] = id
    else:
        id = session['book_id']
    comment = request.form.get("notefield")
    rating = request.form.get("action")
    print("Book Comment: ", username, id, comment, rating)
    # get books data for id
    selection = db.execute("SELECT * FROM books where id = :id", {"id": id}).fetchone()
    # get Goodread Rating
    myISBN = selection[1]
    myKey = "KyNzMuBWuCAOoi42uosr8A"# logout -------------------------------------------------------
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbns": myISBN})
    response = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbns": myISBN})
    data = response.json()
    gr_rating = (data['books'][0]['average_rating'])
    print("Book Content: ", id, username, selection.isbn, comment, rating)
    # Add notes, in applicable
    if not rating:
        rating = 3
    if comment:
        result = db.execute("INSERT INTO bookcomments (username,isbn,mycomment,myreview) \
            VALUES (:u, :isbn, :c, :r)", \
            { "u": username, "isbn": selection.isbn, "c": comment, "r": rating })
        db.commit()    
    # get books data for id
    selection = db.execute("SELECT * FROM books where id = :id", {"id": id}).fetchone()
    # get notes, if avaiable
    bookNotes = db.execute("SELECT * FROM bookcomments where isbn = :isbn", {"isbn": selection.isbn}).fetchall()
    # render book.html
    print("Book Render1: ", username, selection)
    print("Book Render2: ", bookNotes, rating)    
    return render_template('book.html', username=username, selection=selection, notes=bookNotes, rating=gr_rating)


# goSearch -------------------------------------------------------
# from book.html, do another search
@app.route('/goSearch', methods=['GET', 'POST'])
def goSearch():
    if 'username' in session:
            return render_template('search.html')
    else: 
        return render_template('login.html')


# logout -------------------------------------------------------
@app.route("/logout")
def logout():
    print("logout")
    #session.pop('username', None)
    if 'username' in session:
        session.pop('username')
    if 'bood_id' in session:
        session.pop('book_id')
    return render_template('login.html')


# main -------------------------------------------------------
if __name__ == "__main__":
    app.run()
