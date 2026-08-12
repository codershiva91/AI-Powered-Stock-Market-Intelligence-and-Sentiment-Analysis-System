"""
=========================================================
Evaluation Engine
=========================================================

Author : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System
=========================================================
"""

import json
import time
from pathlib import Path

from ai.pipeline.rag_pipeline import RAGPipeline

from ai.evaluation.logger import get_logger
from ai.evaluation.formatter import EvaluationFormatter

logger = get_logger(__name__)


class Evaluator:
    """
    Runs benchmark questions through the RAG pipeline.
    """

    def __init__(self, benchmark_file=None):

        logger.info("Initializing Evaluator...")

        self.pipeline = RAGPipeline()

        if benchmark_file is None:
            benchmark_file = (
                Path(__file__).parent /
                "benchmark_questions.json"
            )

        self.benchmark_file = benchmark_file

        self.questions = self.load_questions()

        self.results = []

        logger.info(
            f"Loaded {len(self.questions)} benchmark questions."
        )

    ##################################################################

    def load_questions(self):

        with open(
            self.benchmark_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    ##################################################################

    def evaluate(self):

        logger.info("=" * 70)
        logger.info("Starting Evaluation")
        logger.info("=" * 70)

        for index, item in enumerate(self.questions, start=1):

            question = item["question"]

            logger.info(f"Running Test {index}")

            start = time.perf_counter()

            try:

                result = self.pipeline.ask(question)

                end = time.perf_counter()

                elapsed = round(end - start, 2)

                if isinstance(result, dict):

                    answer = result.get("response", "")

                    retrieved = result.get(
                        "retrieved_docs",
                        0
                    )

                else:

                    answer = result

                    retrieved = 0

                success = (
                    "Insufficient information"
                    not in answer
                )

                record = {
                    "test": index,
                    "question": question,
                    "response": answer,
                    "retrieved_docs": retrieved,
                    "response_time": elapsed,
                    "status":
                        "PASS" if success else "FAIL"
                }

                self.results.append(record)

                print(
                    EvaluationFormatter.format_test(
                        test_number=index,
                        question=question,
                        retrieved_docs=retrieved,
                        response_time=elapsed,
                        status=record["status"]
                    )
                )

            except Exception as e:

                logger.exception(e)

                self.results.append({

                    "test": index,

                    "question": question,

                    "response": "",

                    "retrieved_docs": 0,

                    "response_time": 0,

                    "status": "ERROR"
                })

        logger.info("Evaluation completed.")

        return self.results

    ##################################################################

    def summary(self):

        total = len(self.results)

        passed = sum(
            r["status"] == "PASS"
            for r in self.results
        )

        failed = total - passed

        average = (
            sum(
                r["response_time"]
                for r in self.results
            ) / total
            if total else 0
        )

        metrics = {

            "total_questions": total,

            "successful_queries": passed,

            "failed_queries": failed,

            "average_response_time": average,

            "retriever_accuracy": (
                (passed / total) * 100
                if total else 0
            ),

            "llm_success_rate": (
                (passed / total) * 100
                if total else 0
            ),

            "no_result_rate": (
                (failed / total) * 100
                if total else 0
            )

        }

        print(
            EvaluationFormatter.format_summary(
                metrics
            )
        )

        return metrics

    ##################################################################

    def save_results(self):

        output = (
            Path(__file__).parent /
            "evaluation_results.json"
        )

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.results,
                file,
                indent=4,
                ensure_ascii=False
            )

        logger.info(
            f"Results saved to {output}"
        )
        
        