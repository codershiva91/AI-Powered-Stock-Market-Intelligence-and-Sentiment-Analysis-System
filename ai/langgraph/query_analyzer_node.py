from ai.common.logger import get_logger
from ai.langgraph.state import GraphState
from ai.query_analyzer.analyzer import QueryAnalyzer

logger = get_logger(__name__)


class QueryAnalyzerNode:
    """
    LangGraph node responsible for analysing
    the user's natural language query.
    """

    def __init__(self):
        self.analyzer = QueryAnalyzer()

    def __call__(self, state: GraphState) -> GraphState:

        logger.info("=" * 60)
        logger.info("QUERY ANALYZER NODE")
        logger.info("=" * 60)

        try:
            question = state["question"]

            logger.info("Question : %s", question)

            analysis = self.analyzer.analyze(question)

            logger.info("Analysis Output : %s", analysis)

            state["query_analysis"] = analysis

            logger.info("Query analysis stored successfully.")

            return state

        except Exception as e:

            logger.exception("Query Analyzer Node failed.")

            state["error"] = str(e)

            return state