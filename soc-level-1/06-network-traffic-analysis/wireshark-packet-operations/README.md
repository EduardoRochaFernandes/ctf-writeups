# Wireshark: Packet Operations

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 06: Network Traffic Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Advanced Wireshark capabilities: display filter functions, TCP flag analysis, ARP/DHCP/DNS attack detection, and HTTP protocol analysis. Builds on Wireshark basics to develop the analytical depth needed for real incident investigation.

---

## Display Filter Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `upper()` | Convert field to uppercase for comparison | `upper(http.server) contains "APACHE"` |
| `lower()` | Convert field to lowercase | `lower(http.host) contains "evil"` |
| `string()` | Convert non-string to string for regex | `string(frame.number) matches "[13579]$"` |

---

## TCP Flags — Decimal Values

TCP flags occupy specific bit positions in the flags byte:
```
Bit:  7    6    5    4    3    2    1    0
Flag: CWR  ECE  URG  ACK  PSH  RST  SYN  FIN
```

| Flag combination | Decimal | Filter (exact) | Filter (flexible) |
|-----------------|---------|---------------|------------------|
| SYN | 2 | `tcp.flags == 2` | `tcp.flags.syn == 1` |
| SYN-ACK | 18 | `tcp.flags == 18` | `tcp.flags.syn == 1 && tcp.flags.ack == 1` |
| ACK | 16 | `tcp.flags == 16` | `tcp.flags.ack == 1` |
| RST | 4 | `tcp.flags == 4` | `tcp.flags.reset == 1` |
| FIN | 1 | `tcp.flags == 1` | `tcp.flags.fin == 1` |
| PSH+ACK | 24 | `tcp.flags == 24` | `tcp.flags.push == 1 && tcp.flags.ack == 1` |

**Exact vs flexible:** `tcp.flags == 2` shows ONLY packets where SYN is set and all other bits are zero. `tcp.flags.syn == 1` shows all packets where the SYN bit is on, including SYN-ACK.

---

## Port Scan Detection

| Scan type | Window size | Behaviour |
|-----------|-------------|-----------|
| TCP Full Connect | >1024 | Completes SYN→SYN-ACK→ACK handshake |
| SYN Scan (half-open) | ≤1024 | Sends RST after SYN-ACK — never completes |
| UDP Scan | N/A | No handshake — sends UDP probe |

---

## ARP Attack Detection

ARP has no authentication. Any device can claim any IP belongs to any MAC. The gateway can only have one MAC — two MACs in ARP replies claiming the same IP indicates spoofing.

```
arp                                   # All ARP
arp.isgratuitous                      # Unsolicited ARP replies
arp.duplicate-address-detected        # Two MACs for same IP
arp.opcode == 1                       # ARP requests only
arp.opcode == 2                       # ARP replies only
```

**Detection method:** Filter `arp.opcode == 2` and look for multiple replies claiming the same IP from different MAC addresses. The gateway IP is usually the target.

---

## DHCP Analysis

| Filter | What it finds |
|--------|--------------|
| `dhcp.option.dhcp == 2` | DHCP Offer — who is serving IPs on this network? |
| `dhcp.option.dhcp == 3` | DHCP Request |
| `dhcp.option.dhcp == 5` | DHCP ACK — IP assignment confirmed |
| `dhcp.option.hostname contains "keyword"` | Find host by name |

**Rogue DHCP detection:** Multiple DHCP Offers for the same request from different source IPs — only one should be responding.

---

## DNS Analysis

```
dns.flags.response == 0          # Queries only
dns.flags.response == 1          # Responses only
dns.qry.name == "example.com"    # Specific domain query
dns.qry.type == 1                # A records (IPv4)
dns.qry.type == 28               # AAAA records (IPv6)
dns.resp.ttl < 60                # Suspiciously short TTL — C2 Fast Flux indicator
dns.qry.name.len > 40            # Unusually long domain name — tunnelling indicator
```

**DNS tunnelling indicators:**
- Query names containing long strings of random characters
- High query rate to a single external domain
- Subdomains with Base64 or hex-encoded data
- Total DNS query volume disproportionate to web browsing activity

---

## HTTP Analysis

```
http.request.method == "GET"            # GET requests
http.request.method == "POST"           # POST requests
http.response.code == 200               # Successful responses
http.response.code == 401               # Authentication failures
http.response.code == 404               # Not found
http.user_agent contains "sqlmap"       # SQL injection scanner
http.user_agent contains "Nmap"         # Nmap HTTP scripts
http.request.uri contains "admin"       # Admin panel access
http.request.uri contains "../"         # Path traversal attempt
data-text-lines contains "password"     # Cleartext credentials in HTTP
```

**SOC patterns:**
- Many 401s then 200 from same IP: brute force succeeded
- Many 404s from same IP in rapid succession: directory scanning
- POST to `aspnet_client/` directory: web shell activity

---

## FTP Analysis

```
ftp.request.command == "USER"     # Username sent
ftp.request.command == "PASS"     # Password sent
ftp.request.command == "RETR"     # File download
ftp.request.command == "STOR"     # File upload (exfiltration)
ftp.response.code == 230          # Login successful
ftp.response.code == 530          # Login failed — brute force indicator
```

---

## Key Takeaways

The decimal value of TCP flags becomes important the moment you need to write a precise display filter. The ARP attack detection workflow — establishing the legitimate gateway MAC, then filtering for any other MAC claiming that IP — is simple in concept but catches a sophisticated attack reliably. Pattern recognition across these protocol-level indicators is the foundation of network forensics.

---

## References

- [Wireshark TCP Analysis](https://wiki.wireshark.org/TCP_Analyze_Sequence_Numbers)
- [MITRE ATT&CK — T1557 Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/)
