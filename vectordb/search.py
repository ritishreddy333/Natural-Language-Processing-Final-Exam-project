import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="vectordb/chroma_db"
)

collection = client.get_collection(
    name="nvidia_news"
)

query = input("Ask a question: ")

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

for i, doc in enumerate(results["documents"][0]):

    print("\n")
    print(f"Result {i+1}")
    print(doc[:500])