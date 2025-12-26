
---

## `09-automate-cybersecurity-tasks-with-python/src/allowlist_updater.py`

```python
allow_file = "data/allow_list.txt"
remove_file = "data/remove_list.txt"

with open(allow_file, "r") as file:
    allow_list = file.read().split()

with open(remove_file, "r") as file:
    remove_list = file.read().split()

for ip in remove_list:
    if ip in allow_list:
        allow_list.remove(ip)

updated_allow_list = "\n".join(allow_list)

with open(allow_file, "w") as file:
    file.write(updated_allow_list)

print("Allow list updated successfully.")

