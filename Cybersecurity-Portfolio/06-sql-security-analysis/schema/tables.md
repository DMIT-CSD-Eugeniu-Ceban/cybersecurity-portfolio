
# Database Schema (Logical)

## employees
| column | description |
|------|------------|
| employee_id | Unique employee identifier |
| name | Employee name |
| department | Department name |
| office | Office location |
| machine_id | Assigned machine |

## machines
| column | description |
|------|------------|
| machine_id | Unique machine identifier |
| os | Operating system |
| hostname | Device name |

## log_in_attempts
| column | description |
|------|------------|
| attempt_id | Unique login attempt |
| employee_id | Employee attempting login |
| login_date | Date of login |
| login_time | Time of login |
| success | 1 = success, 0 = failure |
| country | Country code |
