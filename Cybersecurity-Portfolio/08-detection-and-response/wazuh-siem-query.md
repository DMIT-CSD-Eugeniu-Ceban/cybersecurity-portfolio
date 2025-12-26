# Wazuh SIEM: Log Search and Investigation Query

## Objective
Use Wazuh Discover searches to investigate potential security issues on a mail server by identifying failed SSH login attempts involving the `root` account.

## Dataset / context
Analyzed ingested tutorial event data containing multiple hosts and log sources. Focused investigation on:
- Host: `mailsv` (mail server)
- Log file: `/mailsv/secure.log` (authentication/authorization events)

## Steps performed
1. Verified data was ingested and searchable:
   - Time range set to **Absolute** with a wide start date.
   - Query: `*` (returned large volume of events).
2. Filtered down to the mail server:
   - Query: `host.keyword: mailsv`
3. Searched for failed SSH logins related to `root`:
   - Query: `host.keyword: mailsv AND (fail* OR failed) AND root`
4. Reviewed multiple result pages and inspected relevant fields:
   - host, log.file.path, message, timestamp, user, source IP (when present)

## Key query (evidence)
```text
host.keyword: mailsv AND (fail* OR failed) AND root
