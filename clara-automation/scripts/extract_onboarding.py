import json

def extract_onboarding_updates(transcript_text):

    updates = {}

    text = transcript_text.lower()

    if "24/7" in text or "24 hours" in text:
        updates["business_hours"] = {
            "days": ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"],
            "start": "00:00",
            "end": "23:59",
            "timezone": "unknown"
        }

    if "sprinkler leak" in text:
        updates["emergency_definition"] = ["sprinkler leak"]

    if "transfer after 60 seconds" in text:
        updates["call_transfer_rules"] = {
            "timeout_seconds": 60
        }

    return updates