# Windows Internals

**Platform:** TryHackMe
**Path:** SOC Level 3 — Section 03: Windows Endpoint Investigation
**Status:** Complete

---

## Key Notes

Process vs thread model, virtual memory isolation, Windows API (Win32) as the interface between user-mode and kernel. Process injection techniques: DLL injection, process hollowing, thread hijacking, reflective DLL loading. Classic injection API chain: VirtualAllocEx + WriteProcessMemory + CreateRemoteThread. Detection: Sysmon Event ID 8 (CreateRemoteThread) and Event ID 10 (ProcessAccess) with suspicious GrantedAccess flags.

---

## Placeholder

Detailed writeup can be expanded here.
