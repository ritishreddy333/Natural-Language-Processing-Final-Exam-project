def recommend(decision):

    print("\nRecommendation Agent Started...")

    recommendations = []

    # ---------------- Opportunity ----------------

    if decision["best_opportunity"]:

        article = decision["best_opportunity"]

        title = article["metadata"].get("title", "Business Opportunity")

        recommendations.append({
            "priority": "High",
            "title": f"Expand: {title}",
            "recommendation": f"Invest further in initiatives related to '{title}'.",
            "reason": "This article contains the strongest business opportunity identified during analysis.",
            "expected_impact": "Increase revenue, strengthen competitive position, and accelerate business growth.",
            "risk": "Requires financial investment and execution resources.",
            "evidence": article
        })

    # ---------------- Trend ----------------

    if decision["top_trend"]:

        article = decision["top_trend"]

        title = article["metadata"].get("title", "Technology Trend")

        recommendations.append({
            "priority": "Medium",
            "title": f"Monitor Trend: {title}",
            "recommendation": f"Continue monitoring developments related to '{title}'.",
            "reason": "This topic appears repeatedly across the retrieved intelligence.",
            "expected_impact": "Maintain technology leadership and market awareness.",
            "risk": "Technology evolves rapidly.",
            "evidence": article
        })

    # ---------------- Risk ----------------

    if decision["highest_risk"]:

        article = decision["highest_risk"]

        title = article["metadata"].get("title", "Business Risk")

        recommendations.append({
            "priority": "High",
            "title": f"Mitigate Risk: {title}",
            "recommendation": f"Develop a mitigation strategy for issues highlighted in '{title}'.",
            "reason": "Potential business risks were detected in the retrieved intelligence.",
            "expected_impact": "Reduce operational and strategic risk exposure.",
            "risk": "Mitigation activities may require additional investment.",
            "evidence": article
        })

    print("Recommendation Completed.")

    return recommendations


if __name__ == "__main__":

    from agents.decision_agent import decide
    from agents.analyzer_agent import analyze
    from agents.retriever_agent import retrieve

    docs = retrieve("Latest NVIDIA AI developments")

    analysis = analyze(docs)

    decision = decide(analysis)

    recommendations = recommend(decision)

    print("\n===== STRATEGIC RECOMMENDATIONS =====")

    for i, rec in enumerate(recommendations, start=1):

        print(f"\nRecommendation {i}")
        print("-" * 40)

        print("Priority :", rec["priority"])
        print("Title :", rec["title"])
        print("Recommendation :", rec["recommendation"])
        print("Reason :", rec["reason"])
        print("Expected Impact :", rec["expected_impact"])
        print("Risk :", rec["risk"])

        print("\nEvidence:")
        print("Title :", rec["evidence"]["metadata"].get("title", "Unknown"))
        print("Source :", rec["evidence"]["metadata"].get("source", "Unknown"))
        print(rec["evidence"]["document"][:250])