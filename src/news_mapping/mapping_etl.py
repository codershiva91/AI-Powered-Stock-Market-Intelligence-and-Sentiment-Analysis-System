"""
==============================================================================
News Mapping ETL
==============================================================================

Project : AI-Driven Stock Market Intelligence System

Description
-----------
Maps news articles to stock symbols and stores relationships in the
news_stock_mapping table.

Workflow
--------
Load Companies
        │
        ▼
Initialize Company Matcher
        │
        ▼
Load Unmapped News
        │
        ▼
Match Companies
        │
        ▼
Batch Insert
        │
        ▼
news_stock_mapping

==============================================================================
"""

from ai.common.logger import get_logger

from news_mapping.company_matcher import CompanyMatcher
from news_mapping.mapping_repository import MappingRepository

from news_mapping.config import (
    BATCH_SIZE,
    DEFAULT_RELEVANCE_SCORE,
    LOG_PROGRESS_EVERY,
)

logger = get_logger(__name__)


class NewsMappingETL:

    def __init__(self):

        self.repository = MappingRepository()
        self.matcher = None

    # ------------------------------------------------------------------

    def initialize_matcher(self):
        """
        Initialize CompanyMatcher.
        """

        companies = self.repository.load_companies()

        logger.info(
            "Loaded %d companies from symbol_master.",
            len(companies)
        )

        self.matcher = CompanyMatcher(companies)

    # ------------------------------------------------------------------

    def flush_batch(self, values):
        """
        Bulk insert mappings.

        Returns inserted row count.
        """

        if not values:
            return 0

        inserted = self.repository.insert_many(values)

        values.clear()

        return inserted

    # ------------------------------------------------------------------

    def process(self):
        """
        Execute News Mapping ETL.
        """

        logger.info("=" * 80)
        logger.info("NEWS MAPPING ETL STARTED")
        logger.info("=" * 80)

        try:

            self.initialize_matcher()

            news_articles = self.repository.load_unmapped_news()

            total_news = len(news_articles)

            logger.info(
                "Found %d unmapped news articles.",
                total_news
            )

            values = []

            mapped_news = 0
            total_mappings = 0
            total_inserted = 0

            for index, news in enumerate(news_articles, start=1):

                news_id = news["news_id"]

                title = news.get("title") or ""

                article = news.get("article_text") or ""

                symbols = self.matcher.match(
                    title,
                    article
                )

                if symbols:
                    mapped_news += 1

                for symbol in symbols:

                    values.append(
                        (
                            news_id,
                            symbol,
                            DEFAULT_RELEVANCE_SCORE
                        )
                    )

                    total_mappings += 1

                # Flush batch
                if len(values) >= BATCH_SIZE:

                    total_inserted += self.flush_batch(values)

                # Progress logging
                if index % LOG_PROGRESS_EVERY == 0:

                    logger.info(
                        "Processed %d/%d news articles",
                        index,
                        total_news
                    )

            # Insert remaining rows
            total_inserted += self.flush_batch(values)

            logger.info("=" * 80)
            logger.info("NEWS MAPPING ETL COMPLETED")
            logger.info("=" * 80)

            logger.info("News Processed      : %d", total_news)
            logger.info("Mapped News         : %d", mapped_news)
            logger.info("Mappings Prepared   : %d", total_mappings)
            logger.info("Mappings Inserted   : %d", total_inserted)

            logger.info("=" * 80)

            return {
                "news_processed": total_news,
                "mapped_news": mapped_news,
                "mappings_prepared": total_mappings,
                "mappings_inserted": total_inserted,
            }

        except Exception as e:

            logger.exception(
                "News Mapping ETL failed: %s",
                str(e)
            )

            raise


# ----------------------------------------------------------------------

if __name__ == "__main__":

    etl = NewsMappingETL()

    etl.process()