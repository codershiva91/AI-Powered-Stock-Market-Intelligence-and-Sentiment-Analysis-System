# 

import os
import mariadb
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def log_etl(
    process_name,
    records_processed,
    status,
    start_time,
    remarks=""
):

    conn = mariadb.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="stock_market_analytics"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO etl_logs
        (
            process_name,
            records_processed,
            status,
            start_time,
            end_time,
            remarks
        )
        VALUES
        (?, ?, ?, ?, ?, ?)
        """,
        (
            process_name,
            records_processed,
            status,
            start_time,
            datetime.now(),
            remarks
        )
    )

    conn.commit()

    cursor.close()
    conn.close()