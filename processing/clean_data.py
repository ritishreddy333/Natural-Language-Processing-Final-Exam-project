import json

with open("data/news.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

seen_titles = set()
clean_articles = []

for article in articles:

    title = article["title"].strip()

    if title not in seen_titles:

        seen_titles.add(title)

        clean_articles.append(article)

with open("data/clean_news.json", "w", encoding="utf-8") as f:
    json.dump(clean_articles, f, indent=4)

print(f"Original: {len(articles)}")
print(f"After Cleaning: {len(clean_articles)}")