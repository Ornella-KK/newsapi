from app import app
import urllib.request,json
from .models import source,article
News_Source=source.News_Source
News_Article=article.News_Article

# Getting api key
api_key = app.config['SOURCE_API_KEY']


#Getting the movie base url
base_url=app.config['SOURCE_API_BASE_URL']
article_url=app.config['ARTICLE_API_BASE_URL']

def get_sources(category):
    
    #Function that gets json response to our url request
    
    get_sources_url = base_url.format(category,api_key)
    print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_sources(sources_list):
    '''
    function that processes the news results and transform them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain news details
    Returns:
        sources_results: Alist of news source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        url = sources_item.get('url')
        category = sources_item.get('category')


        if id:
            sources_object = News_Source(id,name,url,category)

            sources_results.append(sources_object)
    return sources_results

def get_articles(id):
    
    #Function that gets the json response to url request
    
    get_article_news_url = article_url.format(id,api_key)
    with urllib.request.urlopen(get_article_news_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

def process_articles(articles_list):
    
    #process the dictionary and output a list of objects
    
    article_results = []
    source_dictionary = {}
    for result in articles_list:
        source_id = result ['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']
        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt=result.get('publishedAt')
        if urlToImage:
            print (id)
            article_object = News_Article(id,name,author,title,description,url,urlToImage,publishedAt)

            article_results.append(article_object)

    return article_results
