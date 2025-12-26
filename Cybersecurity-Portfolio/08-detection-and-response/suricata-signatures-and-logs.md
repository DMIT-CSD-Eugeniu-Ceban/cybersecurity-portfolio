# Suricata: Signatures, Alerts, and eve.json

## Objective
Explore how Suricata rules generate alerts and how Suricata outputs detection data into logs (including `eve.json`) to support investigation and triage.

## What I did
1. Reviewed an existing Suricata rule and identified its core components:
   - Action (e.g., `alert`)
   - Protocol (e.g., `http`, `tcp`, `udp`, `ip`)
   - Source/Destination IPs and ports
   - Direction operator (`->` or `<->`)
   - Rule options in parentheses (e.g., `msg`, `sid`, `rev`, `content`, `classtype`)
2. Triggered a rule using provided lab traffic and confirmed an alert was generated.
3. Reviewed Suricata alert outputs in:
   - `fast.log` or `alerts.log` (human-readable summaries)
   - `eve.json` (structured JSON events usable by SIEM/automation)

## Evidence (paste small excerpts)
### 1) Rule snippet (1–3 lines)
```text
<paste the rule line(s) you reviewed here>
