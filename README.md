# AI-Powered-Stock-Market-Intelligence-and-Sentiment-Analysis-System
Key Technologies  Python | FastAPI | MariaDB | NLP | FinBERT | Sentence Transformers | LLM APIs | Qdrant | Elasticsearch | Streamlit | BeautifulSoup | Playwright | Git | Docker | REST APIs

#Project Architecture (Version 2.0) 


                                # 🏗️ Project Architecture

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
