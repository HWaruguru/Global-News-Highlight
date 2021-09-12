import requests
from app import app
import urllib.request,json
from .models import news

Source = news.Source
Article = news.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    sources_url = f'{base_url}top-headlines/sources?apiKey={api_key}'

    res = requests.get(sources_url)
    sources_data = res.json().get('sources')
    return sources_data


def get_articles():
    '''
    Function that gets the json response to our url request
    '''
    articles_url = f'{base_url}everything?domains=techcrunch.com,thenextweb.com&pageSize=100&apiKey={api_key}'

    res = requests.get(articles_url)
    articles_data = res.json().get('articles')
    return articles_data
