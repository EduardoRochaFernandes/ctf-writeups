# Room: Summit

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Threat Intelligence
**Difficulty:** Easy
**Type:** Challenge
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/thesummit

---

## What is this room about?

Interactive challenge putting the Pyramid of Pain into practice. You play a defender trying to prevent a simulated adversary from achieving their objective, applying defences at each pyramid level.

---

## The Challenge Progression

Starting at hash blocking (bottom), you block indicators and watch the attacker adapt:

1. Block malware hash -> attacker recompiles, new hash in minutes
2. Block IP -> attacker switches C2 IPs
3. Block domain -> attacker registers new domain
4. Detect host artefacts -> attacker redesigns dropper
5. Detect network artefacts -> attacker changes C2 framework
6. Block tools -> attacker must acquire new tools
7. Detect TTPs -> attacker gives up (too expensive to change methodology)

---

## The Cost Model

This is the Pyramid of Pain made tangible. Each level you move up imposes exponentially higher cost on the attacker:
- Hash change: minutes
- IP change: seconds
- Domain change: hours + registration cost
- Tool replacement: days + money
- TTP change: weeks + retraining the entire operation

---

## Applying This in Practice

In a real SOC:
- Hash/IP blocking: fast to implement, low durability
- TTP-based Sigma rules mapped to ATT&CK: high effort, high durability, high attacker pain

Both are needed. Hashes for speed, TTPs for resilience.

---

## Key Takeaways

> After this challenge I reviewed every detection rule in my SOC Home Lab. Rules that only detect a specific hash or IP are now labelled "fragile" and paired with a TTP-based rule that catches the same technique with any indicator.

---

## References

- [Pyramid of Pain — David Bianco](http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)
- [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
