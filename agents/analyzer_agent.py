def analyze(documents):

    print("\nAnalyzer Agent Started...")

    opportunities = []
    risks = []
    trends = []

    # Opportunity keywords
    opportunity_words = [
        "partnership",
        "growth",
        "expansion",
        "investment",
        "market",
        "enterprise",
        "customer",
        "business",
        "adoption",
        "revenue",
        "demand",
        "factory",
        "infrastructure",
        "collaboration",
        "launch"
    ]

    # Risk keywords
    risk_words = [
        "risk",
        "competition",
        "challenge",
        "regulation",
        "shortage",
        "cost",
        "delay",
        "security",
        "privacy",
        "supply",
        "dependency",
        "limitation"
    ]

    # Trend keywords
    trend_words = [
        "ai",
        "agentic",
        "technology",
        "factory",
        "infrastructure",
        "robotics",
        "cloud",
        "gpu",
        "enterprise",
        "automation",
        "llm",
        "generative"
    ]

    # Analyze each retrieved document
    for doc in documents:

        text = doc["document"].lower()

        if any(word in text for word in opportunity_words):
            opportunities.append(doc)

        if any(word in text for word in risk_words):
            risks.append(doc)

        if any(word in text for word in trend_words):
            trends.append(doc)

    analysis = {
        "opportunities": opportunities,
        "risks": risks,
        "trends": trends
    }

    print("Analysis Completed.")
    print("Found Opportunities:", len(opportunities))
    print("Found Risks:", len(risks))
    print("Found Trends:", len(trends))

    return analysis


if __name__ == "__main__":

    from agents.retriever_agent import retrieve

    docs = retrieve("Latest NVIDIA AI developments")

    result = analyze(docs)

    print("\n========== ANALYSIS SUMMARY ==========")

    print("Total Opportunities:", len(result["opportunities"]))
    print("Total Risks:", len(result["risks"]))
    print("Total Trends:", len(result["trends"]))

    if result["opportunities"]:
        print("\nFirst Opportunity:")
        print(result["opportunities"][0]["document"][:250])

    if result["risks"]:
        print("\nFirst Risk:")
        print(result["risks"][0]["document"][:250])

    if result["trends"]:
        print("\nFirst Trend:")
        print(result["trends"][0]["document"][:250])