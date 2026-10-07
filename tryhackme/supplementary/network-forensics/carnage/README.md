# Carnage

**Platform:** TryHackMe
**Path:** Supplementary — completed to reinforce foundational knowledge
**Status:** Complete

---

## Key Notes

Network forensics challenge. A user opened a malicious Word document and enabled macros, which led to a payload download and command-and-control (C2) traffic. The task was to reconstruct the attack chain from a packet capture in Wireshark: the macro-driven download stage, a second-stage payload, Cobalt Strike-style C2 beaconing to several external hosts, an external IP-lookup check, and SMTP-based exfiltration. Hostnames, IPs and other room answers are intentionally not reproduced here (the platform asks users not to publish them: `[redacted]`).

Key filter learned: `dns.a == <IP>` to find which domain resolved to a specific IP.
