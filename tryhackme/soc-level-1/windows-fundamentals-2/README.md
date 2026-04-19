# Room: Windows Fundamentals 2

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Windows
**Difficulty:** Info
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/windowsfundamentals2x0x

---

## What is this room about?

Covers MSConfig and the administrative tools accessible from it: UAC settings, Computer Management, System Information, Resource Monitor, Command Prompt, and Registry Editor.

---

## MSConfig (System Configuration)

`Win+R -> msconfig`. Five tabs: General, Boot, Services, Startup, Tools. The Tools tab is a hub for launching admin utilities quickly.

---

## Key Admin Tools

### Computer Management (compmgmt.msc)
- **Task Scheduler** — persistence mechanism. Event ID 4698 = new scheduled task.
- **Event Viewer** — browse Windows Event Logs
- **Disk Management** — storage

### System Information (msinfo32.exe)
Hardware, OS version, drivers, running services. Used for asset profiling during IR.

### Resource Monitor (resmon.exe)
Real-time CPU/memory/disk/network per process. **Network tab = fastest way to identify which process is making a suspicious outbound connection.**

### Registry Editor (regedit.exe)
Five root keys: HKLM, HKCU, HKU, HKCR, HKCC.

**Critical persistence locations:**
- `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` — runs at boot, all users
- `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` — runs at this user's login

Sysmon Event IDs 12/13 detect registry modifications.

### Command Prompt — Analyst commands
```
ipconfig /all     Full network config
netstat -ano      Active connections with PIDs
tasklist /svc     Processes with services
net user          Local accounts
```

---

## Key Takeaways

> Registry Run keys are the most common commodity malware persistence location. Know where they are. Know how to check them (`Get-ItemProperty` in PowerShell is faster than regedit for a quick check).

---

## References

- [MITRE ATT&CK T1547.001 Registry Run Keys](https://attack.mitre.org/techniques/T1547/001/)
