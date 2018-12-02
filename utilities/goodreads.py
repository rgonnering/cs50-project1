#  goodreads.py
# -------------
"""
        https://www.goodreads.com/
            Roger
            gmail
            D1
API Key
    key: KyNzMuBWuCAOoi42uosr8A
    secret: c7thhZl0ePa46vcCZG6FBm2OnmFlygIyxsBoP3b1VQ
    
Sample Code: to give you the review and rating data for the book with the provided ISBN number.
    import requests
    #res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": "9781632168146"})
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbn": "1632168146"})    
    print(res.json())

Result of request:
        {
            'books': [{
                'id': 29207858, 
                'isbn': '1632168146', 
                'isbn13': '9781632168146', 
                'ratings_count': 0, 
                'reviews_count': 2, 
                'text_reviews_count': 0, 
                'work_ratings_count': 26, 
                'work_reviews_count': 118, 
                'work_text_reviews_count': 10, 
                'average_rating': '4.04'
            }]
        }
"""

import requests
from flask import render_template, request
myKey = "KyNzMuBWuCAOoi42uosr8A"
myISBN = "9781632168146"

# define the main() function
def main():
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbns": "9781632168146"})
    print(res.json())

# run the main() function
if __name__ == "__main__":
    main()