# Room: Introduction to EDR

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Endpoint & EDR
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/introtoedroverview

---

## What is this room about?

EDR — Endpoint Detection and Response — is one of the most important tools in a modern SOC. This room explains what EDR is, how it works under the hood, and critically, how it differs from traditional antivirus.

---

## Why EDR Exists

With remote work, corporate devices operate outside the network perimeter constantly. Traditional firewalls and network-based controls can't protect a laptop on a coffee shop Wi-Fi. EDR is the answer — it puts a security agent directly on the device.

---

## The Three Pillars of EDR

### 1. Visibility
Every process that runs on an endpoint is recorded in a **process tree**. You can see exactly what spawned what, with what arguments, at what time. This is something antivirus can never give you.

### 2. Detection
EDR goes far beyond antivirus signature matching. It uses:
- **Behavioural analysis** — is this process doing something unusual? (Word spawning PowerShell = red flag)
- **Baseline anomaly detection** — the EDR learns what's normal for this specific device over time; deviations are flagged
- **IOC matching** — hash comparison against known malware databases
- **Machine learning** — detecting novel threats based on behavioural patterns
- **Fileless malware detection** — catches attacks that run purely in memory, leaving no file on disk

### 3. Response
When something is detected, the analyst (or the EDR automatically) can:
- **Isolate the host** from the network instantly
- **Kill processes** remotely
- **Quarantine files** without deleting evidence
- **Connect remotely** to the endpoint for live investigation
- **Collect forensic data** (memory dumps, process lists, network connections)

---

## EDR vs Antivirus

| Feature | Antivirus | EDR |
|---------|-----------|-----|
| Known malware detection | ✅ (signatures) | ✅ |
| Unknown/zero-day detection | ❌ | ✅ (behavioural) |
| Fileless malware | ❌ | ✅ |
| Process visibility | ❌ | ✅ (full tree) |
| Remote response | ❌ | ✅ |
| Host isolation | ❌ | ✅ |
| Forensic capability | ❌ | ✅ |

The critical difference: antivirus only knows what it's been told is bad. EDR watches everything and flags what looks wrong — even if it's never seen that specific threat before.

---

## EDR Architecture

```
Agent/Sensor on endpoint
    → Records all process activity
    → Monitors file system, registry, network connections
    → Detects suspicious behaviour
    → Sends data + alerts to Central Console

Central Console
    → Correlates data from all agents
    → Applies ML models
    → Generates alerts with full context
    → Analyst dashboard
```

---

## Telemetry — What the EDR Records

- Process start/stop events (what ran, when, as whom)
- Network connections (destination IP, port, process that made the connection)
- Command line activity (including obfuscated commands)
- File creation, modification, deletion
- Registry changes
- Loaded DLLs and drivers

---

## Important Limitation

EDR is **host-only**. It sees everything that happens on the endpoint but knows nothing about what's happening on the network between endpoints. For network-level detection you need an **NDR (Network Detection and Response)**, and you correlate both with your **SIEM**.

---

## Key Takeaways

> An antivirus asks "have I seen this before?" An EDR asks "is this behaving the way legitimate software should?"

The shift from signature-based to behaviour-based detection is what makes EDR so much more powerful against modern threats. Attackers know how to evade signatures — they change their malware constantly. Changing behaviour is much harder.

---

## References

- [MITRE ATT&CK — T1055 Process Injection](https://attack.mitre.org/techniques/T1055/)
- [Elastic Security — What is EDR?](https://www.elastic.co/what-is/edr-security)
