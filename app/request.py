from app import app
import urllib.request,json
from .models import source

Source = source.Source

# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]
