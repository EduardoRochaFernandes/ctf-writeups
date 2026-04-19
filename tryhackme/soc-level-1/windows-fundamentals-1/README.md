# Room: Windows Fundamentals 1

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Windows
**Difficulty:** Info
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/windowsfundamentals1xbx

---

## What is this room about?

First of three Windows fundamentals rooms. Covers the GUI, NTFS file system, system folders, user accounts, UAC, and Task Manager.

---

## NTFS — Key Security Features

Modern Windows uses NTFS (New Technology File System). Critical for security:
- **File-level ACLs** — granular permission control
- **Journaling** — crash recovery
- **Alternate Data Streams (ADS)** — files can contain hidden data streams invisible in Explorer. Malware hides payloads here.

Detection: `dir /r` reveals ADS.

---

## Key System Folders

| Folder | Security relevance |
|--------|------------------|
| `C:\Windows\System32` | Core executables — malware here is serious |
| `C:\Users` | User profiles |
| `C:\ProgramData` | Shared app data (hidden) — malware common here |
| `C:\Temp` | Writable by all — top malware drop zone |

---

## User Account Types

| Type | Capability |
|------|-----------|
| Administrator | Full system control |
| Standard User | Normal use only |
| SYSTEM | Most privileged — used by OS, not humans |

Manage: `lusrmgr.msc`

---

## UAC — User Account Control

Admin accounts run with reduced privileges by default. UAC prompts when elevation is needed. Limits damage from compromised accounts. Levels: Always Notify, Notify for Apps (default), Never Notify (dangerous).

---

## Key Takeaways

> ADS (Alternate Data Streams) are invisible in normal file browsing but completely real. `dir /r` on suspicious directories should be a routine analyst habit.

---

## References

- [MITRE ATT&CK T1564.004 NTFS File Attributes](https://attack.mitre.org/techniques/T1564/004/)
