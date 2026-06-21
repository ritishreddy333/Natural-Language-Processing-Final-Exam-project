import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="vectordb/chroma_db"
)

collection = client.get_collection(
    name="nvidia_news"
)

query = "Latest developments at NVIDIA"

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=20
)

documents = results["documents"][0]

opportunities = []
risks = []
trends = []

for doc in documents:

    text = doc.lower()

    # Opportunities
    if any(word in text for word in [
        "partnership",
        "growth",
        "expansion",
        "investment",
        "market",
        "opportunity"
    ]):
        opportunities.append(doc[:200])

    # Risks
    if any(word in text for word in [
        "risk",
        "competition",
        "regulation",
        "shortage",
        "challenge"
    ]):
        risks.append(doc[:200])

    # Trends
    if any(word in text for word in [
        "ai",
        "agentic",
        "infrastructure",
        "trend",
        "technology"
    ]):
        trends.append(doc[:200])

print("\n===== OPPORTUNITIES =====")
for item in opportunities[:5]:
    print("-", item)

print("\n===== RISKS =====")
for item in risks[:5]:
    print("-", item)

print("\n===== TRENDS =====")
for item in trends[:5]:
    print("-", item)