import os

from scripts.extract_demo import extract_demo_data, save_v1
from scripts.generate_prompt import generate_agent_spec
from scripts.extract_onboarding import extract_onboarding_updates
from scripts.apply_patch import apply_patch
from scripts.generate_diff import generate_diff


def process_demo(account_id, transcript_path):

    with open(transcript_path, "r") as f:
        transcript = f.read()

    memo = extract_demo_data(transcript, account_id)

    created = save_v1(account_id, memo)

    if created:
        generate_agent_spec(account_id, memo, "v1")
        print(f"Generated v1 for {account_id}")


def process_onboarding(account_id, transcript_path):

    with open(transcript_path, "r") as f:
        transcript = f.read()

    updates = extract_onboarding_updates(transcript)

    memo_v2 = apply_patch(account_id, updates)

    generate_agent_spec(account_id, memo_v2, "v2")

    generate_diff(account_id)

    print(f"Generated v2 for {account_id}")


if __name__ == "__main__":

    demo_folder = "data/demo"
    onboarding_folder = "data/onboarding"

    for file in os.listdir(demo_folder):

        if file.endswith(".txt"):

            account_id = file.replace(".txt", "")

            demo_path = f"{demo_folder}/{file}"

            process_demo(account_id, demo_path)

            onboarding_path = f"{onboarding_folder}/{file}"

            if os.path.exists(onboarding_path):

                process_onboarding(account_id, onboarding_path)