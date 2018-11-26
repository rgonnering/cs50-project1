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
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"



"""    
@app.route("/", methods=["POST"])
def index():
    # for a POST request
    if request.method == "POST":
        # get a new note from the form datafield "note"
        note = request.form.get("note")
        # append the new note to the list of notes
        notes.append(note)

    return render_template("index.html", notes=notes)
"""



"""   
 First of all you have to import it from the flask module:
	from flask import request

* The current request method is available by using the method attribute. To access form data (data transmitted in a POST or PUT request) you can use the form attribute. Here is a full example of the two attributes mentioned above:

	@app.route('/login', methods=['POST', 'GET'])
	def login():
		error = None
		if request.method == 'POST':
			if valid_login(request.form['username'],
						   request.form['password']):
				return log_the_user_in(request.form['username'])
			else:
				error = 'Invalid username/password'
		# the code below is executed if the request method
		# was GET or the credentials were invalid
		return render_template('login.html', error=error)

To access parameters submitted in the URL (?key=value) you can use the args attribute:
	searchword = request.args.get('key', '')   
"""



"""    
   * To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function:

	from flask import abort, redirect, url_for

	@app.route('/')
	def index():
		return redirect(url_for('login'))

	@app.route('/login')
	def login():
		abort(401)
		this_is_never_executed()
"""		 
    
    
    
 """	   
      <body>
        <form>
            <div>
                <input name="name" type="text" placeholder="Name">
                <input name="password" type="password" placeholder="Password">
            </div>  
        </form>
    </body>    
 """    
    
    
    
    
    
    
    
    