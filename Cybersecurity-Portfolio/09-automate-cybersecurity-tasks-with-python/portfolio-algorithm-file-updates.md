

---

## `09-automate-cybersecurity-tasks-with-python/portfolio-algorithm-file-updates.md`

```md
# Portfolio Activity: Update a File Through a Python Algorithm

## Project description
This project demonstrates how Python can be used to automate the maintenance of an IP allow list in a healthcare security environment. The goal is to remove IP addresses that are no longer authorized by comparing an allow list file with a remove list file. Automating this process reduces human error and supports least-privilege access controls.

## Open the file that contains the allow list
```python
import_file = "allow_list.txt"

with open(import_file, "r") as file:
    ip_addresses = file.read()
