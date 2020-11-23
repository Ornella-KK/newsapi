from app import app
from flask import render_template
from .request import get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    source = get_source()
    print(source)
    title = 'Home - Articles'
    return render_template('index.html', title = title,sources = source)