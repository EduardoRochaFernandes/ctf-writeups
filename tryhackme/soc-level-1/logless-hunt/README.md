# Room: Logless Hunt

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Log Analysis
**Difficulty:** Medium
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/loglesshunt

---

## What is this room about?

The attacker cleared the Windows Security Event Log (Event ID 1102). Can you still reconstruct what happened? Teaches alternative log sources and investigation techniques for when primary logs are gone.

---

## Alternative Sources When Security Log is Cleared

### PowerShell History File
`%AppData%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`

Interactive commands are logged here even after Security log clearing.

### Sysmon Logs
`Microsoft-Windows-Sysmon/Operational`

Completely independent channel. Clearing Security log doesn't affect Sysmon. Process activity, file creation, network connections, registry changes all preserved.

### Windows Defender Logs
`Apps and Services Logs > Microsoft > Windows > Windows Defender > Operational`

Events 1116/1117 (threat detected/actioned) independent of Security log.

### RDP Logs
`TerminalServices-LocalSessionManager/Operational`
Events: 21 (logon), 24 (disconnect), 25 (reconnect).

### Prefetch Files
`C:\Windows\Prefetch\` — metadata about recently executed programs. If mimikatz.exe ran, the prefetch file exists. Tool: WinPrefetchView.

---

## Splunk Investigation Without Security Logs

```splunk
index=win (EventCode=4104 OR EventCode=1116 OR EventCode=21)
| table _time, EventCode, host, Message | sort _time

index=win EventCode=4104 Message="*wevtutil*"

index=win EventCode=1
| search Image IN ("*mimikatz*", "*procdump*", "*wce*")
```

---

## Key Takeaways

> Layered logging across independent channels ensures no single deletion destroys your visibility. Sysmon + forwarded logs + Defender logs = no single point of failure.

---

## References

- [MITRE ATT&CK T1070.001 Clear Windows Event Logs](https://attack.mitre.org/techniques/T1070/001/)
