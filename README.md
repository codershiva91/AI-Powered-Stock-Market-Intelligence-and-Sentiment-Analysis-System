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

