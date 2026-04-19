# Room: Humans as Attack Vectors

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Attack Vectors
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/humansasattackvectors

---

## What is this room about?

The weakest link in any security architecture isn't the firewall or the SIEM — it's the people. This room covers the main ways attackers exploit humans rather than systems, and what defenders can do about it.

---

## Why Humans Are Targeted

A zero-day exploit takes months of research and costs a lot. A convincing phishing email takes 30 minutes. Social engineering attacks work because they bypass technical controls entirely — they exploit trust, authority, urgency, and fear instead.

---

## Phishing Attacks

The most common human attack vector. A phishing email:
- Impersonates a trusted entity (bank, Microsoft, your CEO)
- Creates urgency ("Your account will be suspended in 24 hours")
- Contains either a malicious link or an infected attachment

**Detection and prevention:** Email gateways that scan attachments and URLs, link rewriting that checks destinations at click-time, user training to spot suspicious sender addresses.

---

## Malware via Social Engineering

Fake software downloads, "codec required" pop-ups, cracked software from torrent sites — all deliver malware packaged to look legitimate. The user installs it voluntarily.

**Defence:** Application whitelisting, endpoint protection, blocking execution from user-writable directories like Downloads and Temp.

---

## Deepfakes

A growing threat as AI improves. An attacker clones a voice (sometimes from a 30-second YouTube clip) or face, then calls an employee impersonating a manager or executive and requests an urgent wire transfer or credentials.

**Real cases:** Multiple companies have lost millions to audio deepfake fraud. In 2024, a Hong Kong company transferred $25M after a video call with deepfaked executives.

**Defence:** There's no technical solution — it's purely procedural. Organisations need code words, verification callbacks, and strict policies about requests made only via voice or video.

---

## Insider Threats

Employees, contractors, or former staff with legitimate access who misuse it. Can be malicious (intentional data theft) or accidental (clicking a phishing link, misconfiguring a system).

**Detection:** User and Entity Behaviour Analytics (UEBA) — establishing baselines and alerting on anomalies like a user accessing data they've never touched before at 2am.

---

## Key Takeaways

> You can patch software vulnerabilities overnight. You cannot patch human psychology.

The social engineering attacks that succeed aren't brilliant — they're patient. The attacker researches their target, builds credibility, and applies pressure at the right moment. The best defence is a culture where employees feel comfortable saying "let me call you back to verify" without fear of seeming rude or unhelpful.

---

## References

- [SANS — Social Engineering Red Flags](https://www.sans.org/security-awareness-training/resources/)
- [MITRE ATT&CK — T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
