books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

'''
import flask
from flask import request, jsonify
import playlist, books

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/playlist', methods=['GET'])
def playlisthome():
    return playlist.playlist()

@app.route('/books/all', methods=['GET'])
def bookshome():
    return jsonify(books.books)

@app.route('/books', methods=['GET'])
def book_id(): 
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it it to a variable.
    # If no ID is provided, display an error in the browser
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    #Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the request ID.
    # IDs are unique, but other fields might return many results
    for book in books.books:
        if book['id'] == id:
            results.append(book)
    
    # Use the jsonify function form Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
'''