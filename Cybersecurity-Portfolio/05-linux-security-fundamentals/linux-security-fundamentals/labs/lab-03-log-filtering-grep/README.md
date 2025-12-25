
# Lab 03 — Log Analysis & Filtering (Linux)

## Objective
Demonstrate how Linux logs can be analyzed using command-line tools to identify errors and potentially suspicious activity.

## Scenario
System logs contain large volumes of data. A security analyst must efficiently filter logs to identify errors, failed authentication attempts, and unusual patterns using command-line tools.

## Environment
- OS: Ubuntu Linux
- Shell: bash
- Tools: `grep`, `cat`, `less`, `wc`, pipes (`|`)

## Key concepts
- Logs record system and security events
- Filtering helps reduce noise and focus on relevant data
- Pattern matching is essential for incident detection
- Command-line tools allow fast triage of large files

---

## Steps and commands

### Step 1 — Prepare a sample log file
A sample log file is used to simulate system or authentication logs.

---

### Step 2 — Search for error messages
Logs are filtered to identify error-level events.

---

### Step 3 — Identify failed login attempts
Authentication failures are filtered to detect potential brute-force attempts.

---

### Step 4 — Count suspicious events
Counting events helps assess severity and frequency.

---

### Step 5 — Filter multiple conditions
Advanced filtering is used to narrow results to the most relevant entries.

---

## Results
- Extracted error messages from logs
- Identified failed authentication attempts
- Counted suspicious events
- Demonstrated efficient log filtering using `grep`

## Security takeaway
Effective log analysis allows security teams to detect incidents early, investigate suspicious behavior, and respond before damage occurs.
