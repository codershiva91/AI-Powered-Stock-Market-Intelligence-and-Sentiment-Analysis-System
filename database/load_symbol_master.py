import pandas as pd
import mariadb

conn = mariadb.connect(
    host="localhost",
    user="root",
    password="@MariaDB123",
    database="stock_market_analytics"
)

cursor = conn.cursor()

df = pd.read_csv("data/raw/nifty50_constituents.csv")

print(f"Found {len(df)} symbols")

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT IGNORE INTO symbol_master
        (
            symbol,
            company_name
        )
        VALUES (?, ?)
        """,
        (
            row["Yahoo_Symbol"],
            row["Company_Name"]
        )
    )

conn.commit()

print("Nifty50 master loaded successfully")

cursor.close()
conn.close()