# Room: Offensive Security Intro

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SOC Fundamentals
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/offensivesecurityintro

---

## What is this room about?

A brief introduction to offensive security and why blue teamers need to understand it. Includes a hands-on exercise hacking a fake bank website using Gobuster.

---

## Why Blue Teamers Need Offensive Knowledge

Understanding how attackers think is fundamental to defending against them. If you don't know what directory enumeration looks like from the attacker's side, you'll struggle to detect it from the defender's side.

---

## The Hands-On Exercise

Target: a fictional bank (FakeBank). Tool: **Gobuster**.

```bash
gobuster dir -u http://fakebank.thm -w /usr/share/wordlists/dirb/common.txt
```

Gobuster brute-forces directory names from a wordlist, discovering hidden paths not linked from the main site.

**What you find:** `/bank-transfer` — a page accessible directly but not publicly linked. Classic security through obscurity — hiding something rather than securing it. Always fails eventually.

---

## What This Looks Like in SOC Logs

A Gobuster scan against your web server produces:
- Hundreds of 404 responses in rapid succession
- Requests for common directory names (admin, login, backup, etc.)
- Same source IP, same User-Agent, all within seconds
- Occasional 200 or 302 when a valid path is found

Detection: high 404 rate from single IP in a short window.

---

## Key Takeaways

> Every vulnerability a penetration tester finds is one a real attacker could find first. The difference is intent and permission.

---

## References

- [Gobuster GitHub](https://github.com/OJ/gobuster)
- [MITRE ATT&CK T1083 File and Directory Discovery](https://attack.mitre.org/techniques/T1083/)
