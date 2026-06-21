import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="vectordb/chroma_db"
)

collection = client.get_collection(
    name="nvidia_news"
)

query = "Latest NVIDIA developments"

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

    if any(word in text for word in [
        "partnership",
        "collaboration",
        "expansion",
        "investment",
        "market"
    ]):
        opportunities.append(doc)

    if any(word in text for word in [
        "competition",
        "regulation",
        "risk",
        "challenge",
        "shortage"
    ]):
        risks.append(doc)

    if any(word in text for word in [
        "ai",
        "agentic",
        "infrastructure",
        "technology",
        "factory"
    ]):
        trends.append(doc)

print("\n==============================")
print("STRATEGIC INTELLIGENCE REPORT")
print("==============================")

print("\nOPPORTUNITY 1")
print("Title: AI Infrastructure Expansion")
print("Evidence:")
for item in opportunities[:2]:
    print("-", item[:150])

print("\nBusiness Impact:")
print("Growing demand for enterprise AI infrastructure")

print("\nConfidence:")
print("High")

print("\n---------------------------")

print("\nRISK 1")
print("Title: Competitive Pressure")

print("Evidence:")
for item in risks[:2]:
    print("-", item[:150])

print("\nBusiness Impact:")
print("Potential market share pressure")

print("\nConfidence:")
print("Medium")

print("\n---------------------------")

print("\nTREND 1")
print("Title: Agentic AI and AI Factories")

print("Evidence:")
for item in trends[:3]:
    print("-", item[:150])

print("\nBusiness Impact:")
print("Accelerating enterprise AI adoption")

print("\nConfidence:")
print("High")