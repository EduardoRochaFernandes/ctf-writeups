# Systems as Attack Vectors

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 01: Blue Team Introduction
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

When social engineering is not the chosen approach, attackers go directly after the technical infrastructure: servers, workstations, cloud environments, and network devices. This room covers the primary categories of system-level attack and the defensive approaches that address them.

---

## Categories of System Attack

### Exploitation of Software Vulnerabilities

Every complex piece of software contains bugs. When a bug can be leveraged to cause unintended behaviour — arbitrary code execution, privilege escalation, or data disclosure — it becomes a vulnerability. The attacker who finds and weaponises it has an exploit.

**Key terminology:**
| Term | Definition |
|------|-----------|
| Vulnerability | A weakness in software or configuration that can be exploited |
| Exploit | The specific code or method used to take advantage of the vulnerability |
| Attack vector | The path through which the exploit is delivered and executed |
| Zero-day | A vulnerability unknown to the vendor — no patch exists at time of exploitation |
| CVE | Common Vulnerabilities and Exposures — standardised identifier assigned to known vulnerabilities |

**CVE scoring:** Each CVE receives a CVSS (Common Vulnerability Scoring System) score from 0 to 10, measuring severity across dimensions including: attack complexity, authentication requirements, confidentiality/integrity/availability impact, and whether the attack vector is network-based or requires physical access.

### Misconfigurations

Misconfigured systems are often more exploitable than unpatched ones because they require no special tooling — just knowledge of what to look for. Common examples:

- Default credentials left unchanged on network devices, servers, or cloud services
- Cloud storage (S3 buckets, Azure Blob Storage) with public read or write access
- Database services exposed to the internet with no authentication
- Overly permissive firewall rules
- APIs with excessive permissions or no rate limiting

**Defensive controls:** Regular configuration audits, infrastructure-as-code with security linting, cloud security posture management (CSPM) tools, penetration testing.

### Supply Chain Attacks

Modern applications depend on hundreds of third-party libraries and services. A single compromised library can affect thousands of downstream applications simultaneously.

**Notable examples:**
- **SolarWinds (2020)** — malicious code inserted into a software build process, distributed to approximately 18,000 customers including US government agencies
- **Log4Shell (CVE-2021-44228)** — critical remote code execution in the Log4j logging library, present in millions of Java applications
- **XZ Utils backdoor (2024)** — a carefully staged multi-year insertion of a backdoor into a widely used Linux compression utility

### Human-Led System Attacks

Some system compromises begin with a human element: weak passwords that can be brute-forced, deceptive websites that serve drive-by downloads, or hardware such as infected USB drives intentionally left in target locations.

---

## The SOC Analyst's Perspective

From a detection standpoint, understanding the attack surface is essential for building effective detection coverage. An analyst who knows which services are exposed, which CVEs affect the organisation's software estate, and which configuration weaknesses are most commonly exploited can prioritise detection accordingly.

When a new high-severity CVE is published, the immediate SOC response is:
1. Determine whether the affected software is present in the environment
2. Search SIEM and EDR for exploitation indicators
3. Verify that patching is in progress
4. Monitor for exploitation attempts until patching is complete

---

## Key Takeaways

Attackers follow the path of least resistance. A misconfigured public-facing service is often exploited within hours of internet exposure. The combination of vulnerability management, configuration auditing, and continuous monitoring is the minimum baseline for keeping system-level attack surface under control.

---

## References

- [CVE Database — MITRE](https://cve.mitre.org/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)
- [MITRE ATT&CK — T1190 Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/)
- [MITRE ATT&CK — T1195 Supply Chain Compromise](https://attack.mitre.org/techniques/T1195/)
