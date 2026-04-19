# Room: MITRE

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Threat Intelligence
**Difficulty:** Medium
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/mitre

---

## What is this room about?

MITRE is a non-profit organisation that, since 2013, has maintained the most important framework in cybersecurity — ATT&CK. This room covers the full ecosystem of MITRE resources relevant to defenders: ATT&CK, CAR, D3FEND, and related tools.

---

## ATT&CK — The Foundation

**MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge)** is a knowledge base of real-world adversary behaviours, built from observed attacks. It's the universal language of cybersecurity.

### The Three Levels

| Level | What it is | Example |
|-------|-----------|---------|
| **Tactic** | The *why* — the goal of the phase | Credential Access |
| **Technique** | The *how* — the method used | T1110 — Brute Force |
| **Procedure** | The *specific implementation* | Using Hydra against SSH with a wordlist |

### The ATT&CK Matrix

A visual grid with Tactics as columns and Techniques grouped beneath each. Currently 14 tactics:
Initial Access · Execution · Persistence · Privilege Escalation · Defense Evasion · Credential Access · Discovery · Lateral Movement · Collection · Command and Control · Exfiltration · Impact · Reconnaissance · Resource Development

### ATT&CK Navigator

A web tool to annotate and explore the matrix. Lets you:
- Colour-code techniques by detection coverage
- Create layers for specific threat groups
- Compare your detection coverage against known threat actors
- Export as JSON for sharing with your team

---

## CAR — Cyber Analytics Repository

CAR is the practical counterpart to ATT&CK. Where ATT&CK describes attacks, CAR gives you the **detection queries** to catch them.

Each CAR analytic contains:
1. Description of the behaviour being detected
2. ATT&CK technique reference
3. Pseudocode for the logic
4. Concrete implementations — Splunk SPL, EQL, LogPoint queries
5. Unit tests (when present) to validate the analytic

CAR has its own ATT&CK Navigator layer showing which techniques have analytics available — useful for identifying detection gaps.

---

## D3FEND

**D3FEND (Detection, Denial, and Disruption Framework Empowering Network Defense)** is the defensive complement to ATT&CK. Where ATT&CK describes how attackers operate, D3FEND describes how to stop them.

7 defensive tactics, each with techniques and IDs. The most powerful use: for any ATT&CK technique, look up D3FEND to find the corresponding defensive countermeasure.

---

## Related Tools in the MITRE Ecosystem

| Tool | Purpose |
|------|---------|
| **Adversary Emulation Library** | Step-by-step plans to emulate known threat groups in lab environments |
| **Caldera** | Automated adversary emulation tool — simulates real attacker behaviour using ATT&CK TTPs |
| **ATLAS** | ATT&CK for AI systems — covers ML model attacks, adversarial inputs, training data poisoning |
| **AADAPT** | Framework for digital asset and blockchain threats |

---

## Why ATT&CK Matters for SOC Work

Before ATT&CK, the same attack technique had different names at different companies, in different tools, and in different reports. ATT&CK created a shared vocabulary. When an alert fires and you identify it as T1059.001, you can instantly:
- Look up what other techniques are commonly combined with it
- Find CAR analytics to detect variants
- Search threat intel for which groups use it
- Compare against your environment's coverage

---

## Key Takeaways

> ATT&CK is not just a reference — it's a framework for thinking about threats systematically. Every detection rule should map to it.

In my SOC Home Lab, every Sigma rule I write has an ATT&CK technique ID in its tags. This creates a coverage map showing exactly which parts of the kill chain I can detect and which parts are blind spots.

---

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
- [MITRE CAR](https://car.mitre.org/)
- [MITRE D3FEND](https://d3fend.mitre.org/)
- [Caldera](https://caldera.mitre.org/)
