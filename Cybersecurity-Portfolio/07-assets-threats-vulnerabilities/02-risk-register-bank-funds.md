# Risk Register — Bank Funds (Likelihood × Impact)

## Objective
Score key risks to a commercial bank’s funds using a simple qualitative risk model and prioritize remediation focus.

## Operational environment (summary)
The bank operates with on-prem and remote employees, handles sensitive customer accounts, and is subject to strict financial regulations. Disruptions or leaks can trigger regulatory penalties, customer losses, and operational downtime.

## Risk scoring method
- Likelihood: **1 (low)**, **2 (moderate)**, **3 (high)**
- Impact/Severity: **1 (low)**, **2 (moderate)**, **3 (high)**
- Priority score: **Likelihood × Severity** → **1–9**

## Notes (40–60 words)
The bank’s funds and customer data are attractive targets due to direct financial gain. With many users handling sensitive data, both social engineering and credential compromise are realistic threats. Remote access increases exposure to phishing and account takeover. Regulatory requirements amplify impact: breaches can lead to penalties, forced disclosures, and reputational damage.

## Risk register

| Risk | Description | Likelihood (1–3) | Severity (1–3) | Priority (1–9) | Rationale (why) | Recommended controls (examples) |
|---|---|---:|---:|---:|---|---|
| Business email compromise (BEC) | Attacker impersonates exec/vendor to redirect payments | 3 | 3 | 9 | Common, targets finance workflows directly | MFA, payment verification procedures, email security (DMARC/SPF/DKIM), user training |
| Compromised user database | Credential theft leading to account takeover/fraud | 2 | 3 | 6 | Depends on controls; impact is severe | Strong hashing, access controls, monitoring, segmentation, incident response playbooks |
| Financial records leak | Exposure of sensitive financial/customer data | 2 | 3 | 6 | Likely via misconfig or phishing; regulated data | DLP, least privilege, encryption, logging/auditing, vendor controls |
| Theft (physical or insider) | Loss of funds or sensitive assets | 1 | 2 | 2 | Low crime area, but insider risk exists | Physical security, separation of duties, monitoring, approvals |
| Supply chain attack | Vendor compromise impacts banking operations | 1 | 3 | 3 | Less frequent but high impact | Vendor risk management, SBOM, patching, segmentation, contingency planning |

## Prioritization outcome
Highest immediate priority is **BEC (9)** due to high likelihood and direct financial impact. Next focus is reducing exposure to **credential compromise and data leaks (6)** through stronger access control, monitoring, and security awareness.
