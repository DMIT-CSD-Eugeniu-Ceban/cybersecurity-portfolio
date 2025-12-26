
# Incident Handler’s Journal

## Entry 1
**Date:** 2025-12-25  
**Entry #:** 1  
**Description (50–80 words):**  
A ransomware incident disrupted a healthcare clinic’s operations. Employees lost access to medical records and critical software, and a ransom note indicated files were encrypted. Initial assessment focused on understanding the attack vector (phishing attachment), scope of impact (encrypted endpoints and data), and immediate containment actions (shutdown systems, notify stakeholders). *(NIST IR: Detection & Analysis; early Containment planning.)*

**Tool(s) used:** None (scenario-based documentation)

### The 5 W’s
- **Who:** Organized ransomware group targeting healthcare/transportation
- **What:** Ransomware deployed after a phishing attachment was opened; files encrypted
- **When:** Tuesday ~9:00 a.m.
- **Where:** Clinic endpoints/network environment
- **Why:** Phishing delivered malware; lack of user verification/security controls enabled execution

**Additional notes:**  
Immediate priorities: isolate affected systems, preserve evidence, identify patient-data exposure risk, and assess backups for recovery.

---

## Entry 2
**Date:** 2025-12-25  
**Entry #:** 2  
**Description (50–80 words):**  
Performed packet analysis in Wireshark to identify source/destination IPs, protocols used during a browsing session, and DNS resolution behavior. Applied display filters to reduce noise and inspected packet layers (Frame/Ethernet/IP/TCP). Focused on isolating relevant traffic such as DNS (UDP/53) and HTTP (TCP/80) and validating communication endpoints. *(NIST IR: Detection & Analysis.)*

**Tool(s) used:** Wireshark

**Notes (3–5 bullets):**
- Used filters like `ip.addr == <IP>`, `udp.port == 53`, `tcp.port == 80`
- Validated protocol transitions DNS → TCP/HTTP
- Inspected fields like TTL, destination IP, ports, and payload text searches
- Confirmed that filters are essential for fast triage in large PCAPs

---

## Entry 3
**Date:** 2025-12-25  
**Entry #:** 3  
**Description (50–80 words):**  
Captured live traffic using tcpdump to understand interface selection, capture scope, and file-based evidence handling. Saved traffic to a PCAP for repeatable analysis and applied capture/display filters to focus on relevant protocols/hosts. Demonstrated how command-line capture supports rapid IR tasks and complements GUI-based tools like Wireshark. *(NIST IR: Detection & Analysis; evidence collection support.)*

**Tool(s) used:** tcpdump

**Notes (3–5 bullets):**
- Identified interfaces (e.g., `tcpdump -D`)
- Captured traffic and saved to file (`-w capture.pcap`)
- Used filters to narrow scope (host/port/protocol)
- Emphasized minimal capture scope to reduce noise and protect privacy

---

## Entry 4
**Date:** 2025-12-25  
**Entry #:** 4  
**Description (50–80 words):**  
Investigated a suspicious file hash using VirusTotal to determine maliciousness and extract additional indicators of compromise (IoCs). Reviewed vendor ratio, community score, and detections for consistency. Collected IoCs (hash/IP/domain/host artifacts/TTPs) and organized them using the Pyramid of Pain to understand which indicators are easiest vs. hardest for attackers to change. *(NIST IR: Detection & Analysis.)*

**Tool(s) used:** VirusTotal

### The 5 W’s (hash alert)
- **Who:** Likely malware operator delivered via phishing attachment
- **What:** Password-protected attachment executed payload; unauthorized executables created; IDS alert
- **When:** 1:11–1:20 p.m. timeline (email → open → executables → alert)
- **Where:** Employee endpoint; SOC visibility via IDS
- **Why:** Social engineering + malicious attachment enabled execution

**Additional notes:**  
Prefer blocking higher-level IoCs (domains/TTPs) when possible; hashes are useful but easy to replace.

---

## Reflections/Notes (40–60 words each)
1) **Challenging activities and why:**  
(Write 2–3 sentences)

2) **How your understanding changed:**  
(Write 2–3 sentences)

3) **Tool or concept you enjoyed most and why:**  
(Write 2–3 sentences)
