# Carnage

**Platform:** TryHackMe
**Path:** Supplementary — completed to reinforce foundational knowledge
**Status:** Complete

---

## Key Notes

Network forensics challenge. A user opened a malicious Word document, enabling macros, which initiated C2 connections. Analysis of `carnage.pcap` using Wireshark to reconstruct the full attack chain: macro download of documents.zip from attirenepal.com, XLS payload, connection to Cobalt Strike C2 servers (survmeter.live, securitybusinpuff.com), POST to maldivehost.net C2 channel, IP geolocation check via api.ipify.org, SMTP exfiltration. Key filter learned: `dns.a == IP` to find domain resolving to a specific IP.

---

## Placeholder

Detailed writeup can be expanded here.
