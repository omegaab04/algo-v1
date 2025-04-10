import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_trump_news(limit=5):
    """
    Fetches recent news headlines related to Donald Trump.

    Args:
        limit (int): Number of articles to fetch (default 5)

    Returns:
        List[dict]: List of articles with title, url, and time
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "Donald Trump",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": limit,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get("articles", [])

        headlines = []
        for article in articles:
            headlines.append({
                "title": article["title"],
                "url": article["url"],
                "time": article["publishedAt"]
            })

        return headlines

    except Exception as e:
        print(f"❌ News fetch failed: {e}")
        return []