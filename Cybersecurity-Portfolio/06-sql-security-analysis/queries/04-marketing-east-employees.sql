-- Retrieve employees in the Marketing department located in the East building

SELECT *
FROM employees
WHERE department LIKE '%Marketing%'
  AND office LIKE 'East%';

