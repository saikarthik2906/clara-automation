
# Clara Answers Automation Pipeline

## Overview

This project implements an automation pipeline that converts customer conversations into structured configurations for Clara AI voice agents.

The system processes **demo calls** and **onboarding calls** to generate **versioned AI agent configurations**.

The goal is to simulate Clara’s internal automation workflow:

Human conversation → Structured account data → AI voice agent configuration.

The solution follows the **zero-cost constraint** by using rule-based extraction and local processing without paid APIs.

---

## Architecture

The system is designed as a modular pipeline:

Demo Transcript
↓
Extraction Engine
↓
Account Memo (v1)
↓
Agent Prompt Generator
↓
Stored Agent Spec (v1)

When onboarding information arrives:

Onboarding Transcript
↓
Update Extraction
↓
Patch Existing Memo
↓
Generate Updated Memo (v2)
↓
Generate Updated Agent Spec (v2)
↓
Diff Generator → `changes.json`

---

## Pipeline Design

### Pipeline A – Demo Call → Preliminary Agent

Input: Demo call transcript

Steps:

1. Parse transcript
2. Extract structured account information
3. Generate **Account Memo v1**
4. Generate **Retell Agent Spec v1**
5. Store outputs in versioned folders

Output:

outputs/accounts/<account_id>/v1/

* memo.json
* agent_spec.json

---

### Pipeline B – Onboarding Call → Agent Update

Input: Onboarding transcript

Steps:

1. Extract updated operational rules
2. Apply patch to existing v1 memo
3. Generate updated **Account Memo v2**
4. Generate updated **Agent Spec v2**
5. Produce change log

Output:

outputs/accounts/<account_id>/v2/

* memo.json
* agent_spec.json

Change tracking:

outputs/accounts/<account_id>/

* changes.json

---

## Folder Structure

clara-automation/

scripts/

* extract_demo.py
* extract_onboarding.py
* apply_patch.py
* generate_prompt.py
* generate_diff.py

data/

* demo/
* onboarding/

outputs/

* accounts/

  * <account_id>/

    * v1/
    * v2/
    * changes.json

run_pipeline.py

README.md

---

## How To Run

1. Place demo transcripts inside:

data/demo/

2. Place onboarding transcripts inside:

data/onboarding/

3. Run the pipeline:

python3 run_pipeline.py

---

## Example Output

outputs/accounts/bens-electric/

v1/

* memo.json
* agent_spec.json

v2/

* memo.json
* agent_spec.json

changes.json

---

## Versioning Strategy

v1
Generated from demo call assumptions.

v2
Updated using onboarding call confirmations.

A diff file (`changes.json`) tracks all modifications.

---

## Zero Cost Design

This project follows the assignment constraints:

* No paid APIs
* No paid LLM services
* Local rule-based extraction
* JSON file storage
* Reproducible pipeline

---

## Future Improvements

With production access, the system could be extended with:

* Whisper-based automatic transcription
* LLM-powered semantic extraction
* n8n orchestration workflows
* Retell API integration for automatic agent deployment
* Monitoring dashboard for onboarding automation

---

## Summary

This project demonstrates a scalable approach to converting real-world customer conversations into deployable AI voice agents using a structured, versioned automation pipeline.
