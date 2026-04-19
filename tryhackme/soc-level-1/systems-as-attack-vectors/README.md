# Room: Systems as Attack Vectors

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Attack Vectors
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/systemsasattackvectors

---

## What is this room about?

When social engineering fails or isn't the right approach, attackers go directly after the systems themselves — servers, workstations, cloud infrastructure. This room covers the main categories of system-level attacks and how to defend against them.

---

## Categories of System Attacks

### Human-Led System Attacks
Even system compromises often have a human element:
- **Weak passwords** — brute-forceable in minutes
- **Deceptive websites** — drive-by downloads when visiting a page
- **Malicious hardware** — infected USB drives left in car parks or lobbies

### Vulnerabilities and Exploits

Key terminology:
| Term | Meaning |
|------|---------|
| **Exploit** | The specific code or technique used to weaponise a vulnerability |
| **Attack Vector** | The step-by-step methodology to reach and exploit the target |
| **Zero-Day** | A vulnerability unknown to the vendor — no patch exists yet |

### Supply Chain Attacks
Modern software depends on hundreds of third-party libraries. A single compromised library can affect thousands of applications. Notable examples: SolarWinds (2020), XZ Utils backdoor (2024), Log4Shell (2021).

### Misconfigurations
Often more damaging than zero-days because they're everywhere and easy to exploit:
- Exposed APIs with default credentials
- Databases open to the internet
- S3 buckets with public read access
- Overly permissive firewall rules

**Defences:** Penetration testing, infrastructure scanning, change management with audit logs, principle of least privilege.

---

## CVE — Common Vulnerabilities and Exposures

The CVE system (managed by MITRE, funded by the US Department of Homeland Security) gives every known vulnerability a unique identifier: `CVE-YEAR-NUMBER` (e.g., CVE-2021-44228 — Log4Shell).

Each CVE has a **CVSS score** (0–10) that rates severity across dimensions like: how complex is the exploit, does it require authentication, what's the impact on confidentiality/integrity/availability.

**As a SOC analyst**, when a high-severity CVE drops, you need to:
1. Check if your environment runs the affected software
2. Look for exploitation attempts in your logs
3. Verify that patching is in progress
4. Monitor for indicators of exploitation

---

## Key Takeaways

> A misconfigured system is as dangerous as an unpatched one. Most breaches don't require sophisticated exploits — they require a door left open.

The CVE system is your friend as an analyst. When a new critical CVE is announced, knowing how to quickly search your SIEM for exploitation patterns — and how to correlate that with your asset inventory — is a core skill.

---

## References

- [CVE Database — MITRE](https://cve.mitre.org/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)
- [MITRE ATT&CK — T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
