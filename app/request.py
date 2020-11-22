from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            source_results = process_results(source_results_list)


    return source_results


    def process_results(source_list):
    
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        if url:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results