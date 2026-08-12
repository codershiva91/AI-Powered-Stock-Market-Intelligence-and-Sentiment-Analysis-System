
"""
==========================================================
Production FinBERT Sentiment ETL Pipeline V2

Author  : Shivam Sahu
Project : AI-Driven Stock Market Intelligence System

Features
--------
✓ Resume Processing
✓ Batch Processing
✓ Bulk Insert
✓ Automatic Commit
✓ Logging
✓ Progress Bar
✓ Graceful Shutdown
✓ Production Ready
==========================================================
"""

import signal
import time

from tqdm import tqdm

from db import get_connection
from preprocess import clean_text
from finbert_model import predict_sentiment

from logger import get_logger

from config import (
    BATCH_SIZE,
    MODEL_NAME
)

logger = get_logger()


# ---------------------------------------------------------
# Global Variables
# ---------------------------------------------------------

shutdown_requested = False


# ---------------------------------------------------------
# CTRL + C Handler
# ---------------------------------------------------------

def signal_handler(sig, frame):
    """
    Handles CTRL+C gracefully.

    Instead of terminating immediately,
    the current batch is committed first.
    """

    global shutdown_requested

    logger.warning("CTRL+C received.")
    logger.warning("Stopping after current batch...")

    shutdown_requested = True


signal.signal(signal.SIGINT, signal_handler)


# ==========================================================
# SQL Queries
# ==========================================================

SELECT_UNPROCESSED_NEWS_QUERY = """
SELECT
    n.news_id,
    n.title,
    n.article_text
FROM news_articles n
LEFT JOIN news_sentiment s
       ON n.news_id = s.news_id
WHERE s.news_id IS NULL
ORDER BY n.news_id;
"""

INSERT_SENTIMENT_QUERY = """
INSERT INTO news_sentiment
(
    news_id,
    sentiment,
    confidence_score,
    model_name
)
VALUES
(
    %s,
    %s,
    %s,
    %s
)
"""


# ==========================================================
# Database Read Function
# ==========================================================



def load_unprocessed_news(cursor):
    """
    Loads only news articles that have not yet been analysed.
    """

    cursor.execute(SELECT_UNPROCESSED_NEWS_QUERY)

    return cursor.fetchall()


# ==========================================================
# Batch Insert Function
# ==========================================================

def save_batch(write_cursor, connection, batch):
    """
    Saves one batch into MariaDB.
    """

    if not batch:
        return

    try:

        write_cursor.executemany(
            INSERT_SENTIMENT_QUERY,
            batch
        )

        connection.commit()

        logger.info(
            f"Committed {len(batch)} records."
        )

    except Exception as e:

        connection.rollback()

        logger.exception(
            f"Batch insert failed: {e}"
        )

        raise    
    
#==================================

#Statistics Class

#===================================  

class Statistics:

    def __init__(self):

        self.total = 0

        self.processed = 0

        self.failed = 0

        self.skipped = 0

        self.positive = 0

        self.neutral = 0

        self.negative = 0

    def print_summary(self):

        logger.info("=" * 60)

        logger.info("ETL SUMMARY")

        logger.info("=" * 60)

        logger.info(f"Total     : {self.total}")

        logger.info(f"Processed : {self.processed}")

        logger.info(f"Skipped   : {self.skipped}")

        logger.info(f"Failed    : {self.failed}")

        logger.info(f"Positive  : {self.positive}")

        logger.info(f"Neutral   : {self.neutral}")

        logger.info(f"Negative  : {self.negative}")  
       
# =====================================================
# Text Processing Function
# This keeps the main loop clean.

def process_news(row, stats):
    """
    Cleans news text, predicts sentiment using FinBERT,
    updates statistics, and prepares a database record.
    """

    news_id = row["news_id"]

    title = row["title"] or ""
    article = row["article_text"] or ""

    # Combine title and article
    text = clean_text(f"{title} {article}")

    # Skip empty articles
    if not text.strip():
        stats.skipped += 1
        return None

    # Predict sentiment
    prediction = predict_sentiment(text)

    sentiment = prediction["label"]
    confidence = float(prediction["score"])

    # Update statistics
    if sentiment == "Positive":
        stats.positive += 1

    elif sentiment == "Negative":
        stats.negative += 1

    elif sentiment == "Neutral":
        stats.neutral += 1

    else:
        raise ValueError(
            f"Unexpected sentiment label: {sentiment}"
        )

    stats.processed += 1

    # Prepare tuple for bulk insert
    return (
        news_id,
        sentiment,
        confidence,
        MODEL_NAME
    )
#==============================================
#Main Function (Beginning)

#==============================================
          
def main():

    logger.info("=" * 70)

    logger.info(
        "Production FinBERT ETL Started"
    )

    logger.info("=" * 70)

    start_time = time.time()

    
    connection = None
    read_cursor = None
    write_cursor = None
    try:

        connection = get_connection()

        read_cursor = connection.cursor()

        write_cursor = connection.cursor()
        
        logger.info("Database Connected")

        news = load_unprocessed_news(read_cursor)

        stats = Statistics()

        stats.total = len(news)

        logger.info(
            f"Found {stats.total} news articles."
        )

        if stats.total == 0:

            logger.info("Nothing to process.")

            return

        batch = []
        

        logger.info("Starting sentiment analysis...")

        for row in tqdm(
                news,
                total=stats.total,
                desc="Processing News",
                unit="article"
        ):

            # ---------------------------------------
            # Graceful shutdown
            # ---------------------------------------

            if shutdown_requested:

                logger.warning(
                    "Shutdown requested. Saving remaining batch..."
                )

                break

            try:

                result = process_news(
                    row,
                    stats
                )

                if result is None:
                    continue

                batch.append(result)

                # ---------------------------------------
                # Batch Size Reached
                # ---------------------------------------

                if len(batch) >= BATCH_SIZE:

                    save_batch(
                        write_cursor,
                        connection,
                        batch
                    )

                    batch.clear()

            except Exception as e:

                stats.failed += 1

                logger.exception(
                     f"Failed processing News ID {row['news_id']}: {e}"
                )

        # ---------------------------------------
        # Save Remaining Records
        # ---------------------------------------

        if batch:

            logger.info(
                "Saving final batch..."
            )

            save_batch(
                write_cursor,
                connection,
                batch
            )

            batch.clear()

        elapsed = time.time() - start_time
        
        success_rate = (stats.processed / max(stats.total, 1)) * 100

        logger.info(f"Success Rate : {success_rate:.2f}%")
        

        logger.info("")

        logger.info("=" * 70)

        logger.info(
            "Production FinBERT ETL Completed"
        )

        logger.info("=" * 70)

        logger.info(
            f"Execution Time : {elapsed:.2f} seconds"
        )

        logger.info(
            f"Average Speed : "
            f"{stats.processed/max(elapsed,1):.2f} "
            f"articles/sec"
        )

        logger.info(f"Model Used : {MODEL_NAME}")
        
        stats.print_summary()
        
#========================================

#Exception Handling                          

#========================================

    except Exception as e:

        logger.exception( f"ETL Pipeline Failed: {e}")
        if connection:

            connection.rollback()

    finally:

        try:

            if read_cursor:
                read_cursor.close()

            if write_cursor:
                write_cursor.close()
                
            if connection:
                connection.close()    

        except Exception:

            pass

        logger.info("Database Connection Closed")

#================================================

#Program Entry Point        

#================================================

if __name__ == "__main__":

    main()