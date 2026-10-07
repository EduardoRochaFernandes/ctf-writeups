# Network Traffic Basics

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 06: Network Traffic Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Network Traffic Analysis (NTA) is the process of capturing and inspecting network communications to identify anomalies, threats, and policy violations. This room establishes the foundational concepts: why NTA complements log analysis, the OSI model as a visibility framework, traffic capture methods, and the flow-based alternatives when full packet capture is not feasible.

---

## Why NTA Goes Beyond Log Analysis

Logs capture selected fields from events — IP addresses, ports, status codes, usernames. They rarely capture the actual content of network traffic. NTA with full packet capture provides everything:

| OSI Layer | What logs typically miss | What NTA reveals |
|-----------|------------------------|------------------|
| Application | HTTP body content, actual credentials submitted | Full request/response payload |
| Transport | TCP sequence numbers (needed to detect session hijacking) | Full TCP header fields |
| Network | IP fragment offsets (needed for fragmentation attacks) | Complete IP header |
| Link | ARP reply details (needed for ARP poisoning detection) | Full ARP frames |

---

## Traffic Flow Types

**North-South traffic** — crosses the network perimeter: inbound from the internet, outbound to the internet. This is the primary focus of perimeter security controls and is typically well monitored.

**East-West traffic** — stays within the network, moving between internal systems. Often less monitored than North-South. Critical for detecting lateral movement after an initial compromise — an attacker who has a foothold will use East-West traffic to reach their target systems.

---

## Capture Methods

| Method | How | Performance Impact |
|--------|-----|-------------------|
| Network TAP | Physical device spliced inline — copies signals without introducing latency | Near zero |
| Port Mirroring (SPAN) | Switch duplicates traffic from monitored ports to an analysis port | Moderate at high volume |
| Full Packet Capture | Records every packet to a PCAP file for offline analysis | High storage requirement |
| Agent-based capture | Software on endpoints captures traffic locally | Endpoint CPU overhead |

---

## Network Flow Data — NetFlow and IPFIX

When full packet capture is not feasible (high-volume networks, storage constraints), flow data provides metadata without payload:

**NetFlow** (Cisco standard):
- Source and destination IP, port, protocol
- Bytes and packets transferred
- Start and end time of the flow
- Useful for: identifying C2 beaconing patterns, exfiltration volumes, lateral movement

**IPFIX** (IETF standard, successor to NetFlow):
- Vendor-neutral, flexible field selection
- More extensible than NetFlow

Flow data cannot show you what data was transferred, but it can show you that a host transferred 500MB to an unusual external IP at 2am — which is often enough to trigger an investigation.

---

## Key Tools

| Tool | Function |
|------|---------|
| Wireshark | Graphical packet analyser — capture and inspection |
| TShark | Command-line Wireshark — scriptable, pipeline-compatible |
| Zeek | Network security monitor — generates structured logs from traffic |
| Suricata | Network IDS/IPS — signature and behavioural detection |
| NetworkMiner | Forensic PCAP analysis — extracts files, credentials, metadata |

---

## Key Takeaways

Network traffic is a second independent data source that often reveals what host-based logs cannot. A well-designed detection capability uses both: host logs for what happened inside a system, and network traffic for what passed between systems. The combination makes attack chains visible in ways that neither source alone achieves.

---

## References

- [MITRE ATT&CK — T1040 Network Sniffing](https://attack.mitre.org/techniques/T1040/)
- [Wireshark Official Documentation](https://www.wireshark.org/docs/)
- [Zeek Network Monitor](https://zeek.org/)
