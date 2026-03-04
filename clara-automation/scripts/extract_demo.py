import json
import os


def extract_demo_data(transcript_text, account_id):

    memo = {
        "account_id": account_id,
        "company_name": "",
        "business_hours": {
            "days": [],
            "start": "",
            "end": "",
            "timezone": ""
        },
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": {},
        "non_emergency_routing_rules": "",
        "call_transfer_rules": {
            "timeout_seconds": "",
            "retry_count": "",
            "failure_message": ""
        },
        "integration_constraints": [],
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    text = transcript_text.lower()

    # Example rule-based extraction

    if "electric" in text:
        memo["company_name"] = "Electric Service Company"
        memo["services_supported"].append("electrical services")

    if "emergency" in text:
        memo["emergency_definition"].append("customer mentions emergency")

    if "monday" in text or "friday" in text:
        memo["business_hours"]["days"] = ["monday", "tuesday", "wednesday", "thursday", "friday"]

    if "8 am" in text or "8am" in text:
        memo["business_hours"]["start"] = "08:00"

    if "5 pm" in text or "5pm" in text:
        memo["business_hours"]["end"] = "17:00"

    if "address" not in text:
        memo["questions_or_unknowns"].append("office address not provided")

    if not memo["emergency_definition"]:
        memo["questions_or_unknowns"].append("emergency definition unclear")

    return memo


def save_v1(account_id, memo):

    base = f"outputs/accounts/{account_id}/v1"
    memo_path = f"{base}/memo.json"

    if os.path.exists(memo_path):
        print(f"v1 already exists for {account_id}, skipping")
        return False

    os.makedirs(base, exist_ok=True)

    with open(memo_path, "w") as f:
        json.dump(memo, f, indent=2)

    return True