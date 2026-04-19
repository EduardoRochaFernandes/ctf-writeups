# Room: Unified Kill Chain

**Platform:** TryHackMe  
**Path:** SOC Level 1  
**Category:** Threat Intelligence  
**Difficulty:** Easy  
**Room Link:** https://tryhackme.com/room/unifiedkillchain

---

## 📌 What is this room about?

The Unified Kill Chain (UKC) was developed by Paul Pols in 2017 as an evolution of both the Cyber Kill Chain and MITRE ATT&CK. It models 18 phases of an attack in three macro-stages, addressing the limitations of earlier frameworks — particularly for attacks that involve lateral movement and multiple cycles through the kill chain.

---

## 🎯 Key Concepts Learned

- Why the original Kill Chain is insufficient for complex modern attacks
- The three macro-stages of the UKC: In, Through, Out
- How the UKC maps to and complements MITRE ATT&CK
- The concept of an attack "cycling" through multiple kill chains internally

---

## 🧠 The Three Macro-Stages

### Stage 1 — IN (Initial Foothold)
Getting onto the target network for the first time.

Key phases: Reconnaissance → Weaponisation → Social Engineering → Exploitation → Persistence → Defence Evasion → Command & Control

### Stage 2 — THROUGH (Network Propagation)
Moving through the network after initial access to reach the real target.

Key phases: Pivoting → Discovery → Privilege Escalation → Execution → Credential Access → Lateral Movement

### Stage 3 — OUT (Action on Objectives)
Achieving the actual goal of the attack.

Key phases: Collection → Exfiltration → Impact → Objectives

---

## 💡 Key Takeaways

> The original Kill Chain assumes one attacker, one target, one path. Reality is messier — attackers pivot, cycle, and adapt.

The UKC was the framework that made MITRE ATT&CK "click" for me. ATT&CK provides the individual techniques; the UKC shows where in an attack those techniques fit. Together they give a complete picture.

In a SOC context, the UKC helps with **alert triage** — if you see a Privilege Escalation alert, the UKC tells you the attacker is in the "Through" stage, meaning they already have a foothold and you need to look backwards for how they got In.

---

## 🔗 References

- [Unified Kill Chain — official site](https://www.unifiedkillchain.com/)
- [Paul Pols — original thesis](https://www.unifiedkillchain.com/assets/The-Unified-Kill-Chain.pdf)
