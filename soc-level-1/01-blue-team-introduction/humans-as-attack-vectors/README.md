# Humans as Attack Vectors

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 01: Blue Team Introduction
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

The weakest link in any security architecture is not a misconfigured firewall or an unpatched server — it is a person under pressure making a quick decision. This room covers the principal techniques attackers use to exploit human psychology, the characteristics that make these attacks effective, and the defensive measures that reduce their impact.

---

## Why Human Targeting Works

Technical controls have evolved significantly. Modern firewalls, EDR platforms, and email gateways block enormous volumes of automated attack traffic. Attackers have adapted by targeting the path of least resistance: employees who can be persuaded to take an action that bypasses those controls entirely.

Social engineering attacks succeed because they exploit cognitive biases: authority (a message appearing to come from a senior executive), urgency (an account will be suspended in two hours), fear (legal consequences), and greed (an unexpected financial opportunity). These triggers cause people to act before thinking.

---

## Phishing Attacks

Email-based social engineering remains the most common initial access vector in real-world breaches.

**Characteristics of an effective phishing email:**
- Sender spoofed or closely impersonating a trusted entity
- Urgent or fear-inducing subject line
- HTML body that visually replicates a legitimate brand
- A call to action that requires clicking a link or opening an attachment
- Grammar and formatting designed to appear professional

**Variations:**
- **Spear phishing** — targeted at a specific person, incorporating personal details gathered during reconnaissance (job title, colleagues' names, recent company news)
- **Whaling** — spear phishing targeting C-level executives or board members
- **Smishing** — phishing delivered via SMS
- **Vishing** — phishing via voice call

**Defensive controls:** Email gateway with sandbox attachment analysis, DMARC/DKIM/SPF enforcement, link rewriting, security awareness training.

---

## Malware Delivery via Social Engineering

Attackers routinely use fake software downloads, cracked software from unofficial sources, and malicious browser extensions to deliver malware. The user installs it voluntarily, believing it to be legitimate.

**Indicators:** software requested from sources outside official repositories, executables with mismatched icons or unusual file sizes, documents requesting macro enablement.

**Defensive controls:** Application whitelisting, endpoint protection, user education, blocking execution from user-writable directories.

---

## Deepfakes

The availability of AI audio and video synthesis tools has made voice and video cloning accessible. Attackers use synthesised audio (cloned from public recordings such as YouTube or podcast appearances) or AI-generated video to impersonate trusted individuals, typically in scenarios involving urgent financial transfers or credential requests.

**Documented case:** In 2024, a Hong Kong finance employee transferred approximately $25 million after participating in a video conference call in which all other participants — including the CFO — were AI-generated deepfakes.

**Defensive controls:** There is no technical control that reliably detects deepfakes in real time. Mitigation is procedural: pre-agreed verification codes, mandatory callback procedures for financial requests, and a culture where employees feel safe challenging unusual requests regardless of apparent authority.

---

## Insider Threats

Employees, contractors, and former staff with legitimate access who intentionally or accidentally misuse it. Insider threats are particularly difficult to detect because activity that looks normal for a user's role may be the threat itself.

**Detection approach:** User and Entity Behaviour Analytics (UEBA) — establishing a baseline of normal behaviour for each user and alerting on deviations such as accessing data outside normal working hours, downloading unusually large volumes of data, or accessing systems the user has never previously used.

---

## Key Takeaways

Technical controls cannot fully compensate for human behaviour. The most resilient organisations combine strong controls with a culture where employees treat security as a shared responsibility rather than an IT problem. An employee who calls IT to verify an unusual request — even one that seems to come from a senior colleague — is more valuable than a technically sophisticated one who clicks without questioning.

---

## References

- [MITRE ATT&CK — T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
- [MITRE ATT&CK — T1598 Phishing for Information](https://attack.mitre.org/techniques/T1598/)
- [SANS Social Engineering Resources](https://www.sans.org/security-awareness-training/)
