# AI-Powered-Stock-Market-Intelligence-and-Sentiment-Analysis-System
Key Technologies  Python | FastAPI | MariaDB | NLP | FinBERT | Sentence Transformers | LLM APIs | Qdrant | Elasticsearch | Streamlit | BeautifulSoup | Playwright | Git | Docker | REST APIs

#Project Architecture (Version 2.0) 
                                   USERS 
                                       │ 
                                       ▼ 
                           Streamlit Web Dashboard 
                                       │ 
                ┌──────────────────────┼──────────────────────┐ 
                │                      │                      │ 
                ▼                      ▼                      ▼ 
        Stock Search          AI Chat Assistant       Market Dashboard 
                │                      │                      │ 
                └──────────────────────┼──────────────────────┘ 
                                       │ 
                                       ▼ 
                         LangGraph Orchestration Layer 
                                       │ 
      
┌────────────────────────────────┼──────────────────────────
───────┐ 
      │                                │                                 │ 
      ▼                                ▼                                 ▼ 
 Stock Price Analysis         News Analysis Agent           Technical Analysis Agent 
      │                                │                                 │ 
      
└────────────────────────────────┼──────────────────────────
───────┘ 
                                       │ 
                                       ▼ 
                               Large Language Model 
                             (Gemini / OpenAI GPT) 
                                       │ 
                                       ▼ 
                        AI Explanation & Recommendation 
                                       ▲ 
                                       │ 
                    Retrieval-Augmented Generation (RAG) 
                                       │ 
                     ┌─────────────────┴─────────────────┐ 
                     ▼                                   ▼ 
             Qdrant Vector Database              MariaDB Database 
                     │                                   │ 
                     │                                   │ 
         Semantic Search                     Structured Financial Data 
                     │                                   │ 
         ┌───────────┴───────────┐           ┌───────────┴────────────┐ 
         ▼                       ▼           ▼                        ▼ 
   News Embeddings        Forum Embeddings  Stock Prices       Technical Indicators 
         ▲                       ▲           Sentiment Scores      Company Metadata 
         │                       │ 
         └───────────────┬───────┘ 
                         ▼ 
                Sentence Transformer 
             (all-MiniLM-L6-v2 / BGE) 
                         ▲ 
                         │ 
                  Text Preprocessing 
                         ▲ 
      ┌──────────────────┼───────────────────┐ 
      │                  │                   │ 
      ▼                  ▼                   ▼ 
 Financial News      Reddit Posts      Forum Discussions 
                         ▲ 
                         │ 
                 Web Scraping (BS4) 
                         │ 
      ┌──────────────────┼───────────────────┐ 
      ▼                  ▼                   ▼ 
 Yahoo Finance      News API/Finnhub      NSE/BSE Sources 
                         ▲ 
                         │ 
                 Python ETL Pipeline 
                         │ 
      ┌──────────────────┼───────────────────┐ 
      ▼                  ▼                   ▼ 
Data Validation     Feature Engineering   Data Cleaning 
                         │ 
                         ▼ 
              Technical Indicator Engine 
      (RSI, MACD, EMA, SMA, Bollinger Bands) 
                         │ 
                         ▼ 
                  FinBERT Sentiment Model 
                         │ 
                         ▼ 
                  Storage Layer (MariaDB)
