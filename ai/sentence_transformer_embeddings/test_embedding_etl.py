"""
Test the complete embedding pipeline with a small batch.
"""

from embedding_etl import EmbeddingETL


def main():
    etl = EmbeddingETL()

    # Validate services
    etl.initialize()

    print("\nRunning ETL on first batch...\n")

    inserted = etl.process_batch(offset=0)

    print("\n===================================")
    print("TEST COMPLETED")
    print("===================================")
    print(f"Inserted : {inserted}")
    print(f"Processed: {etl.processed}")
    print(f"Skipped  : {etl.skipped}")
    print(f"Failed   : {etl.failed}")
    print("===================================")


if __name__ == "__main__":
    main()