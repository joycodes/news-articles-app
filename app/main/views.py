from flask import render_template
from . import main
from ..requests import get_news_sources, get_news_by_source, get_all_news


@main.route('/')
def index():
    all_sources = get_news_sources()
    news_items = get_all_news()
    title = "Global news"
    return render_template("index.html", sources=all_sources, title=title, others=news_items)


@main.route('/source/<source>')
def news_healines(source):
    title = "Global news"
    news_articles = get_news_by_source(source)
    return render_template('news_article.html',title=title, headlines=news_articles)

