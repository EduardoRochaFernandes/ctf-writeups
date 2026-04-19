# Room: Wireshark: Packet Operations

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Network Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/wiresharkpacketoperations

---

## What is this room about?

Goes deeper into Wireshark's analysis capabilities — advanced filtering with field functions, TCP flags and their decimal values, ARP/DHCP/DNS analysis and their respective attack patterns, and how to investigate HTTP/HTTPS/FTP in depth.

---

## Advanced Display Filter Functions

| Function | Use | Example |
|----------|-----|---------|
| `upper()` | Convert to uppercase for comparison | `upper(http.server) contains "APACHE"` |
| `lower()` | Convert to lowercase | `lower(http.server) contains "apache"` |
| `string()` | Convert non-string to string for regex | `string(frame.number) matches "[13579]$"` |

---

## TCP Flags — Bit Position and Decimal Values

```
Bit:  7    6    5    4    3    2    1    0
Flag: CWR  ECE  URG  ACK  PSH  RST  SYN  FIN
```

| Flag | Meaning | Decimal |
|------|---------|---------|
| SYN | Initiate connection | 2 |
| ACK | Acknowledge | 16 |
| SYN+ACK | Server response to SYN | 18 |
| RST | Abort connection | 4 |
| RST+ACK | Abort with acknowledgement | 20 |
| FIN | Graceful close | 1 |
| PSH+ACK | Data with push | 24 |

**Exact vs flexible filters:**
- `tcp.flags == 2` — ONLY packets where SYN is set and all other bits are 0
- `tcp.flags.syn == 1` — all packets where SYN bit is on (includes SYN-ACK, etc.)

---

## Port Scanning Detection

| Scan type | Window size | Handshake pattern |
|-----------|-------------|------------------|
| TCP Full Connect | > 1024 | Complete SYN → SYN-ACK → ACK |
| SYN Scan (half-open) | ≤ 1024 | RST sent after receiving SYN-ACK — never completes |
| UDP Scan | N/A | No handshake — pure UDP probes |

---

## ARP Analysis and Attack Detection

**ARP Spoofing / Man-in-the-Middle:**
ARP has no authentication. An attacker can respond to an ARP request claiming any IP belongs to their MAC. The victim updates their ARP cache and sends all traffic to the attacker instead of the real destination.

**Gratuitous ARP:** An unsolicited ARP reply — sent without any request. Legitimate uses exist (device announcing itself at boot), but continuous gratuitous ARPs claiming ownership of the gateway IP = poisoning in progress.

```
arp                                     # All ARP traffic
arp.opcode == 1                         # Requests only
arp.opcode == 2                         # Replies only
arp.isgratuitous                        # Gratuitous ARP
arp.duplicate-address-detected          # Two MACs claiming same IP
```

**Investigation pattern:** Filter `arp.opcode == 2` and look for multiple different MACs responding to the same IP. The gateway can only have one MAC — if you see two, someone is lying.

---

## DHCP Attack Detection

| Code | Meaning |
|------|---------|
| `dhcp.option.dhcp == 2` | DHCP Offer (who's serving IPs?) |
| `dhcp.option.dhcp == 3` | DHCP Request |
| `dhcp.option.dhcp == 5` | DHCP ACK (IP assigned) |

**DHCP Starvation:** Thousands of requests with random MACs, exhausting the IP pool. Detect: high volume of DHCP Requests in short time.
**Rogue DHCP:** Fake server responds faster than legitimate, assigns attacker-controlled gateway. Detect: multiple DHCP Offers to the same Request from different servers.

---

## DNS Analysis and Tunnelling Detection

```
dns                              # All DNS
dns.flags.response == 0          # Queries only
dns.flags.response == 1          # Responses only
dns.qry.name == "example.com"    # Specific domain
dns.qry.type == 1                # A records (IPv4)
dns.resp.ttl < 60                # Suspiciously short TTL
dns.qry.name.len > 40            # Long domain names (tunnelling)
```

**DNS Tunnelling indicators:**
- Query names much longer than typical domains
- High query rate to single destination
- Subdomains with Base64-encoded strings
- Tools: dnscat2, dns2tcp

**DNS Cache Poisoning indicators:**
- Two responses to the same query from different servers
- Very short TTL values (1–30 seconds)
- Unprompted DNS responses (no query seen first)

---

## HTTP Analysis

**Suspicious response code patterns:**
- Many 401s followed by a 200 = brute force succeeded
- Many 404s = directory scanning
- Many 405s = method probing

**Useful HTTP filters:**
```
http.request.method == "POST"           # Data submission
http.response.code == 200               # Success
http.user_agent contains "sqlmap"       # Automated SQL injection
http.request.uri contains "admin"       # Admin panel access
data-text-lines contains "password"     # Cleartext credentials
```

---

## FTP Analysis

| Code | Meaning |
|------|---------|
| 220 | Service ready |
| 230 | Login successful |
| 331 | Username valid, password needed |
| 430/530 | Login failed |

```
ftp.request.command == "USER"     # Username sent
ftp.request.command == "PASS"     # Password sent
ftp.request.command == "RETR"     # File download
ftp.request.command == "STOR"     # File upload (exfiltration)
ftp.response.code == 530          # Failed logins (brute force)
```

---

## Key Takeaways

> The decimal values of TCP flags seem like trivia until the day you need to write a display filter for exactly SYN-ACK and nothing else. Then they're critical.

The ARP poisoning detection workflow stuck with me most: establish the legitimate gateway MAC first, then filter for any ARP reply claiming that IP from a different MAC. Simple logic, catches a sophisticated attack.

---

## References

- [Wireshark TCP Analysis](https://wiki.wireshark.org/TCP_Analyze_Sequence_Numbers)
- [MITRE ATT&CK — T1557 Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/)
