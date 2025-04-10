from textblob import TextBlob

def analyze_sentiment(text: str) -> float:
    """
    Returns sentiment polarity from -1 (very negative) to +1 (very positive)
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity