from flask import render_template
from app import app
from .request import get_articles, get_articles_from_source, get_sources

# Views
@app.route("/")
def index():

    """
    View root page function that returns the index page and its data
    """
    sources = get_sources()
    articles = get_articles()   
    return render_template("index.html", sources=sources, articles=articles)

@app.route('/articles/<string:source_id>')
def articles(source_id):

    """
    View articles page function that returns the articles page and its data
    """
    sources = get_sources()
    articles = get_articles_from_source(source_id)   
    return render_template("articles.html", sources=sources, articles=articles)
