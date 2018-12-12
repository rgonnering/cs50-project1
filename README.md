# Project 1
============
Web Programming with Python and JavaScript
    CS50 Web Programming with Python and JavaScript 
        from Harvard University 
        through edX

The Book Club
=============

git repository
    https://github.com/rgonnering/cs50-project1
    https://github.com/submit50/rgonnering/tree/cs50/web/2018/x/projects/1

youtube walkthrough
    https://youtu.be/JAmmXsViVng


Files
=====
application.py - python program which drives the web site
    Routes
        /           default route which transfers to index.html
        /signup     registration route
        /login      login route
        /menu       Home Menu Page
        /search     Search processing route
        /book       Book processing route
        /goSearch   Transitions user to search.html if logged in,            else go to login
        /logout     Logout route

/templates
    book.html               displays book information and 
                            fetches user comments and ratings
    form.html               displays registration information 
                            and takes uwer to home menu
    index.html              gets what the user wants to do from
                            the main menu
    layout.html             base template
    list_selections.html    list the selections from the search
    login.html              enter login credentials
    menu.html               menu choices
    search.html             enter search criteria
    signup.html             enter registration credentials

/static
    styles.css

Other files
README.md           project summary file
requirements.txt    packages needed for this project

/utilities
    books.csv
    dictionary_list.py
    goodreads.py
    import.py
    list_books.py
    search_books.py
    user_search_books.py


