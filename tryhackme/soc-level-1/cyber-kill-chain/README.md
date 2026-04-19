# Room: Cyber Kill Chain

**Platform:** TryHackMe  
**Path:** SOC Level 1  
**Category:** Threat Intelligence  
**Difficulty:** Easy  
**Room Link:** https://tryhackme.com/room/cyberkillchainzmt

---

## 📌 What is this room about?

The Cyber Kill Chain is a framework developed by Lockheed Martin that models the stages of a cyberattack from the attacker's perspective. Understanding each phase helps defenders identify where in an attack they can intervene and what evidence to look for at each stage.

---

## 🎯 Key Concepts Learned

- The 7 phases of the Cyber Kill Chain and what happens in each
- How to map real-world attacker behaviour to kill chain phases
- Why breaking the kill chain early (Reconnaissance, Weaponisation) is more effective than detecting at Exfiltration
- The limitations of the original Kill Chain model for insider threats and lateral movement

---

## 🛠️ Tools / Concepts Referenced

| Tool / Concept | Purpose |
|----------------|---------|
| OSINT tools | Used by attackers in Reconnaissance phase |
| Metasploit | Common in Exploitation phase |
| C2 frameworks | Used in Command & Control phase |

---

## 🧠 The 7 Phases

| Phase | What the attacker does | What defenders look for |
|-------|----------------------|------------------------|
| **1. Reconnaissance** | Research target — OSINT, scanning | Unusual scanning from external IPs, brand monitoring |
| **2. Weaponisation** | Build malware, exploit, payload | Threat intel feeds, malware sandboxes |
| **3. Delivery** | Send phishing email, USB, watering hole | Email gateway, web proxy logs |
| **4. Exploitation** | Execute exploit on target | EDR alerts, Sysmon Event ID 1 |
| **5. Installation** | Install backdoor, persistence | FIM alerts, new scheduled tasks, registry changes |
| **6. Command & Control** | Establish comms with C2 server | Unusual outbound connections, DNS anomalies |
| **7. Actions on Objectives** | Steal data, encrypt, pivot | DLP alerts, large data transfers, lateral movement |

**The defender's advantage:** If you break the chain at any phase, the attack fails. Breaking it early (phases 1-3) before the attacker has a foothold is ideal. Breaking it at phase 6 (C2) is still a win — the attacker has access but cannot use it.

---

## 💡 Key Takeaways

> An attacker must complete every phase. A defender only needs to catch them once.

The Kill Chain reframed how I think about detection. In my SOC Home Lab, I have detections at multiple phases — Suricata catches network scanning (Reconnaissance), Wazuh FIM catches persistence (Installation), and custom Sigma rules catch C2 patterns (Command & Control). This defence-in-depth means an attacker has to evade multiple independent layers.

**Limitation worth noting:** The original Kill Chain was designed for nation-state style targeted attacks. It doesn't model insider threats or attacks that start inside the network particularly well — that's where the Diamond Model and MITRE ATT&CK add value.

---

## 🔗 References

- [Lockheed Martin — Intelligence-Driven Computer Network Defense](https://lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf)
- [MITRE ATT&CK — more granular than Kill Chain](https://attack.mitre.org/)
