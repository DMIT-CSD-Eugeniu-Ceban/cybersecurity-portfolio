import re

log_file = "data/sample_auth.log"
flagged_ips = {"203.0.113.5", "198.51.100.77"}

with open(log_file, "r") as file:
    log_data = file.read()

ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
found_ips = re.findall(ip_pattern, log_data)

unique_ips = set(found_ips)

print("Extracted IP addresses:")
for ip in unique_ips:
    if ip in flagged_ips:
        print(f"{ip} - FLAGGED")
    else:
        print(ip)

