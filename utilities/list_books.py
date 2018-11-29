# list_books.py
# -------------
# list books in books table in project1 database in postgresql.

# get os package
import os

# get functions from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# DATBASE_URL variable
# DATABASE_URL is an environment variable that indicates where the database lives
# Do this before running list_books.py:
#   $ export DATABASE_URL="postgresql://rwg:sql@localhost:5432/project1"
engine = create_engine(os.getenv("DATABASE_URL"))

# create a 'scoped session' that ensures different users' interactions with the
# database are kept separate 
db = scoped_session(sessionmaker(bind=engine))

# define the main() function
def main():
    # execute SQL command and return all of the results for 
    # id, isbn, title, author, and year
    #books = db.execute("SELECT id, isbn, title, author, year FROM books").fetchall()
    books = db.execute("SELECT * FROM books").fetchall()
    # for every flight, print out the flight info
    for book in books:
        print(f"{book.id}, {book.isbn}, {book.title}.")

# run the main() function
if __name__ == "__main__":
    main()