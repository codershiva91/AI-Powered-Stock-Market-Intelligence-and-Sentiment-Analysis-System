from ai.langgraph.graph import graph

state = {
    "question": "Latest news about Reliance",
    "retrieved_documents": [],
    "context": "",
    "answer": "",
    "metadata": {},
    "error": "",
}

result = graph.invoke(state)

print(result["answer"])