def validate(recommendations):

    print("\nValidation Agent Started...")

    validated = []

    for rec in recommendations:

        evidence = rec["evidence"]["document"]

        evidence_length = len(evidence)

        score = 0

        # Evidence quality
        if evidence_length > 500:
            score += 3
        elif evidence_length > 250:
            score += 2
        elif evidence_length > 100:
            score += 1

        # Priority importance
        if rec["priority"] == "High":
            score += 2
        elif rec["priority"] == "Medium":
            score += 1

        # Confidence decision
        if score >= 5:
            confidence = "High"
            status = "Validated"

        elif score >= 3:
            confidence = "Medium"
            status = "Validated"

        else:
            confidence = "Low"
            status = "Needs More Evidence"

        validated.append({

            "priority": rec["priority"],
            "title": rec["title"],
            "recommendation": rec["recommendation"],
            "reason": rec["reason"],
            "expected_impact": rec["expected_impact"],
            "risk": rec["risk"],

            "confidence": confidence,
            "status": status,

            "validation_score": score,
            "evidence_length": evidence_length,

            "evidence": evidence

        })

    print("Validation Completed.")

    return validated


if __name__ == "__main__":

    from agents.recommendation_agent import recommend
    from agents.decision_agent import decide
    from agents.analyzer_agent import analyze
    from agents.retriever_agent import retrieve

    docs = retrieve("Latest NVIDIA AI developments")

    analysis = analyze(docs)

    decision = decide(analysis)

    recommendations = recommend(decision)

    validated = validate(recommendations)

    print("\n========== FINAL VALIDATED RECOMMENDATIONS ==========")

    for i, item in enumerate(validated, start=1):

        print(f"\nRecommendation {i}")
        print("-----------------------------------")

        print("Priority :", item["priority"])
        print("Title :", item["title"])
        print("Recommendation :", item["recommendation"])
        print("Reason :", item["reason"])
        print("Expected Impact :", item["expected_impact"])
        print("Risk :", item["risk"])

        print("Validation Score :", item["validation_score"])
        print("Evidence Length :", item["evidence_length"])

        print("Validation :", item["status"])
        print("Confidence :", item["confidence"])

        print("\nSupporting Evidence:")
        print(item["evidence"][:250])