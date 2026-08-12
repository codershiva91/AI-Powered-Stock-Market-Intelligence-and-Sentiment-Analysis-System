import pandas as pd
import mariadb
import glob
import os

conn = mariadb.connect(
    host="localhost",
    user="root",
    password="@MariaDB123",
    database="stock_market_analytics"
)

cursor = conn.cursor()

files = glob.glob("data/raw/indices/*.csv")

for file in files:

    index_name = os.path.basename(file).replace(".csv","")

    print(f"Loading {index_name}")

    df = pd.read_csv(file)

    df = df[df["Date"].notna()]

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT IGNORE INTO market_indices
            (
                trade_date,
                index_name,
                open_price,
                high_price,
                low_price,
                close_price,
                volume
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                pd.to_datetime(row["Date"]).date(),
                index_name,
                float(row["Open"]),
                float(row["High"]),
                float(row["Low"]),
                float(row["Close"]),
                int(row["Volume"]) if pd.notna(row["Volume"]) else 0
            )
        )

    conn.commit()

    print(f"Loaded {index_name}")

cursor.close()
conn.close()

print("Completed")