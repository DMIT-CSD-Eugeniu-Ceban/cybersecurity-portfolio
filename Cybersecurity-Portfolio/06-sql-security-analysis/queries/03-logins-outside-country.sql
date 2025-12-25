
-- Identify login attempts that did not originate from Mexico

SELECT *
FROM log_in_attempts
WHERE country NOT LIKE '%MEX%';
