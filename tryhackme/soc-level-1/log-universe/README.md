# Room: Log Universe

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Log Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/loguniverse

---

## What is this room about?

Exploration of logs from different system types — web servers, authentication systems, Windows Event Logs, network devices. Builds the breadth needed for the variety of log types in a real SOC.

---

## Web Server Logs (Apache Combined Format)

```
IP - user [timestamp] "METHOD /path HTTP/1.1" status bytes "referer" "user-agent"
```

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10   # Top IPs
awk '$9 ~ /^5/' access.log    # Server errors (5xx)
awk '$9 ~ /^4/' access.log    # Client errors (4xx)
```

---

## Auth Logs (Linux)

```bash
grep "Failed password" /var/log/auth.log | grep -oE 'from [0-9.]+' | sort | uniq -c | sort -rn
grep "Accepted password" /var/log/auth.log    # Successful logins
grep "sudo" /var/log/auth.log | grep COMMAND  # Privilege use
```

---

## Windows Event Logs (PowerShell)

```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625}  # Failed logons
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4688}  # Process creation
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=1102}  # Log cleared
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; Id=4104}
```

---

## Network Device Log Patterns

| Pattern | Indicator |
|---------|-----------|
| High outbound volume to external IP | Data exfiltration |
| Regular intervals to same external IP | Malware beaconing |
| Internal hosts scanning other internal hosts | Lateral movement |
| Multiple authentication failures | Brute force |

---

## Key Takeaways

> Web logs tell you what was requested. Auth logs tell you who authenticated. Network logs tell you where they went. You need all three to reconstruct an attack chain.

---

## References

- [SANS Log Management](https://www.sans.org/reading-room/whitepapers/logging/)
