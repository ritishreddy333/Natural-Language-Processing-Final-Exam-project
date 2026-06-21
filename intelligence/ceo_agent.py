import chromadb
import ollama
from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="vectordb/chroma_db"
)

collection = client.get_collection(
    name="nvidia_news"
)

query = input("\nAsk the CEO Agent: ")

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=10
)

documents = results["documents"][0]

context = "\n\n".join(documents)

print("\nAnalyzing strategic information...\n")

prompt = f"""
You are the CEO Strategic Intelligence Agent for NVIDIA.

Analyze the evidence below and answer as a senior business strategist.

EVIDENCE:

{context}

QUESTION:
{query}

Provide:

1. Major Opportunities
2. Major Risks
3. Key Trends
4. Strategic Recommendations

For every recommendation include:

Priority:
Supporting Evidence:
Expected Impact:
Risk Assessment:

Use executive-level business language.
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
print("CEO STRATEGIC BRIEFING")
print("=" * 60)
print("\n")
print(response["message"]["content"])