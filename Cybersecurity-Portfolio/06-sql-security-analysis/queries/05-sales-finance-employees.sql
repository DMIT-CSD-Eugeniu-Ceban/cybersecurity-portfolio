
-- Retrieve employees in the Sales or Finance departments

SELECT *
FROM employees
WHERE department LIKE '%Sales%'
   OR department LIKE '%Finance%';
