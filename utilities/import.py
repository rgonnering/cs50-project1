# import.py
# import books.csv into postresql

import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    # open the flights.csv file
    f = open("books.csv")
    
    # use the python csv.reader function to read the flights.csv data
    # to create a list called reader
    reader = csv.reader(f)
    
    # loop through each row the reader list and get the datafields 
    # isbn,	title,	author,	year
    for isbn, title, author, year in reader:
        # execute an insertion into the database
        # :isbn, :title, :author, :year are placeholders for the datafields
        # {"isbn": isbn, "title": title, "author": author, "year": year}
        # {"origin": orig, "destination": dest, "duration": dur}
        #   is a python dictionary that tells the database what datafields
        #   in the database to put in the placeholder data.
        #   "origin" is database field, orig is placeholder data from csv
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
            {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Added book isbn: {isbn}, title {title}, author {author}, year {year}.")
        
    # save the new data to the database
    db.commit()

if __name__ == "__main__":
    main()