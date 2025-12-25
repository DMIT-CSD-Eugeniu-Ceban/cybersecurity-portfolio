
-- Identify failed login attempts that occurred after business hours (after 18:00)

SELECT *
FROM log_in_attempts
WHERE success = 0
  AND login_time > '18:00';
