# Botium Toys – Internal Security Audit (Practice Project)

## Scope and Objectives
- **Scope:** Entire security program at Botium Toys, including employee devices, internal network, on-premises systems, and data storage.
- **Objectives:**
  - Identify missing or weak security controls
  - Review compliance posture for PCI DSS and GDPR
  - Recommend improvements to reduce risk and potential regulatory fines

## Key Risks Identified
- All employees can access internally stored data and potentially cardholder data and customers' PII/SPII.
- No encryption on locally stored credit card information.
- No least-privilege or separation-of-duties access controls.
- No intrusion detection system (IDS).
- No disaster recovery plans and no backups of critical data.
- Weak password policy and no centralized password management system.
- Legacy systems are maintained, but without a clear schedule or process.

## Existing Controls
- Firewall with defined security rules
- Antivirus software installed and monitored
- Physical security: locks, CCTV, and fire detection/prevention systems
- GDPR breach-notification process and privacy procedures in place

## Recommendations (High Level)
- Implement role-based access control (RBAC) and least-privilege.
- Encrypt payment data and sensitive customer information.
- Deploy an IDS/IPS solution to monitor network traffic.
- Design and test disaster recovery and backup procedures.
- Update password policy to meet modern complexity standards and enforce via password management tools.
- Define a maintenance schedule and documented procedures for legacy systems.
