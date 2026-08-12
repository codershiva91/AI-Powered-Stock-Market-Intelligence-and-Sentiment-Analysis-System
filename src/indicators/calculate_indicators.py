import pandas as pd
import mariadb
import ta


# ======================
# Database Connection
# ======================

conn = mariadb.connect(
    host="localhost",
    user="root",
    password="@MariaDB123",
    database="stock_market_analytics"
)

cursor = conn.cursor()

# ======================
# Get Symbols
# ======================

cursor.execute(
    """
    SELECT DISTINCT symbol
    FROM stock_prices
    """
)

symbols = [row[0] for row in cursor.fetchall()]

print(f"Found {len(symbols)} symbols")

# ======================
# Calculate Indicators
# ======================

for symbol in symbols:

    print(f"Processing {symbol}")

    query = f"""
    SELECT
        trade_date,
        close_price
    FROM stock_prices
    WHERE symbol='{symbol}'
    ORDER BY trade_date
    """

    df = pd.read_sql(query, conn)

    if len(df) < 50:
        continue

    # ======================
    # Moving Averages
    # ======================

    df["sma_20"] = ta.trend.sma_indicator(
        df["close_price"],
        window=20
    )

    df["sma_50"] = ta.trend.sma_indicator(
        df["close_price"],
        window=50
    )

    df["ema_20"] = ta.trend.ema_indicator(
        df["close_price"],
        window=20
    )

    # ======================
    # RSI
    # ======================

    df["rsi_14"] = ta.momentum.rsi(
        df["close_price"],
        window=14
    )

    # ======================
    # MACD
    # ======================

    macd = ta.trend.MACD(
        df["close_price"]
    )

    df["macd"] = macd.macd()

    df["macd_signal"] = macd.macd_signal()

    # ======================
    # Bollinger Bands
    # ======================

    bb = ta.volatility.BollingerBands(
        df["close_price"],
        window=20
    )

    df["bb_upper"] = bb.bollinger_hband()

    df["bb_lower"] = bb.bollinger_lband()

    # ======================
    # Save to Database
    # ======================

    for _, row in df.iterrows():

        if pd.isna(row["sma_20"]):
            continue

        cursor.execute(
            """
            INSERT IGNORE INTO technical_indicators
            (
                trade_date,
                symbol,
                sma_20,
                sma_50,
                ema_20,
                rsi_14,
                macd,
                macd_signal,
                bb_upper,
                bb_lower
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["trade_date"],
                symbol,

                None if pd.isna(row["sma_20"]) else float(row["sma_20"]),
                None if pd.isna(row["sma_50"]) else float(row["sma_50"]),
                None if pd.isna(row["ema_20"]) else float(row["ema_20"]),

                None if pd.isna(row["rsi_14"]) else float(row["rsi_14"]),

                None if pd.isna(row["macd"]) else float(row["macd"]),
                None if pd.isna(row["macd_signal"]) else float(row["macd_signal"]),

                None if pd.isna(row["bb_upper"]) else float(row["bb_upper"]),
                None if pd.isna(row["bb_lower"]) else float(row["bb_lower"])
            )
        )

    conn.commit()

    print(f"Completed {symbol}")

print("All indicators calculated")

cursor.close()
conn.close()