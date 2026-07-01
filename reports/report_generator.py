import os


def save_report(goal, plan, analysis, validated):

    os.makedirs("reports", exist_ok=True)

    report_path = "reports/final_report.txt"

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("=" * 70 + "\n")
        file.write("AI CEO FINAL REPORT\n")
        file.write("=" * 70 + "\n\n")

        file.write(f"Business Goal:\n{goal}\n\n")

        file.write("Execution Plan\n")
        file.write("-" * 40 + "\n")

        for i, step in enumerate(plan["steps"], start=1):
            file.write(f"{i}. {step}\n")

        file.write("\n")

        file.write("Analysis Summary\n")
        file.write("-" * 40 + "\n")
        file.write(f"Documents Retrieved : {len(analysis['opportunities']) + len(analysis['risks']) + len(analysis['trends'])}\n")
        file.write(f"Opportunities : {len(analysis['opportunities'])}\n")
        file.write(f"Risks : {len(analysis['risks'])}\n")
        file.write(f"Trends : {len(analysis['trends'])}\n\n")

        file.write("=" * 70 + "\n")
        file.write("STRATEGIC RECOMMENDATIONS\n")
        file.write("=" * 70 + "\n")

        for i, rec in enumerate(validated, start=1):

            file.write(f"\nRecommendation {i}\n")
            file.write("-" * 40 + "\n")

            file.write(f"Priority : {rec['priority']}\n")
            file.write(f"Title : {rec['title']}\n")
            file.write(f"Recommendation : {rec['recommendation']}\n")
            file.write(f"Reason : {rec['reason']}\n")
            file.write(f"Expected Impact : {rec['expected_impact']}\n")
            file.write(f"Risk : {rec['risk']}\n")
            file.write(f"Confidence : {rec['confidence']}\n")
            file.write(f"Validation : {rec['status']}\n\n")

            file.write("Evidence:\n")
            file.write(rec["evidence"][:500])
            file.write("\n\n")

    print(f"\nReport saved successfully to: {report_path}")