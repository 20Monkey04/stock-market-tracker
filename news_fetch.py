# News Fetch 


# Imports

from newsapi import NewsApiClient
import datetime
import pandas as pd

# API

NEWS_API_KEY = '6f8193dbced943528a4a4ad70afe37b9'
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# =========================================

# Get News

def get_news(ticker):
    
    query = ticker
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    news = newsapi.get_everything(q=query, language='en', sort_by='relevancy', from_param=today)
    
    # Top 5 Relevant Articles Today
    
    articles = news['articles'][:5]  
    news_list = [(a['title'], a['url']) for a in articles]
    
    return news_list