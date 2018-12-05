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

HTTP Response Codes:
--------------------
202 Accepted
The request has been accepted for processing, but the processing has not been completed. The request might or might not be eventually acted upon, and may be disallowed when processing occurs. 
 
422 Unprocessable Entity (WebDAV; RFC 4918)
The request was well-formed but was unable to be followed due to semantic errors   
        print(ares) results in <Response [422]>

================================================
"""

import requests
from flask import render_template, request
myKey = "KyNzMuBWuCAOoi42uosr8A"
myISBN = "9781632168146"

# define the main() function
def main():
    
    print("By isbns")
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbns": "9781632168146"})
    print(res.json())
    print()
    response = res.json()
    print(response)     
    print() 
    print()   
    print("By isbn")
    #res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbn": "1632168146"}) 
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": myKey, "isbns": "1632168146"})
    response = res.json()
    print(response)    
    
    
# run the main() function
if __name__ == "__main__":
    main()