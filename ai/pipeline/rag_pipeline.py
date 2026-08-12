"""
=========================================================
RAG Pipeline
=========================================================

Author : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System
"""

from ai.retriever.retriever import Retriever
from ai.cross_encoder.reranker import CrossEncoderReranker
from ai.context_builder.builder import ContextBuilder
from ai.llm.gemini_client import GeminiClient
from ai.llm.logger import get_logger

logger = get_logger(__name__)


class RAGPipeline:
    """
    End-to-End Retrieval Augmented Generation Pipeline
    """

    def __init__(self):

        logger.info("Initializing RAG Pipeline...")

        # --------------------------------------------------
        # Initialize Components
        # --------------------------------------------------

        self.retriever = Retriever()
        self.reranker = CrossEncoderReranker()
        self.context_builder = ContextBuilder()
        self.llm = GeminiClient()

        logger.info("RAG Pipeline initialized successfully.")

    ##################################################################

    def ask(self, question: str):
        """
        Execute complete RAG pipeline.

        Returns
        -------
        dict
            Pipeline response and metadata.
        """

        logger.info("=" * 60)
        logger.info("New User Question")
        logger.info(question)
        logger.info("=" * 60)

        try:

            # --------------------------------------------------
            # STEP 1 : Retrieve Documents
            # --------------------------------------------------

            logger.info("Retrieving relevant documents...")

            documents = self.retriever.search_without_filters(
                query=question
            )

            logger.info(
                f"Retrieved {len(documents)} documents."
            )

            # No documents retrieved

            if not documents:

                logger.warning("No relevant documents found.")

                return {
                    "question": question,
                    "response": "Insufficient information available in the knowledge base.",
                    "retrieved_docs": 0,
                    "reranked_docs": 0,
                    "context_length": 0,
                    "retrieved_documents": [],
                    "reranked_documents": [],
                    "success": False,
                    "error": "No documents retrieved"
                }

            # --------------------------------------------------
            # STEP 2 : Cross Encoder Reranking
            # --------------------------------------------------

            logger.info("Reranking retrieved documents...")

            ranked_documents = self.reranker.rerank(
                query=question,
                documents=documents
            )

            logger.info(
                f"Top {len(ranked_documents)} documents selected."
            )

            # Debug Output

            for i, doc in enumerate(ranked_documents, start=1):

                logger.info(
                    f"""
Rank {i}

Vector Score   : {doc.get('score')}

Cross Score    : {doc.get('rerank_score')}

Title          : {doc.get('title')}

Source         : {doc.get('source')}

Sentiment      : {doc.get('sentiment')}
"""
                )

            # --------------------------------------------------
            # STEP 3 : Build Context
            # --------------------------------------------------

            logger.info("Building context...")

            context = self.context_builder.build(
                ranked_documents
            )

            logger.info(
                f"Context Length : {len(context)} characters"
            )

            # --------------------------------------------------
            # STEP 4 : Prompt Engineering
            # --------------------------------------------------

            logger.info("Building final prompt...")

            prompt = f"""
You are an expert AI Financial Analyst.

Use ONLY the retrieved context below.

If the answer is not available in the retrieved context,
reply exactly:

"Insufficient information available in the knowledge base."

Do not hallucinate.
Do not use outside knowledge.

========================================================

QUESTION

{question}

========================================================

RETRIEVED CONTEXT

{context}

========================================================

Provide your response in the following format:

1. Direct Answer

2. Supporting Evidence

3. Overall Sentiment

4. Confidence Level
"""

            # --------------------------------------------------
            # STEP 5 : Generate Response
            # --------------------------------------------------

            logger.info("Generating response...")

            response = self.llm.generate(prompt)

            logger.info("Pipeline completed successfully.")

            # --------------------------------------------------
            # Final Result
            # --------------------------------------------------

            return {
                "question": question,
                "response": response,
                "retrieved_docs": len(documents),
                "reranked_docs": len(ranked_documents),
                "context_length": len(context),
                "retrieved_documents": documents,
                "reranked_documents": ranked_documents,
                "success": True,
                "error": None
            }

        except Exception as e:

            logger.exception("RAG Pipeline failed.")

            return {
                "question": question,
                "response": "An unexpected error occurred while processing your request.",
                "retrieved_docs": 0,
                "reranked_docs": 0,
                "context_length": 0,
                "retrieved_documents": [],
                "reranked_documents": [],
                "success": False,
                "error": str(e)
            }