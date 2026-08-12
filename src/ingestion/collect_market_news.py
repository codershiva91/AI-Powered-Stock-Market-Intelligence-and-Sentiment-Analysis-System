import pandas as pd
import mariadb
import time
import traceback

from gnews import GNews
from datetime import datetime

# ====================
# Database Connection
# ====================

conn = mariadb.connect(
    host="localhost",
    user="root",
    password="@MariaDB123",
    database="stock_market_analytics"
)

cursor = conn.cursor()

# ====================
# Google News
# ====================

google_news = GNews(
    language="en",
    country="IN",
    max_results=100
)

# ====================
# Load Keywords
# ====================

keywords = pd.read_csv(
    "data/raw/market_keywords.csv"
)

# ====================
# News Collection
# ====================

for keyword in keywords["keyword"]:

    print("\n" + "=" * 80)
    print(f"COLLECTING NEWS FOR: {keyword}")
    print("=" * 80)

    try:

        news = google_news.get_news(keyword)

        print(f"Total Articles Found: {len(news)}")

        for idx, article in enumerate(news, start=1):

            print("\n" + "-" * 80)
            print(f"Article #{idx}")

            # ====================
            # Extract Fields
            # ====================

            title = article.get("title", "")

            source = article.get(
                "publisher",
                {}
            ).get(
                "title",
                ""
            )

            publish_date = article.get(
                "published date",
                None
            )

            # ====================
            # Convert Date Format
            # ====================

            try:

                if publish_date:

                    publish_date = datetime.strptime(
                        publish_date,
                        "%a, %d %b %Y %H:%M:%S GMT"
                    )

            except Exception:

                publish_date = None

            # ====================
            # Article Text
            # ====================

            article_text = article.get(
                "description",
                ""
            )

            if not article_text:
                article_text = title

            print(f"TITLE : {title}")
            print(f"SOURCE: {source}")
            print(f"DATE  : {publish_date}")

            # ====================
            # Duplicate Check
            # ====================

            try:

                cursor.execute(
                    """
                    SELECT COUNT(*)
                    FROM news_articles
                    WHERE title = ?
                    """,
                    (title,)
                )

                exists = cursor.fetchone()[0]

                if exists > 0:

                    print("⚠ Duplicate skipped")

                    continue

            except Exception as e:

                print(
                    f"Duplicate Check Error: {e}"
                )

                continue

            # ====================
            # Insert Record
            # ====================

            try:

                cursor.execute(
                    """
                    INSERT INTO news_articles
                    (
                        publish_date,
                        keyword,
                        source,
                        title,
                        article_text
                    )
                    VALUES
                    (?, ?, ?, ?, ?)
                    """,
                    (
                        publish_date,
                        keyword,
                        source,
                        title,
                        article_text
                    )
                )

                print(
                    "✓ Inserted into database"
                )

            except Exception as e:

                print(
                    f"Insert Error: {e}"
                )

                traceback.print_exc()

                continue

        conn.commit()

        print(
            f"\n✓ Completed Keyword: {keyword}"
        )

        time.sleep(5)

    except Exception as e:

        print(
            f"Keyword Failed: {keyword}"
        )

        print(e)

        traceback.print_exc()

# ====================
# Close Connection
# ====================

cursor.close()
conn.close()

print("\nNEWS COLLECTION COMPLETED")