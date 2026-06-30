# 🤖 AI CEO Agent for Strategic Business Intelligence

## AI-Powered Multi-Agent Decision Support System

This project implements an **AI CEO Agent** that assists executives in making strategic business decisions using a **Multi-Agent Architecture** and **Retrieval-Augmented Generation (RAG)**.

The system collects NVIDIA-related business intelligence, retrieves relevant information using semantic search, analyzes opportunities, risks, and technology trends, generates strategic recommendations, validates them, and presents the results through an interactive Streamlit dashboard.

---

# 📌 Project Objective

Modern organizations generate enormous amounts of business information every day.

Instead of manually reading hundreds of news articles, this AI CEO Agent automatically:

- Collects business intelligence
- Retrieves relevant information
- Analyzes opportunities
- Detects business risks
- Identifies emerging technology trends
- Prioritizes findings
- Generates strategic recommendations
- Validates recommendations
- Presents executive insights through a dashboard

The project demonstrates an **Agentic AI Workflow** rather than a simple Prompt → LLM architecture.

---

# 🏗 System Architecture

```
                          USER
                            │
                            ▼
                   Business Goal
                            │
                            ▼
                    Planner Agent
                            │
              Creates Execution Plan
                            ▼
                   Retriever Agent
                            │
       ChromaDB + BGE Embeddings (RAG)
                            │
            Retrieves Relevant Documents
                            ▼
                    Analyzer Agent
          ┌────────────┬────────────┬
          │            │            │
     Opportunities    Risks      Trends
          │            │            │
          └────────────┴────────────┘
                            ▼
                    Decision Agent
                            │
          Selects Most Important Findings
                            ▼
               Recommendation Agent
                            │
        Generates Strategic Recommendations
                            ▼
                   Validation Agent
                            │
      Validates Evidence & Confidence Score
                            ▼
                 Streamlit Dashboard
                            ▼
               Executive Decision Support
```

---

# 🔄 AI Agent Workflow

The implemented workflow follows the project requirements:

```
Business Goal
      │
      ▼
Planner Agent
      │
      ▼
Retriever Agent
      │
      ▼
Analyzer Agent
      │
      ▼
Decision Agent
      │
      ▼
Recommendation Agent
      │
      ▼
Validation Agent
      │
      ▼
Executive Dashboard
```

---

# 🧠 Agent Responsibilities

## 📋 Planner Agent

Responsible for planning before execution.

Input:

- Business Goal

Output:

- Execution Plan

Example:

- Retrieve business documents
- Analyze opportunities
- Analyze risks
- Identify technology trends
- Generate recommendations
- Validate recommendations

---

## 🔍 Retriever Agent

Responsible for retrieving relevant business information.

Uses:

- ChromaDB
- Semantic Search
- Vector Embeddings

Output:

- Most relevant NVIDIA business documents

---

## 📊 Analyzer Agent

Processes retrieved documents.

Identifies:

- Business Opportunities
- Business Risks
- Technology Trends

Produces structured business intelligence.

---

## 🎯 Decision Agent

Prioritizes business intelligence.

Selects:

- Best Opportunity
- Highest Risk
- Top Technology Trend

This demonstrates autonomous decision-making.

---

## 💡 Recommendation Agent

Generates executive recommendations.

Each recommendation contains:

- Priority
- Recommendation
- Business Reason
- Expected Impact
- Risk Level
- Supporting Evidence

---

## ✅ Validation Agent

Verifies recommendation quality.

Checks:

- Evidence availability
- Confidence level
- Validation status

Only validated recommendations are presented.

---

# 📚 Retrieval-Augmented Generation (RAG)

The project implements a Retrieval-Augmented Generation pipeline.

Workflow:

```
Business Goal
        │
        ▼
Embedding Generation
        │
        ▼
Semantic Search
        │
        ▼
ChromaDB Vector Database
        │
        ▼
Relevant Documents
        │
        ▼
Analyzer Agent
        │
        ▼
Decision Agent
        │
        ▼
Recommendation Agent
```

RAG ensures recommendations are based on retrieved business evidence rather than model memory alone.

---

# 🗂 Data Pipeline

```
Business News
        │
        ▼
News Collection
        │
        ▼
Data Cleaning
        │
        ▼
JSON Dataset
        │
        ▼
Embedding Generation
        │
        ▼
ChromaDB Vector Database
        │
        ▼
Retriever Agent
        │
        ▼
Analyzer Agent
        │
        ▼
Decision Agent
        │
        ▼
Recommendation Agent
        │
        ▼
Validation Agent
        │
        ▼
Dashboard
```

---

# 📊 Dashboard Features

The Streamlit dashboard includes:

- AI CEO Agent
- Business Goal Input
- Execution Plan
- Company Overview
- Market Intelligence
- Analysis Summary
- Opportunity Monitor
- Risk Monitor
- Strategic Recommendations
- Sentiment Analysis
- CEO Briefing

---

# 🛠 Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| Dashboard | Streamlit |
| Vector Database | ChromaDB |
| Embedding Model | BGE Sentence Transformers |
| Retrieval | Retrieval-Augmented Generation (RAG) |
| Semantic Search | ChromaDB Similarity Search |
| Visualization | Plotly |
| Data Storage | JSON |

> If your project actually uses Ollama and Qwen, you can also include:
>
> **LLM:** Qwen3-8B (via Ollama)

Only include that if your code genuinely calls the model.

---

# 📁 Project Structure

```
AI_CEO_AGENT/
│
├── agents/
│   ├── planner_agent.py
│   ├── retriever_agent.py
│   ├── analyzer_agent.py
│   ├── decision_agent.py
│   ├── recommendation_agent.py
│   ├── validation_agent.py
│   └── __init__.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── clean_news.json
│   └── raw_news.json
│
├── vectordb/
│   ├── build_db.py
│   └── search.py
│
├── scraper/
│
├── main_agent.py
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 How to Run

### Clone the repository

```bash
git clone <repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Build the Vector Database

```bash
python vectordb/build_db.py
```

### Run the AI CEO Agent

```bash
python main_agent.py
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🎯 Key Features

- Multi-Agent AI Architecture
- Planning Before Execution
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- ChromaDB Vector Database
- Business Opportunity Detection
- Business Risk Analysis
- Technology Trend Detection
- Autonomous Decision Making
- Recommendation Generation
- Recommendation Validation
- Interactive Executive Dashboard

---

# 📈 Project Outcomes

The AI CEO Agent successfully demonstrates:

- Multi-Agent AI Workflow
- Planning Before Execution
- Evidence-Based Retrieval
- Strategic Business Analysis
- Autonomous Decision Making
- Recommendation Generation
- Recommendation Validation
- Executive Decision Support Dashboard

The project satisfies the required workflow:

```
Goal
   ↓
Plan
   ↓
Retrieve
   ↓
Analyze
   ↓
Decide
   ↓
Recommend
   ↓
Validate
```

which demonstrates explicit AI Agent behaviour beyond a traditional Prompt → LLM application.
