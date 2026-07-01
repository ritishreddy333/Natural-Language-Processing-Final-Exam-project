def calculate_score(text, keywords):

    score = 0

    text = text.lower()

    for word, weight in keywords.items():

        if word in text:
            score += weight

    return score


def decide(analysis):

    print("\nDecision Agent Started...")

    opportunity_keywords = {
        "investment":3,
    "partnership":3,
    "growth":2,
    "market":2,
    "expansion":2,
    "enterprise":2,
    "business":2,
    "infrastructure":2,
    "blackwell":3,
    "ai":2,
    "factory":2
    }

    risk_keywords = {
        "risk": 3,
        "competition": 3,
        "regulation": 3,
        "challenge": 2,
        "shortage": 2
    }

    trend_keywords = {
        "ai": 3,
        "agentic": 3,
        "technology": 2,
        "factory": 2,
        "infrastructure": 2
    }

    best_opportunity = None
    best_opportunity_score = -1

    for doc in analysis["opportunities"]:

        score = calculate_score(doc["document"], opportunity_keywords)

        if score > best_opportunity_score:
            best_opportunity_score = score
            best_opportunity = doc

    highest_risk = None
    highest_risk_score = -1

    for doc in analysis["risks"]:

        score = calculate_score(doc["document"], risk_keywords)

        if score > highest_risk_score:
            highest_risk_score = score
            highest_risk = doc

    top_trend = None
    top_trend_score = -1

    for doc in analysis["trends"]:

        score = calculate_score(doc["document"], trend_keywords)

        if score > top_trend_score:
            top_trend_score = score
            top_trend = doc

    decision = {
        "best_opportunity": best_opportunity,
        "highest_risk": highest_risk,
        "top_trend": top_trend,
        "opportunity_score": best_opportunity_score,
        "risk_score": highest_risk_score,
        "trend_score": top_trend_score
    }

    print("Decision Completed.")

    return decision


if __name__ == "__main__":

    from agents.retriever_agent import retrieve
    from agents.analyzer_agent import analyze

    docs = retrieve("Latest NVIDIA AI developments")

    analysis = analyze(docs)

    decision = decide(analysis)

    print("\n========== DECISION ==========")

    if decision["best_opportunity"]:

        print("\nBest Opportunity")
        print("Score :", decision["opportunity_score"])
        print(decision["best_opportunity"]["document"][:200])

    if decision["highest_risk"]:

        print("\nHighest Risk")
        print("Score :", decision["risk_score"])
        print(decision["highest_risk"]["document"][:200])

    if decision["top_trend"]:

        print("\nTop Trend")
        print("Score :", decision["trend_score"])
        print(decision["top_trend"]["document"][:200])