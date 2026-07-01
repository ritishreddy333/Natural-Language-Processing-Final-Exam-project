def create_plan(goal):

    goal_lower = goal.lower()

    steps = [
        "Retrieve relevant business documents"
    ]

    # Dynamic Planning
    if "risk" in goal_lower:
        steps.append("Analyze business risks")
        steps.append("Identify high-risk evidence")
        steps.append("Generate risk mitigation strategy")

    elif "trend" in goal_lower:
        steps.append("Analyze technology trends")
        steps.append("Compare market trends")
        steps.append("Generate trend insights")

    elif "growth" in goal_lower or "expand" in goal_lower or "investment" in goal_lower:
        steps.append("Analyze growth opportunities")
        steps.append("Analyze market trends")
        steps.append("Generate growth recommendations")

    else:
        steps.append("Analyze opportunities")
        steps.append("Analyze risks")
        steps.append("Analyze market trends")
        steps.append("Generate strategic recommendations")

    steps.append("Validate recommendations")

    plan = {
        "goal": goal,
        "steps": steps
    }

    return plan


if __name__ == "__main__":

    goal = input("Enter Business Goal: ")

    plan = create_plan(goal)

    print("\nBusiness Goal:")
    print(plan["goal"])

    print("\nExecution Plan")

    for i, step in enumerate(plan["steps"], start=1):
        print(f"{i}. {step}")