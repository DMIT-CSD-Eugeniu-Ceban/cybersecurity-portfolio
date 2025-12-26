
approved_users = ["alice", "bob", "charlie"]
organization_hours = range(9, 18)

login_attempts = [
    {"user": "alice", "hour": 10, "os": "OS 1"},
    {"user": "bob", "hour": 20, "os": "OS 1"},
    {"user": "mallory", "hour": 11, "os": "OS 2"},
    {"user": "charlie", "hour": 14, "os": "OS 2"}
]

for attempt in login_attempts:
    if attempt["user"] not in approved_users:
        print(f"DENIED: {attempt['user']} is not approved.")
    elif attempt["hour"] not in organization_hours:
        print(f"DENIED: {attempt['user']} logged in outside business hours.")
    elif attempt["os"] == "OS 2":
        print(f"ALLOWED WITH WARNING: {attempt['user']} needs OS update.")
    else:
        print(f"ALLOWED: {attempt['user']} login successful.")
