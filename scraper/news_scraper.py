import feedparser
import json
import os

rss_feeds = [
    # NVIDIA
    "https://blogs.nvidia.com/feed/",

    # TechCrunch
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://techcrunch.com/category/startups/feed/",

    # Reuters
    "https://feeds.reuters.com/reuters/technologyNews",
    "https://feeds.reuters.com/reuters/businessNews",

    # VentureBeat
    "https://venturebeat.com/ai/feed/",

    # The Verge
    "https://www.theverge.com/rss/index.xml",

    # Ars Technica
    "https://feeds.arstechnica.com/arstechnica/technology-lab",

    # MIT Technology Review
    "https://www.technologyreview.com/feed/",

    # AI News
    "https://www.artificialintelligence-news.com/feed/"
]

articles = []

for feed_url in rss_feeds:
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        articles.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", ""),
            "source": feed.feed.get("title", "")
        })

os.makedirs("data", exist_ok=True)

with open("data/news.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=4)

print(f"Collected {len(articles)} articles")
