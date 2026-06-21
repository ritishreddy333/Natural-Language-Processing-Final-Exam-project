import ollama

prompt = """
You are the CEO Strategic Intelligence Agent for NVIDIA.

Generate exactly 3 strategic recommendations.

For EACH recommendation use this format:

========================================

RECOMMENDATION:
<recommendation>

SUPPORTING EVIDENCE:
- Evidence Source 1
- Evidence Source 2
- Evidence Source 3

EXPECTED IMPACT:
- Revenue growth
- Market differentiation
- Customer acquisition

RISK ASSESSMENT:
- Financial risk
- Operational risk
- Strategic risk

========================================

Use business language suitable for executives.
"""

response = ollama.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n")
print("=" * 60)
print("EVIDENCE-BASED RECOMMENDATIONS")
print("=" * 60)
print("\n")

print(response["message"]["content"])