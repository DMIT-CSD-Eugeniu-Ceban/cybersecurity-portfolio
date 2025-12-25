
-- Correlate employees, their machines, and login attempts

SELECT e.name, e.department, m.hostname, l.login_date, l.login_time, l.success
FROM employees e
INNER JOIN machines m ON e.machine_id = m.machine_id
INNER JOIN log_in_attempts l ON e.employee_id = l.employee_id;
