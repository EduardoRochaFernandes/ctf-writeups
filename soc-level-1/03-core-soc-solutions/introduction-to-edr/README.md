# Introduction to EDR

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 03: Core SOC Solutions
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Endpoint Detection and Response (EDR) is a security platform deployed directly on individual endpoints — workstations, servers, laptops. It provides visibility into process activity, file operations, network connections, and registry changes, and enables response actions such as host isolation, process termination, and file quarantine. This room establishes what EDR is, how it differs from traditional antivirus, and how the SOC analyst uses it.

---

## Why EDR Exists

With remote and hybrid work, corporate devices operate outside the network perimeter constantly. Traditional perimeter-based controls — firewalls, network IDS — have no visibility into what happens on an endpoint connected to a home network or a public Wi-Fi connection. EDR provides security coverage that travels with the device.

Additionally, traditional antivirus relies on signature matching: it identifies known malicious files by comparing them against a database of known-bad hashes and patterns. Modern attackers routinely modify their tools to generate new signatures, rendering hash-based detection ineffective within hours of a new variant's release. EDR addresses this with behaviour-based detection.

---

## EDR vs Antivirus

| Capability | Antivirus | EDR |
|-----------|-----------|-----|
| Known malware detection | Yes (signature-based) | Yes |
| Unknown / zero-day detection | No | Yes (behavioural analysis) |
| Fileless malware detection | No | Yes |
| Process tree visibility | No | Yes |
| Network connection monitoring | No | Yes |
| Registry change monitoring | No | Yes |
| Remote host isolation | No | Yes |
| Live response / remote shell | No | Yes |
| Forensic data collection | No | Yes |
| Forensic timeline | No | Yes |

The fundamental difference: antivirus asks "have I seen this file before?" EDR asks "is this process behaving the way a legitimate application should?"

---

## The Three Pillars of EDR

**Visibility**
Every process execution is recorded with full context: parent process, command line arguments, user context, timestamp. File creations, modifications, and deletions are tracked. Network connections are logged with the associated process. Registry changes are captured. This telemetry forms a complete record of endpoint activity that can be queried retrospectively.

**Detection**
EDR uses multiple detection mechanisms:
- *Behavioural analysis* — identifies suspicious patterns such as a document application spawning a command interpreter, or a process injecting code into another process
- *Baseline deviation* — learns the normal behaviour of each endpoint over time and alerts when significant deviations occur
- *IOC matching* — compares file hashes, domain names, and IP addresses against threat intelligence feeds
- *Machine learning models* — classifies processes and files based on characteristics rather than signatures
- *MITRE ATT&CK mapping* — maps detected behaviours to specific tactics and techniques for contextualised alerting

**Response**
When a threat is detected or an analyst initiates a response, the EDR enables:
- Host isolation from the network (while maintaining the management channel)
- Remote process termination
- File quarantine
- Live response session for interactive investigation
- Forensic collection (memory dump, disk image, process list)
- Automated response via SOAR integration

---

## EDR Architecture

```
Endpoint Agent (sensor)
    Monitors all process activity, file operations, network connections, registry
    Applies local detection rules
    Sends telemetry and alerts to central console

Central Console
    Aggregates telemetry from all agents
    Applies organisation-wide detection rules and ML models
    Generates alerts with full context
    Analyst investigation interface
    Response action control plane
```

---

## EDR Telemetry — What Is Recorded

- Process creation and termination (with full command line, parent process, user context)
- File create, modify, delete, rename (with process responsible)
- Network connections (source/destination IP, port, protocol, associated process)
- DNS queries (queried domain, resolved IP, associated process)
- Registry key create, modify, delete
- Loaded DLLs and drivers
- Script execution events (PowerShell, WScript, etc.)
- User logon and logoff events

---

## The Important Limitation

EDR is host-only. It has no visibility into network traffic between endpoints unless that traffic touches one of its monitored hosts. For network-level detection — traffic analysis, IDS signatures, protocol anomalies — a separate NDR (Network Detection and Response) platform is required. In a mature SOC, both are deployed and their alerts are correlated through the SIEM.

---

## Key Takeaways

EDR fundamentally changed endpoint security by shifting from signature-based detection to behavioural monitoring. A process that has never been seen before can still be identified as malicious if its behaviour matches known attack patterns — spawning a shell from a document application, injecting into a system process, or communicating with a recently registered domain. The telemetry EDR collects is also the primary source of evidence for incident response investigations.

---

## References

- [MITRE ATT&CK — T1055 Process Injection](https://attack.mitre.org/techniques/T1055/)
- [MITRE ATT&CK — T1059 Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059/)
