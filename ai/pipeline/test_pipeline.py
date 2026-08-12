from ai.pipeline.rag_pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    question = "Latest Reliance news"

    result = pipeline.ask(question)

    print("\n========== PIPELINE RESULT ==========\n")

    print("Question         :", result["question"])
    print("Retrieved Docs   :", result["retrieved_docs"])
    print("Reranked Docs    :", result["reranked_docs"])
    print("Context Length   :", result["context_length"])
    print("Success          :", result["success"])

    print("\n========== RESPONSE ==========\n")

    print(result["response"])


if __name__ == "__main__":
    main()