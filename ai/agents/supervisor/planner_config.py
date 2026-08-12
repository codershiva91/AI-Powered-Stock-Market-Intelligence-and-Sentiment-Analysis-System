"""
==============================================================================
Planner Configuration
==============================================================================

Defines mapping between query intents and execution plans.

Author : Shivam Sahu
Project: AI-Driven Stock Market Intelligence Platform
==============================================================================
"""

PLANNER_RULES = {

    "COMPARE_COMPANIES": {

        "goal": "COMPANY_ANALYSIS",

        "workflow": "company_workflow",

        "agents": [
            "query",
            "company",
            "recommendation",
            "context"
        ],

        "priority": "HIGH"
    },

    "STOCK_SENTIMENT": {

        "goal": "COMPANY_ANALYSIS",

        "workflow": "company_workflow",

        "agents": [
            "query",
            "company",
            "recommendation",
            "context"
        ],

        "priority": "HIGH"
    },

    "SECTOR_ANALYSIS": {

        "goal": "MARKET_ANALYSIS",

        "workflow": "market_workflow",

        "agents": [
            "query",
            "market",
            "context"
        ],

        "priority": "NORMAL"
    },

    "MARKET_ANALYSIS": {

        "goal": "MARKET_ANALYSIS",

        "workflow": "market_workflow",

        "agents": [
            "query",
            "market",
            "context"
        ],

        "priority": "NORMAL"
    },

    "LATEST_NEWS": {

        "goal": "NEWS_ANALYSIS",

        "workflow": "news_workflow",

        "agents": [
            "query",
            "news",
            "context"
        ],

        "priority": "NORMAL"
    },

    "GENERAL_QUERY": {

        "goal": "COMPANY_ANALYSIS",

        "workflow": "company_workflow",

        "agents": [
            "query",
            "company",
            "context"
        ],

        "priority": "NORMAL"
    }

}