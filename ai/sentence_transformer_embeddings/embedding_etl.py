"""
=========================================================
Embedding ETL Pipeline
Sentence Transformer Embedding Module

Author : Shivam Sahu
Project : AI Stock Market Intelligence System
=========================================================
"""

import math
import time

from .config import (
    FETCH_BATCH_SIZE,
    UPLOAD_BATCH_SIZE,
    COLLECTION_NAME
)

from .database import (
    test_connection,
    get_total_news_count,
    fetch_news_batch
)

from .embedding_service import EmbeddingService

from .qdrant_manager import QdrantManager

from .logger import get_logger

logger = get_logger(__name__)


class EmbeddingETL:
    """
    Production ETL Pipeline

    MariaDB
        ↓
    Sentence Transformer
        ↓
    Qdrant
    """

    def __init__(self):

        logger.info("=" * 70)
        logger.info("Sentence Transformer Embedding ETL")
        logger.info("=" * 70)

        self.embedding_service = EmbeddingService()

        self.qdrant = QdrantManager()

        self.total_records = get_total_news_count()

        self.processed = 0
        self.inserted = 0
        self.skipped = 0
        self.failed = 0

        self.start_time = time.time()

        logger.info(f"Total News Records : {self.total_records}")
        logger.info(f"Fetch Batch Size   : {FETCH_BATCH_SIZE}")
        logger.info(f"Upload Batch Size  : {UPLOAD_BATCH_SIZE}")
        logger.info(f"Collection         : {COLLECTION_NAME}")

        logger.info("-" * 70)

    # =====================================================

    def initialize(self):
        """
        Validate all services.
        """

        logger.info("Checking MariaDB Connection...")

        if not test_connection():

            raise Exception("MariaDB Connection Failed")

        logger.info("MariaDB Connected")

        logger.info("Checking Qdrant Connection...")

        if not self.qdrant.test_connection():

            raise Exception("Qdrant Connection Failed")

        logger.info("Qdrant Connected")

        self.qdrant.create_collection()

    # =====================================================

    def elapsed_time(self):

        return time.time() - self.start_time

    # =====================================================

    def eta(self):

        if self.processed == 0:

            return 0

        rate = self.elapsed_time() / self.processed

        remaining = self.total_records - self.processed

        return remaining * rate

    # =====================================================

    def print_progress(self):

        logger.info("-" * 70)

        logger.info(f"Processed : {self.processed}/{self.total_records}")

        logger.info(f"Inserted  : {self.inserted}")

        logger.info(f"Skipped   : {self.skipped}")

        logger.info(f"Failed    : {self.failed}")

        logger.info(f"Elapsed   : {self.elapsed_time():.2f} sec")

        logger.info(f"ETA       : {self.eta()/60:.2f} min")

        logger.info("-" * 70)
        
        
    # =====================================================
    # Process One Batch
    # =====================================================

    def process_batch(self, offset):
        """
        Process one batch of news articles.

        Parameters
        ----------
        offset : int

        Returns
        -------
        int
            Number of vectors inserted.
        """

        logger.info(f"Fetching records from Offset : {offset}")

        rows = fetch_news_batch(
            offset=offset,
            batch_size=FETCH_BATCH_SIZE
        )

        if not rows:

            logger.warning("No records found.")

            return 0

        points = []

        for row in rows:

            self.processed += 1

            try:

                point = self.embedding_service.process_news(row)

                if point is None:

                    self.skipped += 1

                    continue

                points.append(point)

            except Exception:

                self.failed += 1

                logger.exception(
                    f"Failed to process News ID {row.get('news_id')}"
                )

        if len(points) == 0:

            logger.warning("No valid embeddings generated.")

            return 0

        inserted = self.upload_points(points)

        return inserted

    # =====================================================
    # Upload Batch to Qdrant
    # =====================================================

    def upload_points(self, points):
        """
        Upload one batch of vectors.

        Parameters
        ----------
        points : list[PointStruct]

        Returns
        -------
        int
        """

        total_uploaded = 0

        for start in range(0, len(points), UPLOAD_BATCH_SIZE):

            batch = points[start:start + UPLOAD_BATCH_SIZE]

            try:

                self.qdrant.insert_batch(batch)

                total_uploaded += len(batch)

                self.inserted += len(batch)

            except Exception:

                self.failed += len(batch)

                logger.exception("Batch upload failed.")

        return total_uploaded
    
    
    # =====================================================
    # Run Complete ETL
    # =====================================================

    def run(self):
        """
        Execute the complete embedding pipeline.
        """

        self.initialize()

        total_batches = math.ceil(
            self.total_records / FETCH_BATCH_SIZE
        )

        logger.info("")
        logger.info("=" * 70)
        logger.info(f"Total Batches : {total_batches}")
        logger.info("=" * 70)

        for batch_number in range(total_batches):

            offset = batch_number * FETCH_BATCH_SIZE

            logger.info("")
            logger.info("=" * 70)
            logger.info(
                f"Processing Batch "
                f"{batch_number + 1}/{total_batches}"
            )
            logger.info("=" * 70)

            batch_start = time.time()

            inserted = self.process_batch(offset)

            batch_time = time.time() - batch_start

            logger.info(
                f"Batch Inserted : {inserted} vectors"
            )

            logger.info(
                f"Batch Time : {batch_time:.2f} sec"
            )

            self.print_progress()

        logger.info("")
        logger.info("=" * 70)
        logger.info("Embedding Pipeline Finished")
        logger.info("=" * 70)

        self.print_summary()

    # =====================================================
    # Final Summary
    # =====================================================

    def print_summary(self):
        """
        Print ETL summary.
        """

        total_time = self.elapsed_time()

        logger.info("")
        logger.info("=" * 70)
        logger.info("FINAL SUMMARY")
        logger.info("=" * 70)

        logger.info(
            f"Total Records     : {self.total_records}"
        )

        logger.info(
            f"Processed Records : {self.processed}"
        )

        logger.info(
            f"Inserted Vectors  : {self.inserted}"
        )

        logger.info(
            f"Skipped Records   : {self.skipped}"
        )

        logger.info(
            f"Failed Records    : {self.failed}"
        )

        logger.info(
            f"Execution Time    : {total_time:.2f} sec"
        )

        if total_time > 60:

            logger.info(
                f"Execution Time    : "
                f"{total_time/60:.2f} min"
            )

        logger.info("=" * 70)
        

# =====================================================
# Main
# =====================================================

def main():
    """
    Entry point for the Sentence Transformer ETL pipeline.
    """

    logger.info("")
    logger.info("=" * 70)
    logger.info("Starting Sentence Transformer Embedding ETL")
    logger.info("=" * 70)

    try:
        etl = EmbeddingETL()
        etl.run()

        logger.info("")
        logger.info("=" * 70)
        logger.info("ETL Pipeline Completed Successfully")
        logger.info("=" * 70)

    except KeyboardInterrupt:

        logger.warning("")
        logger.warning("=" * 70)
        logger.warning("ETL Interrupted By User")
        logger.warning("=" * 70)

    except Exception as e:

        logger.exception("Unexpected Error During ETL Execution")
        logger.error(str(e))

    finally:

        logger.info("")
        logger.info("=" * 70)
        logger.info("Program Finished")
        logger.info("=" * 70)


# =====================================================

if __name__ == "__main__":
    main()
    
                        