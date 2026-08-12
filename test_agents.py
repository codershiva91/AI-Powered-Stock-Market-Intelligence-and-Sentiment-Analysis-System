from ai.agents.news_agent import NewsAgent
from ai.agents.stock_agent import StockAgent
from ai.agents.market_agent import MarketAgent
from ai.agents.portfolio_agent import PortfolioAgent


print("=" * 60)
print("Testing NewsAgent")
print("=" * 60)
print(NewsAgent().run("Latest news about TCS"))


print("=" * 60)
print("Testing StockAgent")
print("=" * 60)
print(StockAgent().run("Should I buy Reliance?"))


print("=" * 60)
print("Testing MarketAgent")
print("=" * 60)
print(MarketAgent().run("How is NIFTY 50 today?"))


print("=" * 60)
print("Testing PortfolioAgent")
print("=" * 60)
print(PortfolioAgent().run("Review my investment portfolio"))