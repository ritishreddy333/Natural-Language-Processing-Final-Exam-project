import chromadb
from sentence_transformers import SentenceTransformer
print("Loaded:", __name__)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="vectordb/chroma_db"
)

# Load collection
collection = client.get_collection(
    name="nvidia_news"
)


def retrieve_documents(query, n_results=5):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    documents = results["documents"][0]
    metadatas = results.get("metadatas", [[]])[0]

    retrieved_documents = []

    for i, doc in enumerate(documents):

        metadata = {}

        if i < len(metadatas):
            metadata = metadatas[i]

        retrieved_documents.append(
            {
                "rank": i + 1,
                "document": doc,
                "metadata": metadata
            }
        )

    return retrieved_documents


if __name__ == "__main__":

    query = input("Ask a question: ")

    results = retrieve_documents(query)

    for result in results:

        print(f"\nResult {result['rank']}")

        if result["metadata"]:
            print("Metadata:", result["metadata"])

        print(result["document"][:500])