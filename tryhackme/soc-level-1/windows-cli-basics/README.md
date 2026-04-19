# Room: Windows CLI Basics

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Windows
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/windowsclibasics

---

## What is this room about?

Practical use of CMD and PowerShell for system investigation and incident response. Essential for both live analysis and forensic examination.

---

## CMD vs PowerShell

| | CMD | PowerShell |
|--|-----|-----------|
| Output | Text | .NET objects (filterable/sortable) |
| Event log access | Limited | Full (Get-WinEvent) |
| Remoting | Limited | Native (PSSession, Invoke-Command) |
| Malware abuse | Less common | Frequently abused |

---

## PowerShell for Analysts

```powershell
# Active network connections
Get-NetTCPConnection | Where-Object State -eq "Established"

# Failed logons last 24h
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddDays(-1)}

# Process creation
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4688}

# Check persistence locations
Get-ItemProperty "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run"
Get-ItemProperty "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"

# Scheduled tasks (persistence check)
Get-ScheduledTask | Where-Object State -eq "Ready"

# Local admins
Get-LocalGroupMember -Group "Administrators"

# Recent files created
Get-ChildItem C:\Users -Recurse -File | Sort-Object LastWriteTime -Descending | Select-Object -First 20
```

---

## PowerShell Remoting

```powershell
Enter-PSSession -ComputerName HOSTNAME -Credential domain\analyst
Invoke-Command -ComputerName HOSTNAME -ScriptBlock { Get-NetTCPConnection | Where-Object State -eq "Established" }
```

---

## Key Takeaways

> `netstat -ano` cross-referenced with `tasklist /svc` is one of the fastest ways to identify malware. Unknown process making outbound connections to external IPs = start investigating immediately.

---

## References

- [MITRE ATT&CK T1059.001 PowerShell](https://attack.mitre.org/techniques/T1059/001/)
