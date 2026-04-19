# Room: Intro to Log Analysis

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Log Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/introloganalysis

---

## What is this room about?

Hands-on log analysis using command-line tools. The practical companion to Intro to Logs — analysing real log files to find attack patterns.

---

## Core Analysis Pipeline

```bash
# Top IPs by request count
cut -d' ' -f1 access.log | sort | uniq -c | sort -rn | head -20

# Failed SSH attempts per IP
grep "Failed password" /var/log/auth.log | grep -oE "from [0-9.]+" | sort | uniq -c | sort -rn

# HTTP errors per IP
awk '$9 >= 400 {print $1}' access.log | sort | uniq -c | sort -rn

# SQL injection patterns
grep -iE "union|select|--|%27" access.log

# Path traversal
grep -iE "\.\./|%2E%2E|etc/passwd" access.log

# Extract all IPs from file
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' access.log
```

---

## Common Attack Patterns in Logs

| Pattern | Attack type |
|---------|------------|
| Many 404s from same IP | Directory enumeration |
| SQL keywords in params | SQL injection |
| ../../../etc/passwd in URI | Path traversal |
| Script tags in params | XSS |
| Identical timestamps, many requests | Automated tool |

---

## Log Analysis Workflow

1. **Orient** — log type, format, time range
2. **Baseline** — what does normal look like?
3. **Find anomalies** — what deviates from baseline?
4. **Investigate** — malicious or just unusual?
5. **Extract IoCs** — IPs, domains, hashes
6. **Document** — evidence trail for the report

---

## Key Takeaways

> `cut | sort | uniq -c | sort -rn` is one of the most powerful log analysis pipelines available. Requires no special software. Works on any Unix system. Learn it cold.

---

## References

- [SANS Log Analysis Cheat Sheet](https://www.sans.org/blog/the-ultimate-list-of-sans-cheat-sheets/)
