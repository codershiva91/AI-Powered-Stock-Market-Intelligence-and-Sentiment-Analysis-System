"""
=========================================================
Qdrant Vector Database Analysis
=========================================================

Author  : Shivam Sahu
Project : AI Stock Market Intelligence System

Description
-----------
Main entry point for analysing the Qdrant Vector Database.

Workflow
--------
1. Connect to Qdrant
2. Fetch all vectors
3. Compute statistics
4. Validate payloads
5. Detect duplicates
6. Generate report

=========================================================
"""

#from ai.qdrant.qdrant_manager import QdrantManager
from ai.sentence_transformer_embeddings.qdrant_manager import QdrantManager



from ai.vector_analysis.statistics import VectorStatistics
from ai.vector_analysis.payload_validator import PayloadValidator
from ai.vector_analysis.duplicate_detector import DuplicateDetector
from ai.vector_analysis.report_generator import ReportGenerator


def main():

    print("\nConnecting to Qdrant...\n")

    ############################################################
    # Connect Qdrant
    ############################################################

    manager = QdrantManager()

    ############################################################
    # Test Connection
    ############################################################

    if not manager.test_connection():

        print("Unable to connect to Qdrant.")

        return

    ############################################################
    # Fetch All Points
    ############################################################

    print("Fetching all vectors from collection...\n")

    points = manager.get_all_points()

    print(f"Total Points Retrieved : {len(points)}")

    ############################################################
    # Statistics
    ############################################################

    statistics = VectorStatistics(points)

    ############################################################
    # Payload Validation
    ############################################################

    validator = PayloadValidator(points)

    ############################################################
    # Duplicate Detection
    ############################################################

    detector = DuplicateDetector(points)

    ############################################################
    # Generate Report
    ############################################################

    ReportGenerator.final_summary(

        statistics,

        validator,

        detector

    )

    ############################################################

    print("\nVector Database Analysis Completed Successfully.\n")


############################################################

if __name__ == "__main__":

    main()