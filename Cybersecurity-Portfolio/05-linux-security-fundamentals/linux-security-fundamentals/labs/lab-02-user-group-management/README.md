# Lab 02 — User & Group Management (Linux)

## Objective
Demonstrate how Linux users and groups are managed to control access to system resources, following the principle of least privilege.

## Scenario
A new employee joins the organization and requires limited access to shared resources. My task is to:
- Create a user
- Create a group
- Assign group membership
- Adjust file ownership
- Remove the user when access is no longer required

## Environment
- OS: Ubuntu Linux
- Shell: bash
- Tools: `useradd`, `groupadd`, `usermod`, `chown`, `id`, `getent`

## Key concepts
- Users represent identities (authentication)
- Groups simplify access control (authorization)
- Ownership determines who can modify files
- Least privilege reduces security risk

---

## Steps and commands

### Step 1 — Create a new group
A dedicated group is created to manage access to shared resources.

Command:
- `sudo groupadd audit_team`

Expected outcome:
- Group exists in the system.

---

### Step 2 — Create a new user
A new user is added for a temporary employee.

Command:
- `sudo useradd -m analyst_temp`

Explanation:
- `-m` creates a home directory for the user.

---

### Step 3 — Add user to the group
The user is added to the appropriate group to grant controlled access.

Command:
- `sudo usermod -aG audit_team analyst_temp`

Verification:
- `id analyst_temp`

---

### Step 4 — Assign file ownership to the group
A shared directory is assigned to the group so members can access it.

Commands:
- `mkdir audit_reports`
- `sudo chown :audit_team audit_reports`
- `chmod 770 audit_reports`

Rationale:
- Only the owner and group can access the directory.
- No access is granted to others.

---

### Step 5 — Remove the user
Once access is no longer required, the user is removed from the system.

Command:
- `sudo userdel -r analyst_temp`

Explanation:
- `-r` removes the home directory and user files.

---

## Results
- Created and managed users and groups
- Assigned group-based access to resources
- Enforced least privilege
- Removed unused accounts to reduce attack surface

## Security takeaway
Inactive or over-privileged accounts are a common security risk. Proper user lifecycle management is essential for maintaining a secure Linux environment.

