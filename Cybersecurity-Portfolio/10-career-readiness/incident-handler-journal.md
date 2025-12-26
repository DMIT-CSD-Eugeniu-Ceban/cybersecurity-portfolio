# Incident Handler’s Journal

---

## Entry 1

**Date:** 2025-12-01  
**Entry #:** 1  

**Description:**  
Documented and analyzed a ransomware incident impacting a healthcare organization. The incident disrupted access to patient records and business operations. This entry focuses on detection, initial analysis, and understanding attacker behavior using the 5 W’s framework.

**Tool(s) Used:**  
None (scenario-based analysis)

**The 5 W’s:**
- **Who:** Organized cybercriminal group targeting healthcare organizations  
- **What:** Ransomware attack encrypting critical systems and files  
- **When:** Tuesday at approximately 9:00 a.m.  
- **Where:** Internal network and employee workstations  
- **Why:** Successful phishing email with malicious attachment enabled malware execution  

**Additional Notes:**  
This incident highlights the importance of employee phishing awareness and rapid containment procedures.

---

## Entry 2

**Date:** 2025-12-07  
**Entry #:** 2  

**Description:**  
Analyzed network traffic using Wireshark to inspect packets related to web traffic and DNS queries. This activity focused on identifying IP addresses, protocols, and packet structure during a simulated investigation.

**Tool(s) Used:**  
Wireshark

**Key Findings:**  
- Identified source and destination IP addresses  
- Inspected DNS queries and responses  
- Confirmed TCP and UDP traffic patterns  

**Additional Notes:**  
Packet filtering significantly reduces investigation time when working with large captures.

---

## Entry 3

**Date:** 2025-12-14  
**Entry #:** 3  

**Description:**  
Investigated a suspicious file hash using VirusTotal. The goal was to determine if the file was malicious and identify related indicators of compromise using the Pyramid of Pain model.

**Tool(s) Used:**  
VirusTotal

**The 5 W’s:**
- **Who:** Unknown threat actor distributing malware via phishing  
- **What:** Malicious spreadsheet executing unauthorized payloads  
- **When:** Shortly after email attachment was opened  
- **Where:** Employee workstation  
- **Why:** User executed a password-protected malicious attachment  

**Additional Notes:**  
Hash-based indicators are useful for detection but easy for attackers to change.

---

## Entry 4

**Date:** 2025-121-18  
**Entry #:** 4  

**Description:**  
Responded to a phishing alert using a predefined incident response playbook. Evaluated alert severity, verified malicious attachment, and escalated the incident according to organizational procedures.

**Tool(s) Used:**  
Incident response playbook, SHA256 hash analysis

**Key Actions Taken:**  
- Evaluated alert metadata  
- Verified attachment as malicious  
- Escalated ticket with justification  

**Additional Notes:**  
Playbooks ensure consistent and efficient incident response across teams.

---

## Reflections / Notes

- Packet analysis required careful attention to protocol layers but became easier with practice.  
- My understanding of incident detection and response improved significantly, especially regarding structured documentation.  
- Wireshark and VirusTotal were the most engaging tools due to their real-world relevance and investigative depth.
