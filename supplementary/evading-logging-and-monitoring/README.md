# Evading Logging and Monitoring

**Platform:** TryHackMe
**Path:** Supplementary — understanding attacker evasion for better detection
**Difficulty:** Medium
**Status:** Complete

---

## Overview

Understanding how attackers evade logging is essential for building detection that survives evasion. This room covers ETW (Event Tracing for Windows) architecture and the specific techniques used to disable it.

---

## ETW Architecture

| Component | Role |
|-----------|------|
| Controllers | Build and configure logging sessions |
| Providers | Generate events from specific sources |
| Consumers | Receive and process events (Event Viewer, SIEM agents) |

Once logs are forwarded to the SIEM, the attacker loses control. Evasion must occur at the source.

---

## Evasion Technique 1 — Log Clearing (Log Smashing)

```cmd
wevtutil cl Security
```

Generates Event ID 1102 (Security log cleared) and 104 (System log cleared). In environments with real-time log forwarding, the logs are already in the SIEM before the attacker can delete them.

---

## Evasion Technique 2 — PSEtwLogProvider Reflection

Disables PowerShell Script Block Logging (Event ID 4104) for the current session by modifying the ETW provider in memory:

```powershell
$logProvider = [Ref].Assembly.GetType('System.Management.Automation.Tracing.PSEtwLogProvider')
$etwProvider = $logProvider.GetField('etwProvider','NonPublic,Static').GetValue($null)
[System.Diagnostics.Eventing.EventProvider].GetField('m_enabled','NonPublic,Instance').SetValue($etwProvider,0)
```

**Blue team detection:** Absence of 4104 events during a PowerShell session where they are expected. Correlate with other indicators.

---

## Evasion Technique 3 — ETW Patching in Memory

Patches `EtwEventWrite` in ntdll.dll to return immediately without processing events. Requires `VirtualProtect` calls on ntdll memory.

**Detection:** Monitor for `VirtualProtect` calls on ntdll.dll memory regions. Sysmon with memory access events is useful here.

---

## PowerShell Log Sources

| Source | Enabled by default | Event ID | Captures |
|--------|-------------------|----------|---------|
| ConsoleHost history | Yes | — | Interactive commands |
| PowerShell Event Channel | Yes | 600 | Engine launch only |
| Script Block Logging | No | 4104 | All commands, decoded |

Script Block Logging (4104) should be enabled organisation-wide — it is the most valuable PowerShell log source and must be explicitly enabled.

---

## References

- [MITRE ATT&CK — T1562.006 Indicator Blocking](https://attack.mitre.org/techniques/T1562/006/)
