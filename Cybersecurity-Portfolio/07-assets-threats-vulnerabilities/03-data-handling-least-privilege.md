
# Data Handling Practices — Least Privilege Review

## Objective
Analyze a data leak scenario, identify contributing issues, and recommend least-privilege control improvements aligned with strong access control practices.

## Incident summary (given)
A representative received access to a folder of internal documents. The manager forgot to unshare the folder. The representative intended to share a single file link with an external partner but accidentally shared the entire folder. The partner posted the link publicly on social media.

## Issue(s) (20–60 words)
The leak occurred due to excessive access (broad folder sharing), lack of access review/expiry, and weak sharing controls. The manager failed to revoke access after the meeting, and the representative lacked guardrails to prevent sharing a full folder externally. The process allowed sensitive content to be exposed without approval or monitoring.

## Review (NIST-aligned least privilege summary) (20–60 words)
Least privilege means users should only receive the minimum access needed to perform their role and only for the time required. Effective implementation requires controlled authorization, periodic review, and mechanisms to prevent privilege creep. Limiting access scope and duration reduces the blast radius of mistakes and insider misuse.

## Recommendation(s) — Two control enhancements
1. **Time-bound access + automatic expiry**  
   Grant access only during the meeting window or project period, with automatic revocation afterward.
2. **Granular sharing controls + external sharing restrictions**  
   Allow sharing only at the file level; restrict external sharing by default and require approval/workflow for exceptions.

## Justification (20–60 words)
Time-bound, least-privilege access would have prevented the representative from retaining broad folder permissions after the meeting. Granular sharing and external restrictions reduce accidental over-sharing and create checkpoints before sensitive data leaves the organization. Together, these controls reduce likelihood and impact of similar leaks while preserving productivity.
