import json
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load cleaned articles
with open("data/clean_news.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

# Create Chroma client
client = chromadb.PersistentClient(path="vectordb/chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="nvidia_news"
)

# Add articles
for i, article in enumerate(articles):

    text = article["title"] + " " + article["summary"]

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[text],
        metadatas=[
            {
                "title": article["title"],
                "source": article["source"]
            }
        ]
    )

print(f"Stored {len(articles)} articles in ChromaDB")