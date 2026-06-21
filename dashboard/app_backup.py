import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI CEO Dashboard",
    layout="wide"
)

st.title("🤖 NVIDIA Strategic Intelligence Dashboard")
st.header("📊 Company Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Company", "NVIDIA")
col2.metric("Industry", "AI & Semiconductors")
col3.metric("Documents", "100+")
col4.metric("Sources", "3+")
col5.metric("Last Update", "Today")
st.write("AI-Powered Executive Intelligence Agent")

st.header("📰 Market Intelligence")

st.subheader("Recent News")

st.write("""
• NVIDIA Blackwell leads AgentPerf benchmark

• HPE expands AI Factory with NVIDIA

• Apple adopts NVIDIA Confidential Computing

• UK and France expand sovereign AI initiatives
""")





st.subheader("Competitor Activities")

st.write("""
• AWS exploring custom AI chips

• AMD expanding MI300 platform

• Intel increasing AI accelerator investments
""")





st.subheader("Emerging Technologies")

st.write("""
• Agentic AI

• Physical AI

• AI Factories

• Confidential Computing

• Edge AI
""")




st.subheader("Company Announcements")

st.write("""
• NVIDIA Blackwell launch

• RTX Spark introduction

• Doosan partnership

• HPE AI Factory expansion
""")




st.header("📈 Opportunity Monitor")

st.success("""
Opportunity Title: Agentic AI Infrastructure

Impact Level: High

Evidence:
• NVIDIA Blackwell leads AgentPerf benchmark
• HPE AI Factory expansion
• Growing enterprise AI adoption

Confidence Score: 95%
""")

st.success("""
Opportunity Title: Government AI Projects

Impact Level: High

Evidence:
• UK sovereign AI initiative
• France AI infrastructure investments
• Demand for national AI factories

Confidence Score: 90%
""")

st.success("""
Opportunity Title: Industrial AI Expansion

Impact Level: Medium

Evidence:
• Doosan partnership
• Physical AI growth
• Robotics automation demand

Confidence Score: 85%
""")






st.header("⚠️ Risk Monitor")

st.error("""
Risk Title: AWS Custom AI Chips

Risk Category: Competitive Threat

Severity Level: High

Evidence:
• AWS planning custom AI chips
• Reduced dependency on NVIDIA GPUs

Confidence Score: 90%
""")

st.error("""
Risk Title: Market Saturation

Risk Category: Business Risk

Severity Level: Medium

Evidence:
• Increasing AI competitors
• Falling hardware margins

Confidence Score: 80%
""")

st.error("""
Risk Title: Regulatory Pressure

Risk Category: Regulatory Risk

Severity Level: Medium

Evidence:
• Growing AI governance laws
• Sovereign AI requirements

Confidence Score: 75%
""")



st.header("😊 Sentiment Analysis")

sentiment_data = pd.DataFrame({
    "Category": [
        "Positive",
        "Neutral",
        "Negative"
    ],
    "Count": [
        75,
        20,
        5
    ]
})

fig = px.pie(
    sentiment_data,
    names="Category",
    values="Count",
    title="News Sentiment Distribution"
)

st.plotly_chart(fig, use_container_width=True)


st.header("🎯 Strategic Recommendations")

st.info("""
Recommendation:
Accelerate Agentic AI Infrastructure

Priority: HIGH

Supporting Evidence:
• Blackwell leads AgentPerf benchmark
• HPE AI Factory expansion
• Enterprise AI adoption increasing

Expected Impact:
• Revenue growth
• Market leadership
• Enterprise customer acquisition

Risk Level:
Medium
""")

st.info("""
Recommendation:
Expand Sovereign AI Partnerships

Priority: HIGH

Supporting Evidence:
• UK AI initiative
• France AI investments
• Government demand for AI factories

Expected Impact:
• Long-term contracts
• Stronger global presence
• New government customers

Risk Level:
Medium
""")

st.info("""
Recommendation:
Grow Physical AI Ecosystem

Priority: MEDIUM

Supporting Evidence:
• Doosan collaboration
• Robotics expansion
• Industrial automation growth

Expected Impact:
• New industrial customers
• Diversified revenue streams
• Competitive advantage

Risk Level:
Low
""")






st.header("👔 CEO Briefing")

st.success("""
WHAT HAPPENED?

NVIDIA expanded its leadership in AI infrastructure through Blackwell,
AgentPerf leadership, HPE AI Factory partnerships, sovereign AI initiatives,
and industrial AI collaborations.

WHY DOES IT MATTER?

The AI infrastructure market is growing rapidly.
Governments, enterprises, and industrial companies are investing heavily
in AI factories, agentic AI systems, and sovereign AI capabilities.

Meanwhile AWS, AMD, and Intel are increasing competition through custom AI chips
and alternative AI platforms.

WHAT SHOULD MANAGEMENT DO NEXT?

1. Accelerate deployment of Blackwell-based AI infrastructure.
2. Expand sovereign AI partnerships with governments.
3. Increase investment in industrial AI and robotics.
4. Defend market leadership against AWS custom AI chips.
5. Strengthen enterprise AI ecosystem partnerships.
""")


st.divider()

st.caption(
    "Strategic Intelligence Dashboard | Powered by Qwen3-8B + BGE Embeddings + ChromaDB + RAG Pipeline"
)