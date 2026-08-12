import math
import pymysql
import yfinance as yf
from tqdm import tqdm

from config import DB_CONFIG


def clean(value):
    """
    Convert NaN/inf to None for MariaDB
    """
    if value is None:
        return None

    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return None

    return value


connection = pymysql.connect(**DB_CONFIG)

cursor = connection.cursor()

# -----------------------------
# Read all companies
# -----------------------------

cursor.execute("""
SELECT symbol, company_name
FROM symbol_master
ORDER BY company_name;
""")

companies = cursor.fetchall()

print(f"\nFound {len(companies)} companies.\n")


sql = """
INSERT INTO company_fundamentals
(
symbol,
company_name,
market_cap,
trailing_pe,
forward_pe,
price_to_book,
trailing_eps,
forward_eps,
dividend_yield,
debt_to_equity,
current_ratio,
quick_ratio,
total_revenue,
ebitda,
operating_margin,
profit_margin,
return_on_equity,
updated_at
)

VALUES
(
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW()
)

ON DUPLICATE KEY UPDATE

company_name=VALUES(company_name),
market_cap=VALUES(market_cap),
trailing_pe=VALUES(trailing_pe),
forward_pe=VALUES(forward_pe),
price_to_book=VALUES(price_to_book),
trailing_eps=VALUES(trailing_eps),
forward_eps=VALUES(forward_eps),
dividend_yield=VALUES(dividend_yield),
debt_to_equity=VALUES(debt_to_equity),
current_ratio=VALUES(current_ratio),
quick_ratio=VALUES(quick_ratio),
total_revenue=VALUES(total_revenue),
ebitda=VALUES(ebitda),
operating_margin=VALUES(operating_margin),
profit_margin=VALUES(profit_margin),
return_on_equity=VALUES(return_on_equity),
updated_at=NOW();
"""

success = 0
failed = 0

for company in tqdm(companies):

    yahoo_symbol = company["symbol"]

    try:

        ticker = yf.Ticker(yahoo_symbol)

        info = ticker.info

        values = (

            yahoo_symbol,
            clean(info.get("longName")),

            clean(info.get("marketCap")),

            clean(info.get("trailingPE")),
            clean(info.get("forwardPE")),

            clean(info.get("priceToBook")),

            clean(info.get("trailingEps")),
            clean(info.get("forwardEps")),

            clean(info.get("dividendYield")),

            clean(info.get("debtToEquity")),

            clean(info.get("currentRatio")),
            clean(info.get("quickRatio")),

            clean(info.get("totalRevenue")),
            clean(info.get("ebitda")),

            clean(info.get("operatingMargins")),
            clean(info.get("profitMargins")),
            clean(info.get("returnOnEquity"))

        )

        cursor.execute(sql, values)

        connection.commit()

        success += 1

    except Exception as e:

        failed += 1

        print(f"\n❌ {yahoo_symbol}")
        print(e)

cursor.close()
connection.close()

print("\n==============================")
print("Fundamental ETL Completed")
print("==============================")
print(f"Successful : {success}")
print(f"Failed     : {failed}")