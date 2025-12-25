-- Investigate login attempts on specific dates related to a suspicious incident

SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09'
   OR login_date = '2022-05-08';

