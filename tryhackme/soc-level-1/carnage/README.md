# Room: Carnage

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Network Security
**Difficulty:** Medium
**Type:** Challenge
**Cost:** Free
**Room Link:** https://tryhackme.com/room/c2carnage

---

## What is this room about?

A real-world network forensics challenge. Eric Fischer from the Purchasing Department at Bartell Ltd received an email with a Word document, opened it, and clicked "Enable Content." The SOC received an alert about suspicious outbound connections from his workstation. Your job: analyse the provided PCAP file and reconstruct the entire attack chain.

**Tools required:** Wireshark, VirusTotal, knowledge of HTTP, DNS, TLS, and SMTP analysis.

---

## Initial Setup

Before starting any PCAP analysis, fix the time display:
`Edit → Preferences → Columns → Time → UTC date, as YYYY-MM-DD, and time → OK`

This ensures timestamps match the questions exactly. UTC timestamps in PCAPs are a constant source of confusion when your local system is in a different timezone.

---

## Investigation Results

| # | Question | Answer | Method |
|---|----------|--------|--------|
| 1 | First HTTP connection to malicious IP | `2021-09-24 16:44:38` | Filter `http` → sort by time → first entry |
| 2 | Name of ZIP downloaded | `documents.zip` | Same frame → `http.request.uri` field |
| 3 | Domain hosting the ZIP | `attirenepal.com` | Same frame → `http.host` field |
| 4 | File inside the ZIP | `chart-1530076591.xls` | Follow TCP Stream on frame 1 |
| 5 | Web server name | `LiteSpeed` | Same TCP Stream → `Server:` response header |
| 6 | Web server version | `PHP/7.2.34` | Same TCP Stream → `X-Powered-By:` header |
| 7 | 3 domains with malicious files | `finejewels.com.au`, `thietbiagt.com`, `new.americold.com` | Filter DNS in 16:45:11–16:45:30 window |
| 8 | Certificate Authority of first domain | `GoDaddy` | `tls.handshake.type == 11` → Certificate → issuer commonName |
| 9 | Two Cobalt Strike C2 IPs | `185.106.96.158`, `185.125.204.174` | Statistics → Conversations → TCP → high packet count → confirm on VirusTotal |
| 10 | Host header of first CS IP | `ocsp.verisign.com` | Filter `ip.addr == 185.106.96.158 && http` → Follow HTTP Stream |
| 11 | Domain of first CS IP | `survmeter.live` | Filter `dns.a == 185.106.96.158` |
| 12 | Domain of second CS IP | `securitybusinpuff.com` | Filter `dns.a == 185.125.204.174` |
| 13 | Post-infection C2 domain | `maldivehost.net` | Filter `http.request.method == "POST"` → `http.host` |
| 14 | First 11 chars sent to C2 | `LIisQRWZI9` | Filter on maldivehost.net → Follow HTTP Stream → red (client) data |
| 15 | Length of first packet to C2 | `281` | Same POST filter → Length column |
| 16 | Server header of C2 domain | `Apache/2.4.49 (cPanel)...` | Follow HTTP Stream on maldivehost.net response |
| 17 | Timestamp of DNS API check | `2021-09-24 17:00:04` | Filter `ip.addr == 10.9.23.102 && dns && frame contains "api"` |
| 18 | Domain of DNS API check | `api.ipify.org` | Follow UDP Stream on above packet |
| 19 | First MAIL FROM address | `farshin@mailfa.com` | Filter `smtp.req.parameter contains "FROM"` |
| 20 | Total SMTP packets | `1439` | Filter `smtp` → check "Displayed" count in status bar |

---

## New Wireshark Filters Learned in This Challenge

| Filter | What it finds |
|--------|--------------|
| `dns.a == IP` | Domain name that resolved to a specific IP |
| `dns && frame.time >= "..." && frame.time <= "..."` | DNS traffic in a specific time window |
| `frame contains "string"` | Global search across all packet content |
| `smtp.req.parameter contains "FROM"` | SMTP MAIL FROM addresses |
| `http.request.method == "POST"` | C2 post-infection traffic |
| `ip.addr == X && dns && frame contains "api"` | DNS queries to IP-checking APIs (malware self-identification) |

---

## Attack Chain Reconstruction

```
1. Phishing email delivered → Eric opens Word document → clicks "Enable Content"
2. Macro executes → downloads documents.zip from attirenepal.com
3. ZIP contains chart-1530076591.xls — a malicious Excel file
4. Excel macro fetches additional payloads from 3 domains
5. Cobalt Strike implant establishes C2 to survmeter.live and securitybusinpuff.com
6. Malware checks external IP via api.ipify.org (operator situational awareness)
7. Starts sending POST data to maldivehost.net (data collection/exfiltration)
8. SMTP activity observed — possible lateral phishing or data exfiltration via email
```

---

## Key Takeaways

> A PCAP is a complete record of everything that happened on the wire. Every step of the attack is in there — your job is to find the thread and pull it.

The technique of using `Statistics → Conversations → TCP` sorted by packet count to find C2 servers is something I'll use in every future network forensics investigation. High packet count to an unknown external IP is almost always worth investigating.

---

## References

- [MITRE ATT&CK — T1071 Application Layer Protocol](https://attack.mitre.org/techniques/T1071/)
- [VirusTotal](https://www.virustotal.com/)
- [Cobalt Strike — Red Canary Threat Detection Report](https://redcanary.com/threat-detection-report/threats/cobalt-strike/)
