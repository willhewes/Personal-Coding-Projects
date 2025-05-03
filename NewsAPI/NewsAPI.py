import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('NEWS_API_KEY')
endpoint = 'https://newsapi.org/v2/everything'

# Calculate the date from 3 days ago
three_days_ago = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')

# Parameters dictionary
parameters = {
    'q': input("Topic : "), # Select relevant topic
    'from': three_days_ago, # Select date for search
    'sortBy': 'relevance',
    'apiKey': API_KEY,
    'language': 'en'
}

response = requests.get(endpoint, params=parameters)

if response.status_code == 200:
    data = response.json()
    articles = data['articles'][:5]  # Limit to the top 5 articles
    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Description: {article['description']}")
        print(f"   URL: {article['url']}\n")
else:
    print("Failed to fetch news articles")
