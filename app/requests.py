import urllib.request,json
from .models import Sources, News

# Keys
api_key = None
sources_url = None
everything_news_url = None



def configure_request(app):
    global api_key, sources_url, everything_news_url, top_headlines_news_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_API_URL']
    everything_news_url = app.config['EVERYTHING_BASE_API_URL']
    top_headlines_news_url = app.config['TOP_HEADLINES_BASE_API_URL']


def get_news_sources():

    complete_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(complete_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        sources_results = None
        if sources_response['sources']:
            '''
            eliminates empty sources
            '''
            sources_items = sources_response['sources']
            sources_results = process_news_sources(sources_items)

    return sources_results


def process_news_sources(sources_list):
    sources_processed_results = []
    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        url = item.get('url')
        country = item.get('country')
        description = item.get('description')
        new_source = Sources(id, name, url, country, description)
        sources_processed_results.append(new_source)

    return sources_processed_results


def get_news_by_source(source):
    articles_url = top_headlines_news_url.format(source, api_key)

    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        articles_results = None
        if articles_response['articles']:
            article_items = articles_response['articles']
            articles_results = process_news(article_items)

    return articles_results


def process_news(headlines_list):
    processed_results = []
    for item in headlines_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        news_headlines = News(
            author, title, description, url, urlToImage, publishedAt)
        processed_results.append(news_headlines)

    return processed_results


def get_all_news():
    all_news_url = everything_news_url.format(api_key)

    with urllib.request.urlopen(all_news_url) as url:
        all_data = url.read()
        all_response = json.loads(all_data)
        all_results = None

        if all_response['articles']:
            all_results_list = all_response['articles']
            all_results = process_news(
                all_results_list)

    return all_results


