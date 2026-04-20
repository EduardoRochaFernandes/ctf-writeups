# Wireshark: The Basics

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 06: Network Traffic Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** In Progress

---

## Overview

The foundational Wireshark room covering interface navigation, packet capture, display filters, stream following, and the statistical views that provide the big picture before detailed investigation begins.

---

## Interface Layout

Wireshark has three primary panes:
- **Packet List** (top) — one row per packet, with time, source/destination, protocol, length, and info summary
- **Packet Details** (middle) — hierarchical breakdown of the selected packet's protocol layers
- **Packet Bytes** (bottom) — raw hex and ASCII of the selected packet

---

## Capture Filters vs Display Filters

| Type | Applied | Reversible | Syntax |
|------|---------|-----------|--------|
| Capture Filter | Before capture — packets not captured are gone | No | BPF (Berkeley Packet Filter) |
| Display Filter | On existing capture data | Yes — other packets remain | Wireshark syntax |

**Common Capture Filters (BPF):**
```
host 192.168.1.10       # Traffic to or from this IP
net 192.168.0.0/24      # Entire subnet
port 443                # HTTPS only
tcp and port 80         # HTTP
not arp                 # Exclude ARP
```

**Common Display Filters:**
```
ip.addr == 192.168.1.10
ip.src == 10.0.0.5
tcp.port == 443
http.request.method == "POST"
!(arp || dns || icmp)   # Remove noise
frame.len > 1000
```

---

## Display Filter Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal | `ip.src == 8.8.8.8` |
| `!=` | Not equal | `tcp.port != 80` |
| `contains` | Contains string (case-sensitive) | `http.host contains "evil"` |
| `matches` | Regular expression | `http.uri matches "\.php$"` |
| `&&` | Logical AND | `ip.src == x && tcp.port == 80` |
| `\|\|` | Logical OR | `tcp.port == 80 \|\| tcp.port == 443` |
| `!` | NOT | `!arp` |
| `in {}` | In list | `tcp.port in {80 443 8080}` |

---

## Following Streams

Right-click any packet → Follow → select stream type:
- **TCP Stream** — full conversation reconstructed as readable text
- **HTTP Stream** — web content, including cleartext credentials on HTTP
- **UDP Stream** — UDP conversation
- **TLS Stream** — handshake metadata (not decrypted content unless keys are loaded)

---

## Statistics Views

| Menu Path | What It Shows |
|-----------|--------------|
| Statistics → Protocol Hierarchy | All protocols present, as percentage of traffic |
| Statistics → Conversations | All communication pairs (Ethernet, IPv4, TCP, UDP tabs) |
| Statistics → Endpoints | Each unique host and its traffic volume |
| Statistics → IO Graphs | Traffic volume over time — spot beaconing patterns |
| Analyze → Expert Information | Auto-detected anomalies (retransmissions, resets, errors) |

**Starting point for every PCAP analysis:** Protocol Hierarchy for the big picture, then Conversations to identify the top talkers, then drill down with display filters.

---

## Time Display

Before analysing any PCAP: set the time display format to UTC.
`View → Time Display Format → UTC Date, as YYYY-MM-DD, and time`

Timestamp mismatch between local timezone and UTC is a consistent source of analysis errors, especially when correlating PCAP events with SIEM logs.

---

## Placeholder

Full notes and additional sections to be added upon room completion.

---

## References

- [Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- [Wireshark Documentation](https://www.wireshark.org/docs/)
