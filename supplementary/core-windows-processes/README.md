# Core Windows Processes

**Platform:** TryHackMe
**Path:** Supplementary — Windows security foundations for Windows Monitoring section
**Difficulty:** Easy
**Status:** Complete

---

## Overview

To detect malicious processes on a Windows endpoint, you first need to know what legitimate processes look like. This room establishes the normal parent-child relationships, expected paths, and instance counts for core Windows processes.

---

## Process Hierarchy

```
System (PID 4)
  smss.exe
    wininit.exe
      services.exe
        svchost.exe (many instances — all must have -k flag)
      lsass.exe
    winlogon.exe
      explorer.exe
```

---

## Process Reference

| Process | Expected parent | Instances | Key check |
|---------|----------------|-----------|-----------|
| System | None | 1 | PID always 4 |
| smss.exe | System | 1 | First user-mode process |
| wininit.exe | smss.exe | 1 | Launches services.exe + lsass.exe |
| services.exe | wininit.exe | 1 | Service Control Manager |
| svchost.exe | services.exe | Many | Must have `-k` in command line |
| lsass.exe | wininit.exe | 1 | Authentication — Mimikatz target |
| explorer.exe | userinit.exe | 1 per user | Desktop shell |

---

## The svchost.exe `-k` Rule

Every legitimate svchost.exe must include `-k` in its command line:
```
C:\Windows\System32\svchost.exe -k netsvcs -p -s Schedule
```
No `-k`, or running from outside System32, indicates masquerading.

---

## lsass.exe — Credential Target

Handles all authentication. Exactly one instance, child of wininit.exe. Mimikatz targets it. Detection: Sysmon Event ID 10 (ProcessAccess) with GrantedAccess values `0x1010`, `0x1410`.

---

## Red Flags

- Process running from wrong directory
- Misspelled process name (scvhost.exe, lssas.exe)
- svchost.exe without `-k`
- Multiple instances of processes that should be unique

---

## References

- [MITRE ATT&CK — T1036 Masquerading](https://attack.mitre.org/techniques/T1036/)
