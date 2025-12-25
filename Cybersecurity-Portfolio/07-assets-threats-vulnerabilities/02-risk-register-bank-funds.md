
# Asset Inventory — Home Office Network

## Objective
Create a basic asset inventory for a home office network and classify assets by sensitivity based on the business impact of compromise.

## Scenario
A small business is operated from a home office with multiple network-connected devices. An inventory helps identify which assets store sensitive data or provide access to other assets and therefore require stronger security controls.

## Inventory
Sensitivity levels used:
- **Public**: minimal impact if exposed
- **Internal**: useful but limited impact
- **Confidential**: exposure could cause meaningful harm
- **Restricted**: exposure/alteration would cause severe harm (financial, legal, or operational)

| Asset | Network access | Owner | Location | Notes | Sensitivity |
|---|---|---|---|---|---|
| Desktop computer | Always connected (wired/wifi) | Business owner | Home office (near router) | Stores business documents, credentials, browser sessions; primary workstation | Restricted |
| Router / Wi-Fi gateway | Always connected | Business owner | Central area (near ISP connection) | Controls network access; compromise affects all devices; admin access critical | Restricted |
| External hard drive | Sometimes connected (USB/local) | Business owner | Home office | Contains backups of business data; potential PII and sensitive records | Restricted |
| Smartphone (owner) | Frequently connected (Wi-Fi/mobile) | Business owner | Mobile | Email, MFA prompts, access to accounts; high risk if lost/stolen | Confidential |
| Printer | Sometimes connected (Wi-Fi) | Business owner | Home office | May store print jobs; can leak sensitive documents if misconfigured | Internal |
| Webcam | Sometimes connected (USB/Wi-Fi) | Business owner | Home office | Privacy risk; may enable surveillance if compromised | Internal |

## Classification rationale (examples)
- **Restricted**: assets that store critical business data or control access for the environment (desktop, router, backups).
- **Confidential**: assets that can enable account takeover or expose private business communications (smartphone).
- **Internal**: assets with limited data sensitivity but still represent attack surface (printer, webcam).

## Recommended baseline controls
- Router: change default admin credentials, disable WPS, enable WPA2/WPA3, keep firmware updated
- Desktop: full disk encryption, strong passwords, automatic updates, limited admin usage
- Backups: encrypt external drive, keep offline when not backing up
- Smartphone: screen lock, remote wipe enabled, MFA protected accounts
