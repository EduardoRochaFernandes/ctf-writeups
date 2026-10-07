# Man-in-the-Middle Detection

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 07: Network Security Monitoring
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Man-in-the-Middle attacks allow an attacker to intercept, read, and modify traffic between two parties. This room covers three MitM variants — ARP poisoning, SSL stripping, and DNS spoofing — and the Wireshark-based techniques for detecting each.

---

## ARP Poisoning

ARP has no authentication. An attacker broadcasts unsolicited ARP replies claiming the gateway's IP belongs to their MAC address. Every device that receives this reply updates its ARP cache, routing all traffic through the attacker.

**Detection:**
- Two different MACs in ARP replies claiming the same IP
- High frequency of gratuitous (unsolicited) ARP responses for the gateway IP

```
arp.isgratuitous                        # Unsolicited ARP replies
arp.duplicate-address-detected          # Two MACs for same IP
arp.opcode == 2                         # All ARP replies

# Confirm: the gateway can only have one MAC
# Filter for gateway IP and count distinct source MACs in ARP replies
```

**Investigation process:**
1. Identify the gateway IP (from DHCP ACK or the first Received header in network captures)
2. Filter ARP replies claiming ownership of that IP
3. Count distinct source MAC addresses — if more than one, poisoning is in progress
4. Identify the attacker's MAC and locate their IP through DHCP records or other ARP entries

---

## SSL Stripping

The attacker downscales the victim's HTTPS connection to HTTP:
- Victim → Attacker: HTTP (cleartext) — all credentials readable
- Attacker → Server: HTTPS (encrypted) — normal TLS session

**Detection:**
```
# HTTPS site communicating over HTTP port 80
http && ip.dst == SUSPECTED_ATTACKER && tcp.port == 80

# The attacker maintains HTTPS to the server
tls.handshake.type == 1 && ip.src == SUSPECTED_ATTACKER
```

---

## DNS Spoofing / Cache Poisoning

The attacker intercepts DNS queries and responds before the legitimate resolver, pointing the victim to a malicious IP.

**Detection:**
- Two DNS responses to the same query from different source IPs
- DNS responses appearing without a preceding query visible in the capture
- Very short TTL values (1-30 seconds) — keep cache poisoned

```
dns.flags.response == 1    # All DNS responses
# Filter for the targeted domain and look for multiple responses from different IPs
dns.qry.name == "target.example.com" && dns.flags.response == 1
```

---

## Key Takeaways

All three attacks exploit protocols designed without authentication. The detection in each case relies on the same principle: establishing what the legitimate behaviour looks like (one MAC per IP for ARP, one DNS response per query from the authorised resolver, HTTPS traffic on port 443) and alerting on deviations. This baseline-and-deviation approach generalises to almost every network-level detection scenario.
