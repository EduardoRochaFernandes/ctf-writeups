# Room: Pyramid of Pain

**Platform:** TryHackMe  
**Path:** SOC Level 1  
**Category:** Threat Intelligence  
**Difficulty:** Easy  
**Room Link:** https://tryhackme.com/room/pyramidofpainax

---

## 📌 What is this room about?

The Pyramid of Pain is a threat intelligence model created by David Bianco that describes different types of indicators of compromise (IoCs) and how much "pain" it causes an attacker when defenders detect and block each type. Understanding this model is fundamental to prioritising what to detect and why.

---

## 🎯 Key Concepts Learned

- The six levels of the Pyramid of Pain and what each represents
- Why blocking a hash is nearly useless compared to detecting TTPs
- How attackers can trivially change low-level indicators but cannot easily change their behaviour
- Why TTPs (Tactics, Techniques and Procedures) sit at the top — hardest for attackers to change

---

## 🛠️ Tools / Concepts Referenced

| Tool / Concept | Purpose |
|----------------|---------|
| VirusTotal | Checking file hashes (bottom of pyramid) |
| MITRE ATT&CK | Framework for TTPs (top of pyramid) |
| YARA rules | Detecting artefacts — middle of pyramid |

---

## 🧠 The Pyramid Explained

```
        /\
       /TT\          ← TTPs (Tactics, Techniques, Procedures)
      /----\            Most painful to change — forces attackers to retrain
     / Tool \         ← Tools (malware, C2 frameworks)
    /--------\          Painful — requires new software
   /  Network \       ← Network / Host Artefacts
  /  Artefacts \        Annoying — requires some effort
 /--------------\
/  Domain Names  \   ← Domain Names
/------------------\   Annoying — requires registering new domains
/    IP Addresses   \ ← IP Addresses
/--------------------\  Easy — change IP trivially
/    Hash Values      \← Hash Values
/----------------------\ Trivial — modify one byte, new hash
```

**The core insight:** Most detection tools focus on hashes and IPs because they're easy to write rules for. But a good detection engineer focuses on TTPs because those are what actually hurt attackers.

---

## 💡 Key Takeaways

> Blocking a hash is like changing the locks after a burglar has already copied your key — they'll just make a new one.

The real value in threat intelligence is identifying *how* attackers operate, not *what specific file* they used. A Sigma rule that detects "PowerShell downloading and executing a script" will catch an attacker even if they change their malware every day. A hash-based blocklist won't.

This directly influenced how I think about writing detection rules in my [SOC Home Lab](https://github.com/EduardoRochaFernandes/soc-home-lab) — all rules are mapped to ATT&CK techniques (TTPs), not just signatures.

---

## 🔗 References

- [David Bianco — Pyramid of Pain (original post)](http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)
- [MITRE ATT&CK](https://attack.mitre.org/)
