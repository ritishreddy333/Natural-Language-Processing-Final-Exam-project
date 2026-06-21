import json
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load cleaned data
with open("data/clean_news.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

texts = []

for article in articles:
    text = article["title"] + " " + article["summary"]
    texts.append(text)

# Generate embeddings
embeddings = model.encode(texts)

print("Number of embeddings:", len(embeddings))
print("Embedding dimension:", len(embeddings[0]))