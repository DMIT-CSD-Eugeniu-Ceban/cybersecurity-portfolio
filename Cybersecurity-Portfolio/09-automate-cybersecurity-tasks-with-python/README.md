# Automate Cybersecurity Tasks with Python

## Overview
This section demonstrates Python fundamentals applied to common security automation tasks:
- conditional logic for access decisions,
- loops for repetitive checks,
- functions for reusable detection logic,
- parsing logs and extracting indicators (e.g., IP addresses),
- updating allow lists based on remove lists (file I/O).

## Contents
- `portfolio-algorithm-file-updates.md` — portfolio write-up (scenario + explanation + algorithm summary)
- `src/allowlist_updater.py` — updates an allow list by removing IPs from a remove list
- `src/log_ip_extractor.py` — extracts IP addresses from an auth log using regex and flags suspicious IPs
- `src/login_policy_check.py` — checks example login events against user approval + business hours rules
- `data/` — sample input files (allow list, remove list, sample log)
- `evidence/` — sample output demonstrating before/after results

## How to run (local)
If you run locally:
```bash
python3 src/allowlist_updater.py --allow data/allow_list.txt --remove data/remove_list.txt --write-back
python3 src/log_ip_extractor.py --log data/sample_auth.log --flagged "203.0.113.5,198.51.100.77"
python3 src/login_policy_check.py
