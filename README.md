# AI-Powered-Stock-Market-Intelligence-and-Sentiment-Analysis-System
Key Technologies  Python | FastAPI | MariaDB | NLP | FinBERT | Sentence Transformers | LLM APIs | Qdrant | Elasticsearch | Streamlit | BeautifulSoup | Playwright | Git | Docker | REST APIs

#Project Architecture (Version 2.0) 


                         #🏗️ Project Architecture

```mermaid
flowchart TD

    User([User])

    User --> Dashboard[Streamlit Dashboard]

    Dashboard --> Search[Stock Search]
    Dashboard --> Chat[AI Chat Assistant]
    Dashboard --> Market[Market Dashboard]

    Search --> LangGraph
    Chat --> LangGraph
    Market --> LangGraph

    subgraph AI Layer
        LangGraph[LangGraph Orchestration]
        LLM[Gemini / OpenAI GPT]
        RAG[Retrieval Augmented Generation]
    end

    LangGraph --> LLM
    LangGraph --> RAG

    subgraph Data Layer
        MariaDB[(MariaDB)]
        Qdrant[(Qdrant Vector DB)]
    end

    RAG --> MariaDB
    RAG --> Qdrant

    subgraph Data Processing
        ETL[Python ETL Pipeline]
        Cleaning[Data Cleaning]
        Feature[Feature Engineering]
        Validation[Data Validation]
    end

    ETL --> Cleaning
    Cleaning --> Feature
    Feature --> Validation
    Validation --> MariaDB

    subgraph Data Sources
        Finnhub[Finnhub API]
        Yahoo[Yahoo Finance]
        News[Financial News]
        Reddit[Reddit]
        Forum[Forum Discussions]
    end

    Finnhub --> ETL
    Yahoo --> ETL
    News --> Scraping
    Reddit --> Scraping
    Forum --> Scraping

    Scraping[BeautifulSoup / Playwright]

    Scraping --> NLP

    subgraph NLP Pipeline
        Preprocess[Text Preprocessing]
        Embed[Sentence Transformers]
        FinBERT[FinBERT Sentiment]
    end

    NLP --> Preprocess
    Preprocess --> Embed
    Preprocess --> FinBERT

    Embed --> Qdrant
    FinBERT --> MariaDB

    subgraph Analytics
        Technical[Technical Indicators]
        Recommendation[AI Recommendation]
    end

    MariaDB --> Technical
    MariaDB --> Recommendation
    Qdrant --> Recommendation
    LLM --> Recommendation
```

# 🚀 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | MariaDB |
| Vector Database | Qdrant |
| LLM | Gemini, OpenAI GPT |
| NLP | FinBERT, Sentence Transformers |
| Framework | LangGraph |
| Search | Semantic Search |
| Web Scraping | BeautifulSoup, Playwright |
| APIs | Finnhub, Yahoo Finance |
| Deployment | Docker |
| Version Control | Git |




# 🏗️ System Architecture

```mermaid
flowchart TB

    %% ======================
    %% User Layer
    %% ======================

    User([👤 User])

    User --> UI

    subgraph Frontend
        UI[🖥️ Streamlit Dashboard]
        Search[🔍 Stock Search]
        Chat[🤖 AI Chat Assistant]
        Dashboard[📈 Market Dashboard]
    end

    UI --> Search
    UI --> Chat
    UI --> Dashboard

    %% ======================
    %% AI Layer
    %% ======================

    Search --> LangGraph
    Chat --> LangGraph
    Dashboard --> LangGraph

    subgraph AI Orchestration
        LangGraph[🧠 LangGraph]
        LLM[Gemini / OpenAI GPT]
        RAG[RAG Engine]
    end

    LangGraph --> LLM
    LangGraph --> RAG

    %% ======================
    %% Agents
    %% ======================

    subgraph AI Agents
        StockAgent[📊 Stock Analysis Agent]
        NewsAgent[📰 News Analysis Agent]
        TechnicalAgent[📉 Technical Analysis Agent]
        Recommendation[💡 AI Recommendation Agent]
    end

    LangGraph --> StockAgent
    LangGraph --> NewsAgent
    LangGraph --> TechnicalAgent

    StockAgent --> Recommendation
    NewsAgent --> Recommendation
    TechnicalAgent --> Recommendation

    Recommendation --> LLM

    %% ======================
    %% Databases
    %% ======================

    subgraph Storage
        Maria[(MariaDB)]
        Qdrant[(Qdrant Vector DB)]
    end

    RAG --> Maria
    RAG --> Qdrant

    %% ======================
    %% ETL Pipeline
    %% ======================

    subgraph Data Pipeline

        API[Yahoo Finance API<br/>Finnhub API]

        News[Financial News]

        Reddit[Reddit]

        Forum[Market Forums]

        Scraper[BeautifulSoup + Playwright]

        ETL[Python ETL Pipeline]

        Clean[Data Cleaning]

        Validate[Data Validation]

        Feature[Feature Engineering]

    end

    API --> ETL

    News --> Scraper
    Reddit --> Scraper
    Forum --> Scraper

    Scraper --> ETL

    ETL --> Clean
    Clean --> Validate
    Validate --> Feature
    Feature --> Maria

    %% ======================
    %% NLP
    %% ======================

    subgraph NLP Pipeline

        Text[Text Preprocessing]

        Embed[Sentence Transformers]

        FinBERT[FinBERT]

    end

    Scraper --> Text

    Text --> Embed
    Text --> FinBERT

    Embed --> Qdrant

    FinBERT --> Maria

    %% ======================
    %% Analytics
    %% ======================

    subgraph Analytics

        Indicator[RSI<br/>MACD<br/>EMA<br/>SMA<br/>Bollinger Bands]

        Semantic[Semantic Search]

    end

    Maria --> Indicator

    Qdrant --> Semantic

    Semantic --> RAG

    Indicator --> Recommendation
```

