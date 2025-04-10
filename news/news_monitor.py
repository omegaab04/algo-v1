from news.news_fetcher import fetch_trump_news
from news.sentiment_analyser import analyze_sentiment
from utils.logger import log

def monitor_trump_news(trigger_threshold=-0.5, display=True) -> bool:
    """
    Fetches Trump news and returns True if any headline is negative enough.

    Args:
        trigger_threshold (float): Polarity value to consider "too negative"
        display (bool): If True, prints headlines + sentiment

    Returns:
        bool: True if override should be triggered
    """
    headlines = fetch_trump_news(limit=5)
    override = False

    if display:
        log("📰 News Flash — Donald Trump Headlines:")

    for article in headlines:
        sentiment = analyze_sentiment(article['title'])

        if display:
            log(f"\n🗞️ {article['title']}")
            log(f"🔗 {article['url']}")
            log(f"📅 {article['time']}")
            log(f"🧠 Sentiment Score: {sentiment:.2f}")

        if sentiment <= trigger_threshold:
            override = True

    if override:
        log(f"🚨 News-triggered override (sentiment ≤ {trigger_threshold})")

    return override