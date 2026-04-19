# Room: Network Traffic Basics

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Network Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/networktrafficbasics

---

## What is this room about?

Network Traffic Analysis (NTA) is the process of capturing, inspecting, and analysing network traffic as it flows — in real time or from recorded captures — to gain complete visibility into what's happening inside and outside a network.

---

## Why NTA Goes Beyond Logs

Logs capture selected fields — source IP, destination IP, port, status code. They never capture the full packet. NTA with full packet capture gives you everything:

| Layer | What logs miss | What NTA sees |
|-------|---------------|---------------|
| **Application** | The payload content (e.g. what's inside that HTTP POST) | Full HTTP body, credentials, file contents |
| **Transport** | Sequence numbers (key for session hijacking detection) | TCP sequence numbers, flags, window size |
| **Network** | Fragment offset (key for fragmentation attacks) | Full IP header including TTL, fragmentation |
| **Link** | ARP cache poisoning details | Full ARP frames |

---

## Traffic Flow Types

- **North-South**: Traffic crossing the network perimeter (in from internet, out to internet). Heavily monitored.
- **East-West**: Traffic staying inside the network between internal systems. Often less monitored — but critical for detecting **lateral movement** after an initial compromise.

---

## Capture Methods

| Method | How | Performance impact |
|--------|-----|--------------------|
| **Network TAP** | Physical device spliced inline — copies electrical/optical signals | Near zero |
| **Port Mirroring (SPAN)** | Switch duplicates traffic from one port to another | Can degrade switch performance at high volume |
| **Full Packet Capture** | Record every packet to PCAP file | High storage requirement |
| **NetFlow / IPFIX** | Metadata only (IPs, ports, bytes, duration) | Low — no payload |

---

## NetFlow vs IPFIX

Both are flow-based protocols that capture metadata without the full packet:

- **NetFlow** — created by Cisco. Useful for detecting C2 traffic patterns, exfiltration, lateral movement at scale
- **IPFIX** — IETF standard, successor to NetFlow. Vendor-neutral, more flexible field selection

When you can't store full PCAPs (too much volume), flow data gives you the "who talked to whom, for how long, and how much data" picture.

---

## Key Takeaways

> Logs tell you that something happened. Packets tell you exactly what it was.

Understanding NTA fundamentals is essential for working with Wireshark, Suricata, Zeek, or any network-based detection tool. The OSI model isn't just exam theory — it directly maps to what data you can and can't see at each layer.

---

## References

- [Wireshark](https://www.wireshark.org/)
- [MITRE ATT&CK — T1040 Network Sniffing](https://attack.mitre.org/techniques/T1040/)
