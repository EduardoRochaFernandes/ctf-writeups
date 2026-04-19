# Room: Wireshark: Traffic Analysis

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Network Security
**Difficulty:** Medium
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/wiresharktrafficanalysis

---

## What is this room about?

The most advanced of the Wireshark rooms — applying everything learned in 101 and Packet Operations to real attack scenario analysis. Covers TLS inspection, ICMP tunnelling, HTTP attack detection (including Log4Shell), SSL stripping, beaconing patterns, and exfiltration detection.

---

## TLS/SSL Analysis

Even without decrypting TLS traffic, you can extract valuable information from the handshake:

| Handshake type | Meaning |
|----------------|---------|
| 1 — Client Hello | Contains SNI (Server Name Indication) — the domain in plaintext |
| 2 — Server Hello | Negotiated cipher suite |
| 11 — Certificate | Server's digital certificate with full subject info |
| 14 — Server Hello Done | Handshake parameters complete |
| 20 — Finished | Encryption begins |

**SNI is gold for analysts** — it tells you exactly which domain was requested, even in encrypted traffic.

```
tls.handshake.type == 1                          # Client Hello
tls.handshake.type == 11                         # Certificate
tls.handshake.extensions_server_name == "evil.com"  # SNI lookup
x509sat.uTF8String contains "keyword"            # Certificate field search
```

**Suspicious certificate indicators:**
- Self-signed certificate on a domain that should have a CA
- Certificate valid for only hours or days (typical C2 infrastructure)
- Certificate CN doesn't match the SNI the client requested
- Certificate from an unknown or suspicious CA

---

## SSL Stripping Attack

The attacker sits between the victim and the server:
- Victim ↔ Attacker: **HTTP (port 80) — unencrypted, attacker sees everything**
- Attacker ↔ Server: **HTTPS (port 443) — attacker forwards securely**

The victim sees a padlock (the attacker has a valid HTTPS session) but their own connection is unencrypted.

```
# 1. See the legitimate TLS handshake (attacker → server)
tls.handshake.type == 1

# 2. Find the unencrypted victim connection (proof of stripping)
http && ip.src == VICTIM_IP && ip.dst == ATTACKER_IP

# 3. Check port — should be 443; port 80 for HTTPS-only sites = stripping
tcp.port == 80
```

---

## ICMP Tunnelling Detection

ICMP (the ping protocol) is rarely blocked by firewalls — making it a viable data exfiltration channel. Normal ICMP Echo Request/Reply payloads are tiny (8–64 bytes). Tunnelling inflates the payload.

```
icmp                       # All ICMP
icmp.type == 8             # Echo Request (ping sent)
icmp.type == 0             # Echo Reply
data.len > 64 and icmp     # Oversized payload = tunnelling indicator
```

**Detection pattern:** `data.len` (payload only, excluding headers) > 64 bytes consistently + communication only with one external IP + tools like ptunnel or icmptunnel generating distinctive patterns.

---

## Log4Shell (CVE-2021-44228) Detection

One of the most severe vulnerabilities ever discovered — in Log4j, a Java logging library used by thousands of applications. The attacker sends a JNDI lookup string in any input field (URL, header, form) that Log4j logs. Log4j processes the log entry and executes the payload.

```
# Attack starts with POST
http.request.method == "POST"

# JNDI is the signature of the payload
(frame contains "jndi") or (frame contains "Exploit")

# Payload often in User-Agent header
(http.user_agent contains "$") or (http.user_agent contains "==")
```

The most effective filter: `(frame contains "jndi") or (frame contains "Exploit")` — catches both the initial request and the malicious response containing the downloaded payload.

To decode a Base64 command found in the payload: `echo "base64string==" | base64 -d`

---

## Beaconing Detection

Malware on a compromised host communicates with its C2 server at regular intervals — "phoning home" to receive instructions. The regularity is the tell.

**Detection approach:**
1. `Statistics → Conversations` — look for sessions with unusually high packet counts to external IPs
2. `Statistics → IO Graphs` — look for regular peaks in traffic at fixed intervals (every 30s, every 60s)
3. Filter on the suspicious IP and examine timestamps — regular spacing confirms beaconing

```
ip.dst == SUSPICIOUS_EXTERNAL_IP    # Isolate potential C2 traffic
```

---

## Data Exfiltration Channels

| Channel | Indicator | Key filter |
|---------|-----------|-----------|
| DNS Tunnelling | Long query names, high frequency | `dns.qry.name.len > 40` |
| ICMP Tunnelling | Large payloads | `data.len > 64 and icmp` |
| HTTP POST | Large outbound POST to unknown IP | `http.request.method == "POST"` |
| FTP STOR | File upload to external | `ftp.request.command == "STOR"` |
| SMB to exterior | SMB outside LAN | `smb2 && ip.dst != 192.168.0.0/16` |

---

## Key Takeaways

> The SNI field in TLS Client Hello is one of the most useful pieces of intelligence in encrypted traffic. It tells you the destination domain in plaintext — always check it when investigating HTTPS connections.

The Log4Shell analysis was the most impactful part of this room. Understanding how a logging library becomes a remote code execution vector — and how a single Wireshark filter can expose the attack in a PCAP — makes abstract CVE severity scores feel very concrete.

---

## References

- [Log4Shell CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)
- [MITRE ATT&CK — T1572 Protocol Tunneling](https://attack.mitre.org/techniques/T1572/)
- [Wireshark TLS Analysis](https://wiki.wireshark.org/TLS)
