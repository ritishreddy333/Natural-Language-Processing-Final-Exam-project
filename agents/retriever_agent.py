from vectordb.search import retrieve_documents


def retrieve(goal):

    print("\nRetriever Agent Started...")

    documents = retrieve_documents(goal)

    print(f"Retrieved {len(documents)} documents.")

    return documents


if __name__ == "__main__":

    goal = input("Enter business goal: ")

    docs = retrieve(goal)

    print("\nTop Retrieved Documents:\n")

    for doc in docs:

        print(f"Rank : {doc['rank']}")

        if doc["metadata"]:
            print("Title :", doc["metadata"].get("title", "Unknown"))

            print("Source :", doc["metadata"].get("source", "Unknown"))

        print(doc["document"][:300])

        print()