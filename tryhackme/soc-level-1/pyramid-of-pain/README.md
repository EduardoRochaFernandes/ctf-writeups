# Room: Pyramid of Pain

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Threat Intelligence
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/pyramidofpainax

---

## What is this room about?

The Pyramid of Pain is a threat intelligence model created by David Bianco that describes different types of indicators of compromise (IoCs) and — critically — **how much pain it causes an attacker when defenders detect and block each type**. It completely changed how I think about what's worth detecting.

---

## The Six Levels

```
         /\
        /TT\          ← TTPs
       /----\           Hardest to change — forces full retool
      / Tool \        ← Tools
     /--------\        Painful — requires new software
    /  Network  \     ← Network / Host Artifacts
   /  Artifacts  \     Annoying — attacker has to adapt
  /--------------\
 /  Domain Names  \   ← Domain Names
/------------------\   Annoying — need new domain registration
/   IP Addresses    \  ← IPs
/--------------------\  Easy — change in seconds
/    Hash Values      \ ← Hashes
/----------------------\ Trivial — modify one byte = new hash
```

---

## Each Level Explained

### Hash Values (Trivial)
A hash is a fixed-length fingerprint of a file — MD5 (128-bit, avoid), SHA-1 (160-bit, legacy), SHA-256 (256-bit, standard). Hashes are used by EDRs and threat intel platforms to identify known malware. The problem: changing a single character in the file generates a completely different hash. Attackers rebuild binaries constantly. **Fuzzy hashing (SSDeep)** is better — it detects near-identical files even with minor modifications.

### IP Addresses (Easy)
Blocking IPs is common but ineffective on its own. Attackers use **Fast Flux DNS** — a technique that rotates a domain through hundreds of IPs constantly, all pointing back to the real C2. A botnet of compromised hosts acts as proxies. You block one IP, the malware just uses another.

### Domain Names (Annoying)
Harder than IPs — requires registering a new domain, waiting for DNS propagation, and updating the malware. Attackers use **Punycode** (visual spoofing with lookalike characters — `wlndows` with an L instead of I) and **URL shorteners** to hide real destinations. Tools like **Any.Run** (sandbox) show HTTP requests, DNS queries, and connections made by malware — great for extracting domains from samples.

### Host Artifacts (Annoying)
Traces the attacker leaves **inside the compromised system**: suspicious registry keys, unusual process trees (Word spawning PowerShell), dropped files, attack-specific IOCs. To change these, the attacker has to redesign their tooling — they can't just change a config value.

### Network Artifacts (Annoying)
Traces in **network traffic**: unusual User-Agent strings in HTTP requests, C2 beaconing patterns, specific URI patterns in POST requests. Detecting these forces the attacker to rebuild their communication framework. TShark is useful here:
```bash
tshark -Y http.request -T fields -e http.host -e http.user_agent -r capture.pcap
```

### Tools (Painful)
When you can detect the tools themselves — Mimikatz, Cobalt Strike, specific RATs — the attacker has to buy or build new ones. Detection methods: antivirus signatures, YARA rules (pattern matching inside files), community rule sets from **MalwareBazaar** and **Malshare**.

### TTPs — Tactics, Techniques & Procedures (Maximum Pain)
The top of the pyramid. TTPs describe **how** the attacker operates — their methodology, their tradecraft, their specific procedures. All mapped in the **MITRE ATT&CK framework**. An attacker can change their IP in seconds but cannot change their TTPs overnight — doing so means retraining, rebuilding, and rethinking the entire attack chain. Pass-the-Hash is a TTP. If you detect it, contain it, and shut it down — the attacker has nowhere to go.

---

## Key Takeaways

> Blocking a hash is like changing the locks after a burglar copied your key. They'll just make a new one. Block their *methods*, not their tools.

This model directly shapes how I think about detection engineering. Every Sigma rule I write for my [SOC Home Lab](https://github.com/EduardoRochaFernandes/soc-home-lab) maps to a MITRE ATT&CK technique — never just a hash or an IP. A rule that says "detect PowerShell downloading and executing a script" will catch an attacker regardless of what malware family they use.

---

## References

- [David Bianco — Pyramid of Pain (original post)](http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [SSDeep fuzzy hashing](https://ssdeep-project.github.io/ssdeep/)
- [MalwareBazaar](https://bazaar.abuse.ch/)
