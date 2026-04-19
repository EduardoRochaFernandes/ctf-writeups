# Room: Core Windows Processes

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Windows
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/btwindowsinternals

---

## What is this room about?

To detect malicious processes on a Windows endpoint you first need to know what legitimate processes look like. Covers core Windows processes, their parent-child relationships, expected paths, and instance counts — so anomalies are immediately visible.

**Tools:** Task Manager, Process Hacker, Process Explorer

---

## Why This Matters

Attackers masquerade as legitimate processes — naming malware `svchost.exe`, misspelling it (`scvhost.exe`), or running it from the wrong directory. Without knowing what normal looks like, you can't spot the fake.

---

## Core Process Hierarchy

```
System (PID 4)
  smss.exe
    winlogon.exe -> explorer.exe
    wininit.exe
      services.exe -> svchost.exe (many)
      lsass.exe
```

---

## Process Reference

| Process | Normal parent | Instances | Key check |
|---------|--------------|-----------|-----------|
| System | None | 1 | PID always 4 |
| smss.exe | System | 1 | First user-mode process |
| wininit.exe | smss.exe | 1 | Launches services.exe + lsass.exe |
| services.exe | wininit.exe | 1 | Service Control Manager |
| svchost.exe | services.exe | Many | Must have `-k` in command line |
| lsass.exe | wininit.exe | 1 | Auth handler — Mimikatz target |
| winlogon.exe | smss.exe | 1/session | Manages CTRL+ALT+DEL |
| explorer.exe | userinit.exe | 1/user | Desktop shell |

---

## The svchost.exe `-k` Rule

Every legitimate `svchost.exe` must have `-k` in its command line:
```
C:\Windows\System32\svchost.exe -k netsvcs -p -s Schedule
```

`svchost.exe` without `-k`, or running from outside System32 = malware.

---

## lsass.exe — High-Value Target

Handles all Windows authentication. Exactly **one** instance, child of `wininit.exe`. Mimikatz dumps credentials from lsass memory. Detection: Sysmon Event ID 10 (ProcessAccess) with GrantedAccess values 0x1010, 0x1410.

---

## Red Flags

| Indicator | Suggests |
|-----------|---------|
| Process in wrong directory | Masquerading |
| Misspelled name (scvhost.exe) | Process impersonation |
| svchost.exe without -k | Malicious service |
| Multiple lsass.exe | Credential dumper |

---

## Key Takeaways

> Legitimate svchost.exe always has -k. Check parent, path, and -k parameter. Three checks catch every svchost impersonation.

---

## References

- [MITRE ATT&CK T1036 Masquerading](https://attack.mitre.org/techniques/T1036/)
- [MITRE ATT&CK T1003.001 LSASS Memory](https://attack.mitre.org/techniques/T1003/001/)
