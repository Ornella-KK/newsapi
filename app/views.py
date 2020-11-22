from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_sources = get_sources('popular')
    print(popular_sources)
    title = 'Home - Articles'
    return render_template('index.html', title = title,popular = popular_sources)