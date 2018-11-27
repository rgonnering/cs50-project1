# search_books.py
# ---------------
# list books in books table in project1 database where title contains 'irl'

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
    # execute SQL command, get all data constrained by having 'irl' in the title
    #selections = db.execute("SELECT * FROM books WHERE title LIKE '%irl%' ").fetchall()
    
    myString = 'irl'    
    # execute SQL command, get all data constrained by having 
    # myString in the title and ascending order by year
    selections = db.execute("SELECT * FROM books WHERE title LIKE '%"+myString+"%' order by year asc").fetchall()

    # for every selection that has string in the title, print all data
    for book in selections:
        print(f"{book.id}, {book.isbn}, {book.title}, {book.author}, {book.year}.")

# run the main() function
if __name__ == "__main__":
    main()
