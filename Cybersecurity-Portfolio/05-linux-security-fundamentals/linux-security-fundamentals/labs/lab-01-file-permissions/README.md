# Lab 01 — File Permissions & Authorization (Linux)

## Objective
Demonstrate how Linux file permissions control access (authorization), and how to detect and fix insecure permissions.

## Scenario
A shared team folder contains sensitive files. Some files/directories have overly permissive access that could allow unauthorized reading or modification. My task is to review permissions and correct them using least privilege.

## Environment
- OS: Ubuntu (WSL or VM)
- Tools: bash shell, `ls`, `chmod`, `chown`, `stat`, `umask`

## Key concepts
- Permission string: `drwxr-x---` (type + user/group/other)
- Permission classes:
  - `u` = owner (user)
  - `g` = group
  - `o` = others
- Permission bits:
  - `r` = read (4)
  - `w` = write (2)
  - `x` = execute / enter directory (1)
- Least privilege: grant only the minimum required access.

---

## Steps and commands

### Step 1 — Create a controlled lab directory and sample files
I created a directory structure to simulate a shared folder and a couple of sensitive files.

Commands:
- `mkdir -p lab01/shared`
- `cd lab01/shared`
- `echo "confidential payroll" > payroll.txt`
- `echo "ssh private key placeholder" > id_rsa.txt`
- `mkdir reports`
- `echo "Q4 report" > reports/q4.txt`

Expected outcome:
- Files and folders exist and can be listed.

---

### Step 2 — Inspect current permissions
I reviewed permissions using long listing.

Commands:
- `ls -la`
- `ls -la reports`

What I looked for:
- Any file showing `...rw-rw-rw-` or similar (world-writable/readable).
- Any directory allowing others to enter (`o+x`) when it should not.

---

### Step 3 — Introduce an intentional misconfiguration (for demonstration)
To show detection and remediation, I intentionally set insecure permissions.

Commands:
- `chmod 777 payroll.txt`
- `chmod 777 reports`

Why this is risky:
- `777` means anyone can read/write/execute (or enter) — unauthorized users could modify or steal data.

---

### Step 4 — Re-check and identify the problem
I confirmed the insecure permissions after misconfiguration.

Commands:
- `ls -la`
- `ls -la reports`

Finding:
- `payroll.txt` became world-readable and world-writable.
- `reports/` became accessible and writable by “others”.

---

### Step 5 — Fix permissions (least privilege)
I corrected permissions so only the owner can read/write sensitive files and only authorized users can access directories.

Remediation commands (example safe settings):
- Sensitive files: owner read/write only
  - `chmod 600 payroll.txt`
  - `chmod 600 id_rsa.txt`
- Directory: owner can read/write/enter; group can read/enter; others no access
  - `chmod 750 reports`

Rationale:
- `600` prevents non-owners from reading or modifying sensitive files.
- `750` keeps the directory accessible to the owner and a trusted group, but blocks everyone else.

---

### Step 6 — Verify final state
I verified permissions are corrected.

Commands:
- `ls -la`
- `ls -la reports`
- `stat payroll.txt`

Expected outcome:
- `payroll.txt` and `id_rsa.txt` show `-rw-------`
- `reports` shows `drwxr-x---`

---

## Results
- Identified insecure permissions (`777`) that would allow unauthorized access.
- Remediated using `chmod` with least privilege settings.
- Verified the final permissions using `ls -la` and `stat`.

## Notes / Security takeaway
Linux authorization is enforced at the filesystem level using owner/group/other permission bits. Regular permission reviews help prevent accidental data exposure and unauthorized modification.

