import pymysql

try:
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="@MariaDB123",
        database="stock_market_analytics",
    )

    print("Connected Successfully!")

    with conn.cursor() as cur:
        cur.execute("SELECT VERSION()")
        print(cur.fetchone())

    conn.close()

except Exception as e:
    print(type(e).__name__)
    print(e)