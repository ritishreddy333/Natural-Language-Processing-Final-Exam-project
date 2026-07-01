from agents.planner_agent import create_plan
from agents.retriever_agent import retrieve
from agents.analyzer_agent import analyze
from agents.decision_agent import decide
from agents.recommendation_agent import recommend
from agents.validation_agent import validate

from reports.report_generator import save_report


def run_agent(goal):

    print("=" * 70)
    print("AI CEO AGENT")
    print("=" * 70)

    # Step 1: Planning
    plan = create_plan(goal)

    print("\nEXECUTION PLAN")
    print("-" * 40)

    for i, step in enumerate(plan["steps"], start=1):
        print(f"{i}. {step}")

    # Step 2: Retrieve Documents
    documents = retrieve(goal)

    # Step 3: Analyze Documents
    analysis = analyze(documents)

    # Step 4: Make Decisions
    decision = decide(analysis)

    # Step 5: Generate Recommendations
    recommendations = recommend(decision)

    # Step 6: Validate Recommendations
    validated = validate(recommendations)

    print("\n")
    print("=" * 70)
    print("FINAL CEO REPORT")
    print("=" * 70)

    print("\nBusiness Goal:")
    print(goal)

    print("\nExecution Summary")
    print("-" * 40)

    print(f"Documents Retrieved : {len(documents)}")
    print(f"Opportunities Found : {len(analysis['opportunities'])}")
    print(f"Risks Found : {len(analysis['risks'])}")
    print(f"Trends Found : {len(analysis['trends'])}")
    print(f"Recommendations Generated : {len(validated)}")

    for i, rec in enumerate(validated, start=1):

        print("\n")
        print(f"Recommendation {i}")
        print("-" * 40)

        print("Priority :", rec["priority"])
        print("Title :", rec["title"])
        print("Recommendation :", rec["recommendation"])
        print("Reason :", rec["reason"])
        print("Expected Impact :", rec["expected_impact"])
        print("Risk :", rec["risk"])
        print("Confidence :", rec["confidence"])
        print("Validation :", rec["status"])

        print("\nSupporting Evidence:")
        print(rec["evidence"][:300])

    # Step 7: Save Report
    save_report(
        goal,
        plan,
        analysis,
        validated
    )

    print("\n" + "=" * 70)
    print("AI CEO AGENT EXECUTION COMPLETED")
    print("=" * 70)


if __name__ == "__main__":

    goal = input("Enter Business Goal: ")

    run_agent(goal)