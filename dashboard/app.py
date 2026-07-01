import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
import pandas as pd
import json
from datetime import datetime
import plotly.express as px
from agents.planner_agent import create_plan
from agents.retriever_agent import retrieve
from agents.analyzer_agent import analyze
from agents.decision_agent import decide
from agents.recommendation_agent import recommend
from agents.validation_agent import validate


st.set_page_config(
    page_title="NVIDIA Strategic Intelligence Dashboard",
    layout="wide"
)


with open("data/clean_news.json", "r") as file:
    news_data = json.load(file)


    st.title(" NVIDIA Strategic Intelligence Dashboard")

st.write("AI-Powered Executive Intelligence Agent")


st.divider()

st.header(" AI CEO Agent")

goal = st.text_input(
    "Enter Business Goal",
    placeholder="Example: Expand NVIDIA enterprise AI business"
)

run_agent = st.button("Run AI CEO Agent")

if run_agent and goal:

    st.success("Business Goal Received")

    # Planner
    plan = create_plan(goal)

    st.subheader("📋 Execution Plan")

    for i, step in enumerate(plan["steps"], start=1):
        st.write(f"{i}. {step}")

    # Retriever
    documents = retrieve(goal)

    # Analyzer
    analysis = analyze(documents)

    # Decision
    decision = decide(analysis)

    # Recommendation
    recommendations = recommend(decision)

    # Validation
    validated = validate(recommendations)

    st.subheader("📊 Analysis Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Opportunities",
        len(analysis["opportunities"])
    )

    col2.metric(
        "Risks",
        len(analysis["risks"])
    )

    col3.metric(
        "Trends",
        len(analysis["trends"])
    )

    st.subheader("🎯 Strategic Recommendations")

    for rec in validated:

        st.info(
            f"""
### {rec['title']}

Priority: {rec['priority']}

Recommendation:
{rec['recommendation']}

Reason:
{rec['reason']}

Expected Impact:
{rec['expected_impact']}

Risk:
{rec['risk']}

Confidence:
{rec['confidence']}

Validation:
{rec['status']}
"""
        )



st.header("📊 Company Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Company", "NVIDIA")
col2.metric("Industry", "AI & Semiconductors")
col3.metric("Documents", len(news_data))
col4.metric("Sources", "3+")
col5.metric("Last Update", datetime.now().strftime("%Y-%m-%d"))


st.header("📰 Market Intelligence")

st.subheader("Recent News")

for article in news_data[:5]:

    st.markdown(f"### {article['title']}")

    st.caption(
        f"{article['source']} | {article['published']}"
    )

    st.write(article["summary"])

    st.markdown("---")


st.subheader("Competitor Activities")

competitors = [
    "AWS developing custom AI chips",
    "AMD expanding MI300 AI platform",
    "Intel increasing AI accelerator investments"
]

for item in competitors:
    st.write("•", item)



st.subheader("Emerging Technologies")

technologies = [
    "Agentic AI",
    "Physical AI",
    "AI Factories",
    "Confidential Computing",
    "Edge AI"
]

for tech in technologies:
    st.write("•", tech)



st.subheader("Important Company Announcements")

announcements = [
    "NVIDIA Blackwell launch",
    "RTX Spark introduction",
    "Doosan partnership",
    "HPE AI Factory expansion"
]

for item in announcements:
    st.write("•", item)





st.header("📈 Opportunity Monitor")

if run_agent and goal:

    if analysis["opportunities"]:

        for opp in analysis["opportunities"]:

            st.success(f"""
### {opp.get("title", "Business Opportunity")}

Source:
{opp.get("metadata", {}).get("source", "Unknown")}

Evidence:
{opp.get("document", "")[:250]}
""")

    else:
        st.info("No business opportunities detected.")





st.header("😊 Sentiment Analysis")

sentiment_data = pd.DataFrame({
    "Sentiment": ["Positive", "Neutral", "Negative"],
    "Count": [75, 20, 5]
})


fig = px.pie(
    sentiment_data,
    values="Count",
    names="Sentiment",
    title="News Sentiment Distribution"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Public Sentiment")

st.success("Positive sentiment dominates due to NVIDIA's AI leadership, Blackwell adoption, and sovereign AI partnerships.")



trend_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sentiment Score": [65, 70, 74, 78, 82, 88]
})

trend_chart = px.line(
    trend_data,
    x="Month",
    y="Sentiment Score",
    title="Sentiment Trend"
)

st.plotly_chart(trend_chart, use_container_width=True)



st.header("🎯 Strategic Recommendations")

recommendations = [

    {
        "recommendation": "Accelerate Agentic AI Infrastructure",
        "priority": "HIGH",
        "evidence": "Blackwell leads AgentPerf benchmark, HPE AI Factory expansion, enterprise AI adoption",
        "impact": "Revenue growth, market leadership, enterprise customer acquisition",
        "risk": "Medium"
    },

    {
        "recommendation": "Expand Sovereign AI Partnerships",
        "priority": "HIGH",
        "evidence": "UK sovereign AI initiative, France AI investments, government demand for AI factories",
        "impact": "Long-term contracts, stronger global presence, new government customers",
        "risk": "Medium"
    },

    {
        "recommendation": "Grow Physical AI Ecosystem",
        "priority": "MEDIUM",
        "evidence": "Doosan collaboration, robotics expansion, industrial automation growth",
        "impact": "New industrial customers, diversified revenue streams, competitive advantage",
        "risk": "Low"
    }

]

for rec in recommendations:

    st.info(
        f"""
Recommendation: {rec['recommendation']}

Priority: {rec['priority']}

Supporting Evidence: {rec['evidence']}

Expected Impact: {rec['impact']}

Risk Level: {rec['risk']}
"""
    )




    st.header("👔 CEO Briefing")

st.success("""
WHAT HAPPENED?

NVIDIA strengthened its AI leadership through Blackwell adoption, sovereign AI partnerships, industrial AI expansion, and continued enterprise AI infrastructure growth.


WHY DOES IT MATTER?

The global AI infrastructure market continues to expand rapidly. Governments, enterprises, and industrial organizations are increasing investments in AI factories, agentic AI systems, and sovereign AI initiatives.

Meanwhile, competitors such as AWS, AMD, and Intel are increasing investments in custom AI hardware and competing AI platforms.


WHAT SHOULD MANAGEMENT DO NEXT?

1. Accelerate deployment of Blackwell-based AI infrastructure.
2. Expand sovereign AI partnerships with governments.
3. Increase investment in industrial AI and robotics ecosystems.
4. Strengthen enterprise AI platform adoption.
5. Monitor competitive threats from AWS, AMD, and Intel.
""")



st.divider()

st.caption(
    "Strategic Intelligence Dashboard | Powered by Qwen3-8B + BGE Embeddings + ChromaDB + RAG Pipeline"
)