# Wireshark: Traffic Analysis

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 06: Network Traffic Analysis
**Difficulty:** Medium
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Applied Wireshark analysis for real attack scenario investigation: TLS/SNI analysis, SSL stripping detection, ICMP tunnelling, Log4Shell exploitation, beaconing detection, and data exfiltration identification.

---

## TLS Analysis Without Decryption

Even without decrypting TLS traffic, the handshake reveals valuable intelligence.

**TLS Handshake Message Types:**

| Type | Meaning |
|------|---------|
| 1 — Client Hello | Contains SNI (Server Name Indication) — the target domain in plaintext |
| 2 — Server Hello | Server chooses cipher suite |
| 11 — Certificate | Server sends certificate with full subject info, issuer, validity period |
| 20 — Finished | Handshake complete — encrypted data begins |

**SNI** is available in the Client Hello in plaintext, even in encrypted sessions. It tells you the domain the client intended to reach.

```
tls.handshake.type == 1                              # Client Hello
tls.handshake.type == 11                             # Certificate
tls.handshake.extensions_server_name == "domain"     # SNI lookup
x509sat.uTF8String contains "keyword"               # Certificate field search
```

**Suspicious certificate indicators:**
- Self-signed certificate on a domain that should have a CA
- Certificate valid for hours or days (typical C2 infrastructure)
- Certificate subject does not match the SNI
- Certificate from an unknown or recently created CA

---

## SSL Stripping Detection

The attacker sits between victim and server:
- Victim ↔ Attacker: HTTP port 80 — attacker reads everything
- Attacker ↔ Server: HTTPS port 443 — normally encrypted

Victim appears to have a secure session; attacker has full cleartext visibility.

**Detection:**
```
# HTTPS-only site generating HTTP traffic = stripping in progress
http && ip.dst == SUSPECTED_ATTACKER && tcp.port == 80

# Compare: legitimate connection should be port 443
tcp.port == 443

# Verify attacker maintains HTTPS to server
tls.handshake.type == 1
```

---

## ICMP Tunnelling Detection

ICMP (ping protocol) is rarely blocked. Normal ICMP Echo payloads are 8-64 bytes. Tunnelling inflates the payload.

```
icmp                       # All ICMP
icmp.type == 8             # Echo Request (ping sent)
icmp.type == 0             # Echo Reply
data.len > 64 and icmp     # Oversized payload — tunnelling indicator
```

**Note:** `data.len` is the payload length only, excluding headers. The `Length` column in Wireshark includes headers. Use `data.len` for tunnelling detection.

**Tools producing this pattern:** ptunnel, icmptunnel, icmpsh.

---

## Log4Shell (CVE-2021-44228) Detection

Critical RCE vulnerability in the Apache Log4j Java logging library. The attacker embeds a JNDI lookup string in any input field that Log4j logs. Log4j processes the log entry and executes the lookup, fetching and running attacker-controlled code.

```
# Attack begins with POST
http.request.method == "POST"

# JNDI is the signature — appears in any field (URL, headers, body)
(frame contains "jndi") or (frame contains "Exploit")

# Payload often in User-Agent
http.user_agent contains "${"

# Decode Base64 payloads found in the frame
echo "encoded_string==" | base64 -d
```

The filter `(frame contains "jndi") or (frame contains "Exploit")` is the most comprehensive — it catches the initial injection payload and the subsequent response containing the malicious class file.

---

## Beaconing Detection

Malware maintains contact with its C2 server at regular intervals — "checking in" to receive instructions. The regularity of this communication is the detection indicator.

**Detection approach:**
1. `Statistics → IO Graphs` — look for regular spikes at fixed intervals
2. `Statistics → Conversations` — find sessions with unusually high packet counts to external IPs
3. Filter on the suspicious IP and examine timestamps manually

```
ip.dst == SUSPECTED_C2_IP    # Isolate potential C2 traffic
```

A pattern of regular connections every 30, 60, or 300 seconds to the same external IP, even during off-hours, is a strong beaconing indicator.

---

## Data Exfiltration Channels

| Channel | Key Indicator | Detection Filter |
|---------|--------------|-----------------|
| DNS Tunnelling | Long query names, high query rate | `dns.qry.name.len > 40` |
| ICMP Tunnelling | Payload >64 bytes | `data.len > 64 and icmp` |
| HTTP POST | Large POST to external IP | `http.request.method == "POST"` |
| FTP Upload | STOR command to external | `ftp.request.command == "STOR"` |
| HTTPS to cloud | Large upload to known cloud provider | `tls.handshake.extensions_server_name` |

---

## Key Takeaways

The SNI field in TLS Client Hello is one of the most underutilised intelligence sources in encrypted traffic analysis. It reveals the intended destination domain in plaintext, allowing classification of encrypted connections without decryption. Checking SNI against threat intelligence feeds as part of network monitoring adds detection coverage across all TLS traffic.

---

## References

- [CVE-2021-44228 Log4Shell](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)
- [MITRE ATT&CK — T1572 Protocol Tunneling](https://attack.mitre.org/techniques/T1572/)
- [Wireshark TLS Analysis](https://wiki.wireshark.org/TLS)