#📂 Project Structure

AI-Stock-Market-Intelligence/
│
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── LICENSE
│
├── app.py                          # Streamlit entry point
│
├── config/
│   ├── config.py
│   ├── settings.py
│   └── logging_config.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── cache/
│   └── embeddings/
│
├── database/
│   ├── schema.sql
│   ├── connection.py
│   ├── mariadb.py
│   ├── qdrant_client.py
│   └── crud.py
│
├── data_collection/
│   ├── stock_data/
│   │   ├── finnhub_collector.py
│   │   ├── yahoo_collector.py
│   │   └── scheduler.py
│   │
│   ├── news_data/
│   │   ├── news_api.py
│   │   └── rss_feed.py
│   │
│   ├── scraping/
│   │   ├── reddit_scraper.py
│   │   ├── forum_scraper.py
│   │   ├── beautifulsoup_scraper.py
│   │   └── playwright_scraper.py
│   │
│   └── pipeline.py
│
├── preprocessing/
│   ├── clean_stock_data.py
│   ├── clean_news.py
│   ├── remove_duplicates.py
│   ├── text_preprocessing.py
│   └── feature_engineering.py
│
├── analytics/
│   ├── technical_indicators.py
│   ├── fundamentals.py
│   ├── market_statistics.py
│   └── recommendation_features.py
│
├── sentiment_analysis/
│   ├── finbert_model.py
│   ├── sentiment_pipeline.py
│   └── sentiment_utils.py
│
├── embeddings/
│   ├── embedding_generator.py
│   ├── sentence_transformer.py
│   └── vector_store.py
│
├── rag/
│   ├── retriever.py
│   ├── context_builder.py
│   ├── prompt_template.py
│   └── rag_pipeline.py
│
├── llm/
│   ├── gemini_client.py
│   ├── openai_client.py
│   ├── llm_router.py
│   └── market_summary.py
│
├── agents/
│   ├── langgraph_workflow.py
│   ├── stock_agent.py
│   ├── news_agent.py
│   ├── sentiment_agent.py
│   ├── recommendation_agent.py
│   └── chat_agent.py
│
├── dashboard/
│   ├── home.py
│   ├── stock_dashboard.py
│   ├── market_dashboard.py
│   ├── chatbot.py
│   ├── recommendation.py
│   └── visualization.py
│
├── utils/
│   ├── helper.py
│   ├── constants.py
│   ├── validators.py
│   ├── logger.py
│   └── scheduler.py
│
├── tests/
│   ├── test_api.py
│   ├── test_database.py
│   ├── test_sentiment.py
│   ├── test_embeddings.py
│   ├── test_rag.py
│   └── test_dashboard.py
│
├── docs/
│   ├── architecture.md
│   ├── api_documentation.md
│   ├── database_design.md
│   └── screenshots/
│
└── notebooks/
    ├── EDA.ipynb
    ├── sentiment_analysis.ipynb
    ├── embeddings.ipynb
    └── experimentation.ipynb
