# Room: Diamond Model

**Platform:** TryHackMe  
**Path:** SOC Level 1  
**Category:** Threat Intelligence  
**Difficulty:** Easy  
**Room Link:** https://tryhackme.com/room/diamondmodelrmuwwg42

---

## 📌 What is this room about?

The Diamond Model of Intrusion Analysis is a framework for structuring and analysing cyber intrusions. It defines four core features of every attack — Adversary, Capability, Infrastructure and Victim — and the relationships between them. It's particularly useful for threat intelligence analysts linking separate incidents to the same threat actor.

---

## 🎯 Key Concepts Learned

- The four vertices of the Diamond Model and what each represents
- How to use the model to pivot between IoCs and find related infrastructure
- How the Diamond Model complements the Kill Chain and ATT&CK
- The concept of Activity Threads and Event Graphs for tracking campaigns

---

## 🧠 The Four Vertices

```
          Adversary
         /         \
        /           \
  Capability ——— Infrastructure
        \           /
         \         /
            Victim
```

| Vertex | Description | Example |
|--------|-------------|---------|
| **Adversary** | The threat actor behind the attack | APT29, a ransomware group |
| **Capability** | The tools and techniques used | Mimikatz, PowerShell Empire, custom malware |
| **Infrastructure** | Systems used to conduct the attack | C2 servers, phishing domains, bulletproof hosting |
| **Victim** | The target — organisation, person, or asset | A company's domain controller |

**The power of pivoting:** If you find a C2 IP (Infrastructure), you can pivot to find other victims using the same IP, other malware communicating with it, and potentially link it to a known adversary. This is how threat intel analysts attribute attacks and find related campaigns.

---

## 💡 Key Takeaways

> Every intrusion event can be described by who did it, how they did it, where from, and to whom. The Diamond Model makes this explicit and pivotable.

The Diamond Model is less about detection (that's ATT&CK's job) and more about **investigation and attribution**. In a SOC context, when a major incident occurs, the Diamond Model helps structure the investigation — "we know the Capability (malware) and Victim (us), now let's find the Infrastructure (C2) and eventually the Adversary."

This maps directly to how TheHive in my SOC Home Lab works — cases track adversary, capability, infrastructure and victim as observable types.

---

## 🔗 References

- [The Diamond Model of Intrusion Analysis — original paper](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf)
- [CISA — Using the Diamond Model](https://www.cisa.gov/sites/default/files/publications/diamond-model-intrusion-analysis.pdf)
