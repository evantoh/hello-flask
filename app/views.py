from flask import render_template
from app import app

#views
# We import the render_template() function from Flask.
#  This function takes in the name of a template file as the first argument
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home-welcome to the best movie Review website Online'
    return render_template('index.html',title = title)
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    return render_template('movie.html',id = movie_id)