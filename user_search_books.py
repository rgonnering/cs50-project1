# user_search_books.py
# --------------------
# list books in books table in project1 database where title contains 'irl'
"""
    Example:
        Enter anything you might know about the book
        Just his 'Enter' to skip any field you don't know anything about
        title: irl
        author: ian
        year: 2012
            3264, 0297859382, Gone Girl, Gillian Flynn, 2012.
            4272, 0385534795, The Sandcastle Girls, Chris Bohjalian, 2012.
"""

# get os package
import os

# get functions from sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# DATBASE_URL variable
# DATABASE_URL is an environment variable that indicates where the database lives
# Do this before running search_books.py:
#   $ export DATABASE_URL="postgresql://rwg:sql@localhost:5432/project1"
engine = create_engine(os.getenv("DATABASE_URL"))

# create a 'scoped session' that ensures different users' interactions with the
# database are kept separate 
db = scoped_session(sessionmaker(bind=engine))

# define the main() function
def main():
    title = ''
    author = ''
    year = ''
    
    # Menu
    print("Enter anything you might know about the book.")
    print("Just his 'Enter' to skip any field you don't know anything about.")
    title = input("title: ")
    author = input("author: ")
    year = input("year: ")

    # execute SQL command and get all data with user constraintes 
    selections = db.execute("SELECT * FROM books WHERE title LIKE '%"+title+"%' and author LIKE '%"+author+"%' and year LIKE '%"+year+"%' ").fetchall()
    # for every selection that has string in the title, print all data
    for book in selections:
        print(f"{book.id}, {book.isbn}, {book.title}, {book.author}, {book.year}.")

# run the main() function
if __name__ == "__main__":
    main()