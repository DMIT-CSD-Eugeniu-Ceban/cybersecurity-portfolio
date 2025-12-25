
# Linux Security Fundamentals — Summary

## Overview
This project demonstrates practical Linux skills used in entry-level cybersecurity, SOC, and IT support roles. The labs focus on authorization, user management, and log analysis — core tasks performed by security analysts and system administrators.

Rather than documenting basic commands, this project emphasizes **security reasoning**, **least privilege**, and **incident detection workflows**.

---

## Skills demonstrated

### Linux authorization & access control
- Interpreted Linux permission strings and ownership
- Identified insecure permissions and corrected them using least privilege
- Managed file and directory access for sensitive data

### User & group management
- Created and removed users
- Managed group-based authorization
- Assigned ownership and permissions to shared resources
- Applied secure user lifecycle management practices

### Log analysis & security monitoring
- Filtered logs using `grep` and pipes
- Identified failed authentication attempts
- Detected repeated login attempts from the same IP address
- Counted and summarized suspicious events

---

## Tools & technologies
- Linux (Ubuntu)
- Bash shell
- Core utilities: `ls`, `chmod`, `chown`, `useradd`, `usermod`, `grep`, `wc`
- Text-based log analysis

---

## Security mindset
- Applied the principle of least privilege
- Treated misconfigurations as security risks
- Focused on reducing attack surface
- Approached logs from a SOC analyst perspective

---

## Relevance to cybersecurity roles
These labs reflect tasks commonly performed by:
- SOC Analyst (Tier 1)
- Junior Cybersecurity Analyst
- IT Support / System Administrator (security-aware)

They demonstrate the ability to work independently, analyze security-relevant data, and document findings clearly.

---

## Next steps
Future projects will build on these fundamentals by:
- Using SQL to detect suspicious activity in structured log data
- Analyzing malicious and phishing emails
- Expanding into incident response and alert triage scenarios
