import requests
from bs4 import BeautifulSoup

def get_news_sources():
    # Define a dictionary of news sources with their URLs
    news_sources = {
        'BBC': 'https://www.bbc.co.uk/news',
        'CNN': 'https://edition.cnn.com/world',
        'Al Jazeera': 'https://www.aljazeera.com/',
        'Fox News': 'https://www.foxnews.com/',
        'The New York Times': 'https://www.nytimes.com/',
        # Add more sources as needed
    }
    return news_sources

def get_articles(source_url, keywords):
    # Make a request to the source URL and parse the content with BeautifulSoup
    response = requests.get(source_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant information about news articles based on keywords
    articles = soup.find_all('article')
    relevant_articles = [article.get_text() for article in articles if any(keyword in article.get_text().lower() for keyword in keywords)]

    return relevant_articles

def aggregate_and_report(keywords):
    # Get a list of news sources
    news_sources = get_news_sources()

    # Iterate through each news source and gather relevant news articles
    for source, url in news_sources.items():
        print(f"\nArticles from {source}:")
        _articles = get_articles(url, keywords)

        # Print the headlines or perform any other reporting action
        for i, article in enumerate(_articles, start=1):
            print(f"{i}. {article}")

# Specify keywords for relevance (e.g., 'hamas', 'terror', etc.)
relevant_keywords = ['election']

# Run the aggregation and reporting
aggregate_and_report(relevant_keywords)

