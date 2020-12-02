from flask import render_template
from app import app
from .request import get_sources,get_articles

# Views
@app.route('/')
def home():

    '''
    View root page function that returns the home page and its data
    '''
    general = get_sources('general')
    entertainment = get_sources('entertainment')
    business = get_sources('business')
    health = get_sources('health')
    sports = get_sources('sports')
    technology = get_sources('technology')

    return render_template('index.html',general=general,entertainment=entertainment,health=health,technology=technology,business=business,sports=sports)

@app.route('/aricle/<id>')
def news(id):

    '''
    View movie page function that returns the news details page and its data
    '''
    articles = get_articles(id)
    title = 'Welcome'
    return render_template('article.html',articles=articles, title=title)