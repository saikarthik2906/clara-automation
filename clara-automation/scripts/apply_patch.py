import json
import os

def apply_patch(account_id, updates):

    v1_path = f"outputs/accounts/{account_id}/v1/memo.json"

    with open(v1_path) as f:
        memo = json.load(f)

    for key, value in updates.items():
        memo[key] = value

    base = f"outputs/accounts/{account_id}/v2"
    os.makedirs(base, exist_ok=True)

    with open(f"{base}/memo.json", "w") as f:
        json.dump(memo, f, indent=2)

    return memo