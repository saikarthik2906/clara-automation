import json
import os

def generate_agent_spec(account_id, memo, version="v1"):

    agent = {
        "agent_name": f"{account_id}_agent",
        "voice_style": "professional",
        "version": version,
        "system_prompt": f"""
You are Clara, an AI answering agent.

Business Hours Flow:
1. Greet the caller
2. Ask purpose of call
3. Collect name and phone number
4. Route or transfer call
5. If transfer fails, apologize and assure callback
6. Ask if anything else is needed
7. Close call politely

After Hours Flow:
1. Greet caller
2. Ask purpose
3. Confirm if emergency
4. If emergency collect name, phone, and address
5. Attempt transfer
6. If transfer fails assure follow up
7. If non emergency collect request
8. Confirm follow up during business hours
9. Ask if anything else
10. Close call
""",
        "variables": {
            "business_hours": memo["business_hours"],
            "office_address": memo["office_address"],
            "emergency_definition": memo["emergency_definition"]
        }
    }

    base = f"outputs/accounts/{account_id}/{version}"
    os.makedirs(base, exist_ok=True)

    with open(f"{base}/agent_spec.json", "w") as f:
        json.dump(agent, f, indent=2)