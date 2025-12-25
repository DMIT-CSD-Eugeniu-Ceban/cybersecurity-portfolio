-- Identify employees not in the Information Technology department

SELECT *
FROM employees
WHERE department NOT LIKE '%Information Technology%';

