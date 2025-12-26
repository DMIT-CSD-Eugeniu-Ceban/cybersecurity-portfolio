# tcpdump Capture and Filtering

## Objective
Capture live network traffic via command line, save evidence to PCAP, and apply basic filters.

## Steps performed
- Identified available interfaces (e.g., `tcpdump -D`)
- Captured traffic on a chosen interface with limited scope
- Saved capture output to file for repeatable analysis (`-w`)
- Applied protocol/port/host filters to narrow captured traffic

## Why tcpdump matters in IR
- Quick capture without GUI dependency
- Useful for servers and remote shells
- Captures can be moved into Wireshark for deeper inspection
