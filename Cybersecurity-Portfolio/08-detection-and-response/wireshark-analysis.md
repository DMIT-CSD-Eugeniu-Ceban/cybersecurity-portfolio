# Wireshark Packet Analysis (PCAP)

## Objective
Analyze a packet capture to identify endpoints, protocols, and key packet attributes relevant to a web browsing session.

## Workflow
1. Opened PCAP in Wireshark and reviewed packet list columns (Time, Source, Destination, Protocol, Info).
2. Applied filters to isolate traffic associated with a target IP and reviewed reduced packet set.
3. Inspected packet layers in detail: Frame → Ethernet II → IPv4 → TCP/UDP.
4. Filtered DNS traffic (`udp.port == 53`) to review query/answer behavior.
5. Filtered HTTP traffic (`tcp.port == 80`) to review endpoint communications and inspect fields like TTL and header attributes.
6. Performed payload text filtering (e.g., searching for specific strings in TCP payload).

## Key takeaways
- Display filters dramatically reduce noise and accelerate investigation.
- DNS queries and answers provide important context for which domain names resolve to which IPs.
- Reviewing protocol layers validates where information lives (MAC, IP, ports, flags, payload).
