import chromadb
from sentence_transformers import SentenceTransformer
import ollama

print("Loading models...")

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="vectordb/chroma_db")

collection = client.get_collection("nvidia_news")

query = """
What are the biggest opportunities,
risks and strategic priorities for NVIDIA?
"""

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=15
)

documents = results["documents"][0]

evidence_text = "\n\n".join(documents)

prompt = f"""
You are the CEO Strategic Intelligence Agent for NVIDIA.

Based ONLY on the evidence below:

{evidence_text}

Generate 3 executive recommendations.

For each recommendation provide:

RECOMMENDATION

SUPPORTING EVIDENCE
- Evidence 1
- Evidence 2
- Evidence 3

EXPECTED IMPACT
- Revenue impact
- Market impact
- Customer impact

RISK ASSESSMENT
- Financial risk
- Operational risk
- Strategic risk

Use only information from the evidence.
Do not invent facts.
"""

response = ollama.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n")
print("=" * 60)
print("FINAL EVIDENCE-BASED RECOMMENDATIONS")
print("=" * 60)
print("\n")

print(response["message"]["content"])