
# Linux Security Fundamentals

## Overview
This repository demonstrates practical Linux skills used in entry-level cybersecurity, SOC, and security-aware IT roles.  
The focus is on **access control**, **user management**, and **log analysis** — core tasks performed during daily security operations.

Rather than listing basic Linux commands, this project emphasizes:
- Security reasoning
- Least privilege
- Detection of suspicious activity
- Clear documentation of findings

---

## Labs included

### Lab 01 — File Permissions & Authorization
- Reviewed Linux file and directory permissions
- Identified insecure permission configurations
- Corrected permissions using least privilege
- Verified changes using `ls -la` and `stat`

📁 `labs/lab-01-file-permissions/`

---

### Lab 02 — User & Group Management
- Created and removed users
- Managed group-based authorization
- Assigned ownership and permissions to shared resources
- Demonstrated secure user lifecycle management

📁 `labs/lab-02-user-group-management/`

---

### Lab 03 — Log Analysis & Filtering
- Analyzed authentication-style logs
- Filtered failed login attempts using `grep`
- Identified repeated login attempts from the same IP
- Counted suspicious events to assess severity

📁 `labs/lab-03-log-analysis-grep/`

---

## Tools & technologies
- Linux (Ubuntu)
- Bash shell
- Core utilities:
  - `ls`, `chmod`, `chown`
  - `useradd`, `usermod`, `userdel`
  - `grep`, `wc`
- Text-based log analysis

---

## Security principles applied
- Principle of least privilege
- Authorization through permissions and groups
- Reduction of attack surface
- Log-based detection and triage

---

## Intended audience
This project is relevant for:
- SOC Analyst (Tier 1)
- Junior Cybersecurity Analyst
- IT Support / System Administrator (security-focused)

---

## Notes
All examples are educational and use controlled sample data.  
The goal is to demonstrate understanding of Linux security concepts and analyst workflows.

---

## Project summary
A high-level summary of skills and outcomes is available in:

📄 `summary.md`
