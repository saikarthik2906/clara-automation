import json
from jsondiff import diff

def generate_diff(account_id):

    with open(f"outputs/accounts/{account_id}/v1/memo.json") as f:
        v1 = json.load(f)

    with open(f"outputs/accounts/{account_id}/v2/memo.json") as f:
        v2 = json.load(f)

    changes = diff(v1, v2)

    with open(f"outputs/accounts/{account_id}/changes.json", "w") as f:
        json.dump(changes, f, indent=2)

    return changes