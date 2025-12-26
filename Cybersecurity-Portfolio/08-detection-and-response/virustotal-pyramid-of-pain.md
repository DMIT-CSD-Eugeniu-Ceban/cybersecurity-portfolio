# Suspicious File Hash Investigation (VirusTotal + Pyramid of Pain)

## Objective
Determine whether a downloaded file is malicious using VirusTotal and document associated IoCs using the Pyramid of Pain.

## Artifact
- **SHA256:** `54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b`

## Malicious verdict
**Verdict:** Malicious  
**Reasoning:** Vendor detections and community scoring indicated consistent malicious classification. Additional behavior/relations data suggested execution and network activity consistent with malware delivery via phishing attachment.

## Timeline (from alert)
- 1:11 p.m. email received with attachment  
- 1:13 p.m. user downloaded/opened file  
- 1:15 p.m. unauthorized executables created  
- 1:20 p.m. IDS alert sent to SOC

## Pyramid of Pain (selected IoCs)
- **Additional hash (MD5/SHA1):** `<paste from VirusTotal Details tab>`
- **IP address contacted:** `<paste from Relations or Behavior tab>`
- **Domain contacted:** `<paste from Relations tab with detections>`

## Notes
- Hashes are useful for exact matches but are easy for attackers to change.
- Domains/IPs can be rotated; higher-level detection should include behavioral indicators and TTPs when available.
