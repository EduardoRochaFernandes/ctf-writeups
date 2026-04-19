# Room: Man-in-the-Middle Detection

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Network Security
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/mitmdetection

---

## What is this room about?

Covers how MitM attacks work and how to detect them — ARP poisoning, DNS spoofing, and SSL stripping — using Wireshark and network log analysis.

---

## ARP Poisoning

ARP has no authentication. Attacker sends unsolicited ARP replies claiming the gateway's IP belongs to their MAC. All traffic meant for the gateway goes to the attacker.

**Detection indicators:**
- Two different MACs claiming the same IP in ARP replies
- High frequency of gratuitous (unsolicited) ARP responses targeting the gateway IP

```
# Wireshark filters
arp.isgratuitous                    # Unsolicited ARP replies
arp.duplicate-address-detected      # Two MACs claiming same IP
```

**Rule:** the gateway can only have one MAC. Any ARP message claiming otherwise is an attack or a misconfiguration.

---

## SSL Stripping

Attacker sits between victim and server. Victim connection: HTTP port 80 (cleartext). Attacker to server: HTTPS port 443 (encrypted). Attacker reads all credentials in plaintext.

**Detection:** HTTPS-only websites generating HTTP traffic. `tcp.port == 80` for a site that should only use 443.

---

## DNS Spoofing

Attacker intercepts DNS queries and sends fake responses with a malicious IP.

**Detection:** Two DNS responses to the same query from different source IPs — one legitimate resolver, one attacker.

---

## Key Takeaways

> ARP and DNS were designed without authentication — a design decision from the 1980s that attackers still exploit today. Detecting MitM requires establishing a baseline of what's normal on the network.

---

## References

- [MITRE ATT&CK T1557 Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/)
