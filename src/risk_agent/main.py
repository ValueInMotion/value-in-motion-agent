import json
from pathlib import Path

from src.risk_agent.schemas import AccountLifecycle
from src.risk_agent.agent import compute_risk

def run():
    data_path = Path(__file__).parent / "data" / "accounts.json"
    with open(data_path, "r", encoding="utf-8") as f:
        accounts = json.load(f)

    print("\n=== VALUE IN MOTION — RISK AGENT ===\n")

    for raw in accounts:
        acc = AccountLifecycle(**raw)
        result = compute_risk(acc)

        print(f"Account: {result['account']}")
        print(f"Risk: {result['risk_level']}")
        print(f"Reasons: {', '.join(result['reasons'])}")
        print(f"Action: {result['next_action']}")
        print(f"Breakdown: {result['breakdown']}")
        print("-" * 50)

if __name__ == "__main__":
    run()
