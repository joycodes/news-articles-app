import os


class Config:
  
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SOURCES_BASE_API_URL = "https://newsapi.org/v2/sources?apiKey={}"
    EVERYTHING_BASE_API_URL = "https://newsapi.org/v2/everything?domains=wsj.com&apikey={}"
    TOP_HEADLINES_BASE_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

class ProdConfig(Config):

    pass


class DevConfig(Config):
    # To enable debug mode.
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
