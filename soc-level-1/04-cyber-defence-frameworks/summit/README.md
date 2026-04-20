# Summit

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 04: Cyber Defence Frameworks
**Difficulty:** Easy
**Type:** Challenge
**Status:** Complete

---

## Overview

Summit is a challenge room that operationalises the Pyramid of Pain. Rather than studying the model theoretically, the player acts as a defender attempting to stop a simulated adversary by applying controls at each level of the pyramid. The adversary adapts to every block, forcing the player to escalate to higher, more costly levels of detection.

---

## The Challenge Mechanic

The player starts with access to the bottom of the pyramid — hash-based blocking. Each block causes the adversary to adapt:

1. Block the malware hash — attacker recompiles: new hash in minutes
2. Block the C2 IP — attacker rotates to a new IP
3. Block the domain — attacker registers a new domain
4. Detect host artefacts — attacker redesigns their dropper and persistence mechanism
5. Detect network artefacts — attacker redesigns C2 communication patterns
6. Block the tools — attacker must acquire or build new tooling
7. Detect TTPs — attacker abandons the campaign

Each level takes longer and costs more for the attacker to overcome. At the TTP level, the cost is prohibitive for most threat actors.

---

## The Cost Model

The Pyramid of Pain is fundamentally an economic model:

| Level | Attacker cost to adapt | Defender effort to implement |
|-------|----------------------|------------------------------|
| Hash | Seconds | Low |
| IP | Seconds | Low |
| Domain | Hours + registration fee | Low-Medium |
| Host Artefacts | Days | Medium |
| Network Artefacts | Days to weeks | Medium-High |
| Tools | Weeks + financial cost | High |
| TTPs | Weeks to months, full retooling | Very High |

The highest-value defences are the hardest to implement but impose the greatest cost on the adversary. Hash and IP blocking have their place — speed matters — but they should never be the primary detection strategy.

---

## Lessons from the Challenge

**Layered defences are necessary.** No single level provides complete protection. A hash block that expires before TTP-based detection is in place leaves a gap.

**Detection durability is as important as detection breadth.** A TTP-based Sigma rule that catches PowerShell injection will remain valid across tool changes, IP changes, and domain changes. A hash-based rule will be obsolete within hours of a new variant.

**The attacker's adaptation speed sets the required response speed.** At the hash level, the attacker adapts faster than most organisations can update blocklists. At the TTP level, the attacker cannot adapt faster than a well-written detection rule.

---

## Application to the SOC Home Lab

This room directly influenced the detection engineering approach in my [SOC Home Lab](https://github.com/EduardoRochaFernandes/soc-home-lab): every Sigma rule is tagged with an ATT&CK technique ID, and rules that detect only specific hashes or IPs are marked as "low durability" and paired with a behaviour-based rule targeting the same technique with different indicators.

---

## References

- [Pyramid of Pain — David Bianco](http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)
- [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
