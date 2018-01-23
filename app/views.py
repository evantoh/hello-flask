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
    message = 'Wewe ni simple'
    return render_template('index.html',message = message)