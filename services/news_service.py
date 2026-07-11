import feedparser
from datetime import datetime

def get_stock_news(stock, limit=5):
    """
    Fetch latest news headlines for a given stock.
    """

    url = (
        f"https://news.google.com/rss/search?"
        f"q={stock}+stock+India&hl=en-IN&gl=IN&ceid=IN:en"
    )

    feed = feedparser.parse(url)

    news = []

    for entry in feed.entries[:limit]:

        source = "Unknown"

        if hasattr(entry, "source"):
            source = entry.source.title

        published = entry.get("published", "N/A")

        # Optional formatting here

        news.append({
            "title": entry.title,
            "link": entry.link,
            "published": published,
            "source": source
        })

    return news

def format_news_for_ai(news):
    """
    Convert news headlines into a format suitable for Gemini AI.
    """

    if not news:
        return "No recent news available."

    formatted_news = ""

    for i, item in enumerate(news, start=1):
        formatted_news += (
            f"\nNews {i}\n"
            f"Headline : {item['title']}\n"
            f"Source   : {item['source']}\n"
            f"Published: {item['published']}\n"
        )

    return formatted_news