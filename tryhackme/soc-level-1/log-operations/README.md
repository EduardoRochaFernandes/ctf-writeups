# Room: Log Operations

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Log Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/logoperations

---

## What is this room about?

Knowing that logs exist is not enough — you need to be able to work with them. This room covers the practical side of log analysis: Windows Event Log structure, Linux log locations, and the command-line tools that let you slice through log files efficiently.

---

## Windows Event Logs

Stored at `C:\Windows\System32\winevt\Logs\` as `.evtx` files. Viewable with **Event Viewer** or alternative tools like **ULogViewer**.

### Structure of a Windows Event Log Entry

| Field | Description |
|-------|-------------|
| Log Name | Channel (Security, System, Application, etc.) |
| Source | Application or component that generated it |
| Event ID | Unique numeric identifier for the event type |
| Level | Information / Warning / Error / Critical / Verbose |
| User | Account that triggered the event |
| Logged | Timestamp |
| Task Category | Process Creation, Log Clear, etc. |
| Keywords | Audit Success / Audit Failure |
| Computer | Hostname |
| Message | Full event details |

The **PID (Process ID)** and **TID (Thread ID)** are essential for correlating events from the same process across multiple log entries.

### Critical Event IDs for Blue Team

| Category | Event ID | What it means |
|----------|----------|--------------|
| Account Management | 4720 | New account created |
| | 4722 / 4725 / 4726 | Account enabled / disabled / deleted |
| | 4723 / 4724 | Password changed / reset |
| Account Logon | 4624 | Successful logon |
| | 4625 | Failed logon (with reason code) |
| | 4634 / 4647 | Logoff |
| Scheduled Tasks | 4698 / 4702 / 4699 | Task created / updated / deleted |
| Security | 1102 | **Security log cleared** — major red flag |
| | 1116 | Malware detected |
| Process | 4688 | New process created |

---

## Linux Logs

Stored in `/var/log/` in cleartext (syslog-style) or binary (systemd journal — read with `journalctl`).

| File | Contents |
|------|---------|
| `/var/log/syslog` or `/var/log/messages` | General system events |
| `/var/log/auth.log` or `/var/log/secure` | Authentication events — SSH, sudo |
| `/var/log/kern.log` | Kernel messages |
| `/var/log/cron.log` | Scheduled task execution |
| `/var/log/faillog` | Failed login attempts (read with `faillog`) |
| `/var/log/wtmp` | Session history (read with `who`) |
| `/var/log/lastlog` | Last login per user (read with `lastlog`) |

---

## Command-Line Log Analysis

The real power for Linux log analysis is the combination of standard shell tools:

| Command | Common use |
|---------|-----------|
| `cat` | View full file |
| `less` | Navigate large files page by page |
| `tail -f` | Follow a log in real time |
| `grep "pattern"` | Filter lines matching a pattern |
| `grep -v "pattern"` | Exclude lines matching pattern |
| `cut -d' ' -f1` | Extract field 1 (space-delimited) |
| `sort` | Sort output alphabetically or numerically |
| `uniq -c` | Count unique occurrences |
| `awk '$9 >= 400'` | Filter by numeric field value |
| `wc -l` | Count lines |

### Common Pipelines

```bash
# Top 10 IPs by request count from Apache access log
cut -d' ' -f1 access.log | sort | uniq -c | sort -rn | head -10

# Find all failed SSH attempts
grep "Failed password" /var/log/auth.log

# Find all 404 errors in web log
grep " 404 " /var/log/nginx/access.log

# Extract all IP addresses from a file
grep -Eo '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' access.log

# Filter POST requests with 4xx response codes
grep '"POST ' access.log | awk '$9 >= 400'

# Find path traversal attempts
grep -E '\.\./|%2E%2E%2F' access.log
```

---

## Key Takeaways

> The shell pipeline (`cut | sort | uniq -c | sort -rn`) is one of the most powerful log analysis tools you have — and it requires no special software.

Windows Event ID 4625 (failed logon) with the reason code tells you exactly why authentication failed — wrong password, account disabled, logon type not permitted. Learning to read reason codes saves hours of investigation time.

---

## References

- [Windows Security Event IDs — Ultimate List](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/)
- [Linux Log Files Reference](https://www.thegeekstuff.com/2011/08/linux-var-log-files/)
