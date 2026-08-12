"""
LangGraph Nodes
"""

from ai.langgraph.state import GraphState
from ai.cross_encoder.reranker import CrossEncoderReranker

from ai.retriever.retriever import Retriever
from ai.context_builder.builder import ContextBuilder
from ai.llm.gemini_client import GeminiClient

# ------------------------------------------------------------------
# Initialize Components (loaded once)
# ------------------------------------------------------------------

retriever = Retriever()
context_builder = ContextBuilder()
gemini = GeminiClient()
reranker = CrossEncoderReranker()

# ------------------------------------------------------------------
# Retrieval Node
# ------------------------------------------------------------------

def retrieval_node(state: GraphState) -> GraphState:
    """
    Retrieve relevant documents from Qdrant.
    """

    print("\n" + "=" * 80)
    print("RETRIEVAL NODE")
    print("=" * 80)
    print(f"Question : {state['question']}\n")

    try:
        documents = retriever.search(
            query=state["question"]
        )

        print(f"Retrieved {len(documents)} documents.\n")

        # Display retrieved documents
        for i, doc in enumerate(documents, start=1):

            print(f"Document #{i}")
            print("-" * 60)

            print(f"Title      : {doc.get('title', 'N/A')}")
            print(f"Source     : {doc.get('source', 'N/A')}")
            print(f"Topic      : {doc.get('topic', 'N/A')}")
            print(f"Published  : {doc.get('published_at', 'N/A')}")
            print(f"Sentiment  : {doc.get('sentiment', 'N/A')}")
            print(f"Score      : {doc.get('score', 'N/A')}")

            content = doc.get("document") or ""
            if content:
                print(f"Preview    : {content[:150]}...")
            else:
                print("Preview    : N/A")

            print("-" * 60)

        state["retrieved_documents"] = documents
        return state

    except Exception as e:
        print(f"\n Retrieval Error : {e}")
        state["error"] = str(e)
        return state


# ------------------------------------------------------------------
# Context Builder Node
# ------------------------------------------------------------------

def context_builder_node(state: GraphState) -> GraphState:
    """
    Convert retrieved documents into LLM context.
    """

    print("\n" + "=" * 80)
    print("CONTEXT BUILDER NODE")
    print("=" * 80)

    try:

        context = context_builder.build(
            documents=state["reranked_documents"]
        )

        state["context"] = context

        print("Context built successfully.")
        print(f"Context Length : {len(context)} characters\n")

        return state

    except Exception as e:

        print(f"\n Context Builder Error : {e}")
        state["error"] = str(e)
        return state


# ------------------------------------------------------------------
# Gemini Node
# ------------------------------------------------------------------

def gemini_node(state: GraphState) -> GraphState:
    """
    Generate answer using Gemini.
    """

    print("\n" + "=" * 80)
    print("GEMINI NODE")
    print("=" * 80)

    try:

        prompt = f"""
You are an AI-powered Stock Market Intelligence Assistant.

Answer ONLY from the provided context.

If the answer is unavailable in the context,
reply with:

"I don't have sufficient information in the retrieved documents."

Question:
{state["question"]}

Context:
{state["context"]}
"""

        answer = gemini.generate(prompt)

        state["answer"] = answer

        print("Gemini Response Generated Successfully.\n")
        print("=" * 80)
        print("FINAL ANSWER")
        print("=" * 80)
        print(answer)
        print("=" * 80)

        return state

    except Exception as e:

        print(f"\n Gemini Error : {e}")
        state["error"] = str(e)
        return state
    
# ------------------------------------------------------------------
# Cross Encoder Node
# ------------------------------------------------------------------

def reranker_node(state: GraphState) -> GraphState:
    """
    Rerank retrieved documents using Cross Encoder.
    """

    print("\n" + "=" * 80)
    print("CROSS ENCODER NODE")
    print("=" * 80)

    try:

        reranked_docs = reranker.rerank(
            query=state["question"],
            documents=state["retrieved_documents"],
        )

        state["reranked_documents"] = reranked_docs

        print(f"Top {len(reranked_docs)} documents selected.\n")

        # Display reranked documents
        for i, doc in enumerate(reranked_docs, start=1):

            print(f"Rank #{i}")
            print("-" * 60)
            print(f"Title          : {doc.get('title')}")
            print(f"Retriever Score: {doc.get('score')}")
            print(f"Rerank Score   : {round(doc.get('rerank_score', 0), 4)}")
            print("-" * 60)

        return state

    except Exception as e:

        print(f"\nCross Encoder Error : {e}")

        state["error"] = str(e)

        return state