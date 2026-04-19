# Room: Windows Basics

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Windows
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/windowsbasics

---

## What is this room about?

Practical introduction to navigating Windows — the file system, essential commands, key directories, and security-relevant locations.

---

## Security-Relevant Directories

| Path | Why it matters |
|------|---------------|
| `C:\Windows\System32` | Core OS — executables here should be verified |
| `C:\Temp` | Writable by all users — top malware drop zone |
| `C:\Users\[user]\AppData` | Hidden by default — common persistence location |
| `C:\Windows\System32\Tasks` | Scheduled task definitions |
| `C:\Windows\Prefetch` | Recently executed programs — forensic evidence |
| `C:\Windows\System32\winevt\Logs` | Windows Event Log files (.evtx) |

---

## Essential CMD Commands for Analysts

```cmd
ipconfig /all         Full network config + DNS
netstat -ano          Active connections with PIDs
tasklist /svc         Processes with services
whoami /priv          Current user privileges
net user              List local accounts
net localgroup        List local groups
dir /a /s C:\Temp     All files including hidden
dir /r                Show Alternate Data Streams
attrib [file]         File attributes (hidden, system)
```

---

## Key Differences: Windows vs Linux

| | Windows | Linux |
|--|---------|-------|
| Path separator | Backslash | Forward slash |
| Case sensitivity | Insensitive | Sensitive |
| Line endings | CRLF | LF |
| Admin account | Administrator | root |
| Config storage | Registry | Text files |

---

## Key Takeaways

> `C:\Temp` and `C:\Users\[user]\AppData\Local\Temp` are the two most common malware landing zones. Any new executable in these directories deserves immediate investigation.

---

## References

- [Microsoft Windows Documentation](https://learn.microsoft.com/en-us/windows/)
