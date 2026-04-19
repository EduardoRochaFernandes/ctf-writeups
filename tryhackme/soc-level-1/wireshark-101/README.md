# Room: Wireshark 101

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Network Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/wireshark

---

## What is this room about?

The foundational Wireshark room. Covers what the tool is, how packets are structured, the difference between capture and display filters, how to follow streams, and the essential statistical views that give you the big picture before you dive into individual packets.

---

## What is Wireshark?

A **packet sniffer and protocol analyser** that lets you capture and inspect every packet on a network interface. Used by analysts for network forensics, traffic analysis, malware investigation, and protocol debugging.

### Capture Limitations by Interface Type

| Interface type | What you can see by default |
|---------------|---------------------------|
| **Wired (Ethernet)** | Only your own device's traffic (switch isolates MACs) |
| **Wi-Fi (normal mode)** | Only your device's traffic |
| **Wi-Fi (monitor mode)** | All devices on the network (requires WPA3 key + 4-way handshake) |

To capture other devices' traffic on a wired network: use **port mirroring (SPAN)** on a managed switch, or connect via a **network hub** (obsolete but broadcasts to all ports).

---

## The Packet

The fundamental unit of network communication. Every packet has:
- **Header** — metadata: source/destination MAC, IP, protocol, flags
- **Payload** — the actual data being transmitted

---

## Capture Filters vs Display Filters

| | Capture Filter | Display Filter |
|--|---------------|---------------|
| **When applied** | Before capture starts | After capture, on existing data |
| **Reversible?** | No — uncaptured packets are gone | Yes — other packets stay in memory |
| **Syntax** | BPF (Berkeley Packet Filter) | Wireshark's own syntax |

### Capture Filters (BPF)
```
host 192.168.1.10        # Traffic to/from this IP
net 192.168.1.0/24       # Entire subnet
port 80                  # Port 80 only
tcp                      # TCP only
not arp                  # Exclude ARP
```

### Display Filters
```
ip.addr == 192.168.1.10      # From or to this IP
ip.src == 192.168.1.10       # Only from this IP
tcp.port == 443              # Port 443
!(arp || dns || icmp)        # Remove noise
frame.len > 1000             # Large packets
http.host contains "google"  # HTTP to Google
```

### Display Filter Operators

| Operator | Example |
|----------|---------|
| `==` | `ip.src == 8.8.8.8` |
| `!=` | `ip.src != 192.168.1.1` |
| `contains` | `http.host contains "evil"` |
| `matches` | `http.uri matches "\.php$"` |
| `&&` / `and` | `ip.src == x && tcp.port == 80` |
| `||` / `or` | `tcp.port == 80 || tcp.port == 443` |
| `!` / `not` | `!arp` |
| `in {}` | `tcp.port in {80 443 8080}` |

---

## Following Streams

Right-click any packet → **Follow** → select stream type:
- **TCP Stream** — full conversation in readable text
- **HTTP Stream** — web content including credentials sent over plain HTTP
- **UDP Stream** — UDP conversation
- **TLS Stream** — TLS metadata (not decrypted content unless you have the key)

This applies the filter `tcp.stream eq N` — all packets belonging to that session.

---

## Profiles

`Edit → Configuration Profiles` — save different column/filter/colour setups for different analysis types. Switch from the status bar bottom-right.

Pre-built profiles useful in security: DNS Analysis, HTTP Analysis, Malware Hunt.

---

## Statistics Views

| View | How to open | What it tells you |
|------|------------|------------------|
| **Protocol Hierarchy** | Statistics → Protocol Hierarchy | All protocols present with percentages |
| **Conversations** | Statistics → Conversations | All communication pairs (TCP/UDP tabs) |
| **Endpoints** | Statistics → Endpoints | Each unique host and its traffic volume |
| **IO Graphs** | Statistics → IO Graphs | Traffic over time — spot beaconing patterns |
| **Expert Information** | Analyze → Expert Information | Auto-detected anomalies (retransmissions, resets) |

---

## Coloring Rules

`View → Coloring Rules` — default colour meanings:

| Colour | Meaning |
|--------|---------|
| Light green | HTTP traffic |
| Light blue | TCP general |
| Dark blue | DNS |
| Black / red background | TCP errors (RST, bad checksum) |
| Yellow/orange | ARP and broadcast |

---

## Key Takeaways

> The Statistics views are your starting point, not your endpoint. Protocol Hierarchy and Conversations give you the big picture in seconds — then you drill down with filters.

The most important habit I developed from this room: **always set the time display to UTC before opening any PCAP**. Timestamp mismatch between your local timezone and the capture timezone is a constant source of analysis errors.

---

## References

- [Wireshark Official Docs](https://www.wireshark.org/docs/)
- [Wireshark Display Filter Reference](https://wiki.wireshark.org/DisplayFilters)
