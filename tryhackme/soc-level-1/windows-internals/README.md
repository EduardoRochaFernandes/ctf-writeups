# Room: Windows Internals

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Windows
**Difficulty:** Medium
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/windowsinternals

---

## What is this room about?

Deeper look at Windows internals — processes, threads, virtual memory, the Windows API, and process injection. Essential for advanced malware analysis and understanding EDR detection logic.

---

## Processes vs Threads

- **Process** — container for a running program. Own virtual memory, security context, resources.
- **Thread** — actual execution unit. Multiple threads per process.
- **PID/TID** — unique identifiers.

Malware injects code into legitimate processes (process injection — T1055) to hide under trusted process names.

---

## Virtual Memory

Each process gets isolated virtual address space. One process cannot read another's memory without specific API calls: `ReadProcessMemory`, `WriteProcessMemory`.

---

## Classic Process Injection API Chain

```
VirtualAllocEx       - allocate memory in target process
WriteProcessMemory   - write malicious code there
CreateRemoteThread   - execute the code
```

Sysmon Event ID 8 (CreateRemoteThread) and Event ID 10 (ProcessAccess) detect this chain.

---

## Process Injection Techniques

| Technique | Method |
|-----------|--------|
| DLL Injection | Force process to load malicious DLL |
| Process Hollowing | Replace legitimate process code |
| Thread Hijacking | Redirect existing thread |
| Reflective DLL | Load DLL from memory, no disk file |

---

## The Windows API

Everything goes through Win32 API — file operations, network connections, process creation. EDRs hook these API calls to monitor behaviour. Attackers use API unhooking and direct syscalls to bypass.

---

## Key Takeaways

> VirtualAllocEx + WriteProcessMemory + CreateRemoteThread in sequence is as close to a definitive process injection signature as you get. Sysmon Event ID 8 targeting an unrelated process is always worth investigating.

---

## References

- [MITRE ATT&CK T1055 Process Injection](https://attack.mitre.org/techniques/T1055/)
