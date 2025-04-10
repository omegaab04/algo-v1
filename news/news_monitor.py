from news.news_fetcher import fetch_trump_news
from news.analyse_sentiment import analyse_sentiment  
from utils.logger import log

KEYWORDS = ["tariff", "tariffs", "trade war", "china", "import tax", "duties"]

def is_all_caps_alert(text: str, threshold: float = 0.7) -> bool:
    words = text.split()
    if not words:
        return False
    upper_words = [w for w in words if w.isupper()]
    return (len(upper_words) / len(words)) >= threshold

def monitor_trump_news(trigger_threshold=-0.5, display=True) -> bool:
    """
    Fetches Trump news and returns True if:
      - sentiment is negative
      - or keywords like "tariff" are found
      - or the headline is mostly ALL CAPS
    """
    headlines = fetch_trump_news(limit=5)
    override = False

    if display:
        log("News Flash — Donald Trump Headlines:")

    for article in headlines:
        title = article["title"]
        lower_title = title.lower()
        sentiment = analyse_sentiment(title)
        keyword_hit = any(kw in lower_title for kw in KEYWORDS)
        caps_alert = is_all_caps_alert(title)

        if display:
            log(f"\nHeadline: {title}")
            log(f"URL: {article['url']}")
            log(f"Time: {article['time']}")
            log(f"Sentiment Score: {sentiment:.2f}")
            if keyword_hit:
                log("Keyword alert: Tariff-related term detected.")
            if caps_alert:
                log("CAPS ALERT: Headline contains intense capitalization.")

        if sentiment <= trigger_threshold or keyword_hit or caps_alert:
            override = True

    if override:
        log("🚨 News-triggered override activated.")
    return override