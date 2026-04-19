# Room: Evading Logging and Monitoring

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Windows
**Difficulty:** Medium
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/monitoringevasion

---

## What is this room about?

Understanding how attackers evade logging is essential for defenders — you can't detect evasion you don't know about. This room covers the Windows logging architecture (ETW), and the specific techniques attackers use to blind it, from simple log clearing to memory patching.

---

## Why Attackers Target Logging

Logs are the only record of what happened. If an attacker can destroy or prevent log generation, defenders work blind. The attacker's goal isn't total destruction (which raises suspicion) — it's **selective blindness**: preventing specific detection while keeping the system stable enough not to trigger alarms.

Log flow: `Host → Event Collector/Forwarder → Indexer → SIEM`. Once logs reach the SIEM, the attacker loses control of them. The attack must happen at the source.

---

## ETW — Event Tracing for Windows

The low-level logging infrastructure in Windows. Three components:

| Component | Role |
|-----------|------|
| **Controllers** | Build and configure logging sessions |
| **Providers** | Generate events (one per data source) |
| **Consumers** | Receive and process events (Event Viewer, SIEM agents) |

**Provider types:** MOF, WPP, Manifest-Based, TraceLogging — each with different characteristics and session limits.

---

## Evasion Technique 1 — Log Smashing (Clearing Logs)

The obvious approach: delete the logs. High risk because it's immediately detectable:

| Event ID | What it means |
|----------|--------------|
| **1102** | Security audit log cleared |
| **104** | System log cleared |
| **1100** | Event Log service stopped |

In modern environments, logs are already forwarded to the SIEM before they're cleared — so this is mostly evidence destruction that doesn't actually prevent detection.

---

## Evasion Technique 2 — PSEtwLogProvider Reflection (PowerShell)

The ETW provider for PowerShell (`PSEtwLogProvider`) is loaded as a .NET assembly in every PowerShell session. Since it runs in the same security context as the PowerShell process, an attacker can modify it using Reflection:

```powershell
$logProvider = [Ref].Assembly.GetType('System.Management.Automation.Tracing.PSEtwLogProvider')
$etwProvider = $logProvider.GetField('etwProvider','NonPublic,Static').GetValue($null)
[System.Diagnostics.Eventing.EventProvider].GetField('m_enabled','NonPublic,Instance').SetValue($etwProvider,0)
```

**Effect:** PowerShell commands executed after this script generate no Event ID 4104 (Script Block Logging) entries. The session is effectively invisible to the SIEM.

---

## Evasion Technique 3 — Group Policy Takeover

Script Block Logging and Module Logging are controlled by Group Policy settings stored in memory. An attacker can modify them for the current session:

```powershell
$GPOField = [ref].Assembly.GetType('System.Management.Automation.Utils').GetField('cachedGroupPolicySettings','NonPublic,Static')
$GPOSettings = $GPOField.GetValue($null)
$GPOSettings['ScriptBlockLogging']['EnableScriptBlockLogging'] = 0
```

**Effect:** Disables Event ID 4104 logging for the current PowerShell session without touching Group Policy infrastructure.

---

## Evasion Technique 4 — ETW Patching (Most Aggressive)

Directly patches the `EtwEventWrite` function in `ntdll.dll` in memory, forcing it to return immediately without processing any events:

```
Before: 779f23c0: xor ecx, esp → processes the event
After:  779f23c0: ret 14h      → returns immediately, nothing logged
```

**C# Implementation pattern:**
1. Get handle to `EtwEventWrite` in ntdll.dll
2. Change memory protection to RWX (read/write/execute)
3. Write `ret 14h` (`0xc2 0x14 0x00`) at the function start
4. Restore original memory protection (OPSEC)
5. Flush instruction cache

**Blue team detection:** Monitor for `VirtualProtect` calls against ntdll.dll memory regions, or `Marshal.Copy`/`WriteProcessMemory` targeting system functions.

---

## Key PowerShell Log Sources

| Source | Enabled by default | Event ID | What it captures |
|--------|-------------------|----------|-----------------|
| Console History | ✅ | — | Interactive commands only |
| Windows PowerShell Event Channel | ✅ | 600 | Engine launch and arguments |
| Script Block Logging | ❌ | 4104 | All commands, fully decoded, including obfuscated Base64 |

**4104 is the most valuable** — it shows the decoded command even if it was Base64-encoded or obfuscated. Enabling it via Group Policy should be a baseline in every environment.

---

## Key Takeaways

> Understanding how attackers evade detection is not about enabling attacks — it's about building detection that survives evasion attempts.

The ETW patching technique is particularly important to understand. When a security tool relies entirely on PowerShell Event ID 4104 for detection, and an attacker can disable that logging with three lines of PowerShell before their main payload runs, those detections are worthless. Defence-in-depth means having multiple independent logging sources.

---

## References

- [MITRE ATT&CK — T1562.006 Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/)
- [ETW Architecture (Microsoft Docs)](https://learn.microsoft.com/en-us/windows/win32/etw/about-event-tracing)
