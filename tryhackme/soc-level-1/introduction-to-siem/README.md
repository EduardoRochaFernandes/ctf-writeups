# Room: Introduction to SIEM

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SIEM
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/introtosiem

---

## What is this room about?

SIEM (Security Information and Event Management) is the central nervous system of a SOC. This room covers what a SIEM does, how it ingests logs, how detection rules work, and what makes it such a critical tool for analysts.

---

## What a SIEM Does

A SIEM does three things:
1. **Collects and stores** logs from every source in the environment — all in one place
2. **Normalises and correlates** logs so you can query across different systems uniformly
3. **Alerts in real time** when detection rules match

Popular SIEMs: **Splunk**, **Elastic Security**, **Microsoft Sentinel**, **IBM QRadar**.

---

## Log Sources

### Host-Centric
Events from the operating system and applications on a specific machine.

- **Windows Event Logs** — stored in Event Viewer. Every event type has a unique Event ID:
  - `4688` — New process created (with full command line if auditing enabled)
  - `4624/4625` — Successful/failed logon
  - `1102` — Security event log cleared (major red flag)
  - `104` — System log cleared

- **Linux** — logs in specific paths:
  - `/var/log/auth.log` — authentication events
  - `/var/log/httpd` or `/var/log/nginx` — web server access
  - `/var/log/cron` — scheduled tasks
  - `/var/log/kern` — kernel events

### Network-Centric
Events from network devices monitoring traffic between hosts.
- Firewalls, IDS/IPS, routers, web proxies, VPN

---

## Log Ingestion Methods

| Method | How it works |
|--------|-------------|
| **Agent/Forwarder** | Lightweight software installed on the endpoint that ships logs automatically |
| **Syslog** | Standard protocol for real-time log transmission from servers and network devices |
| **Manual Upload** | Import historical log files for offline analysis |
| **Port Forwarding** | SIEM listens on a port; endpoints forward directly to it |

---

## How Detection Rules Work

Rules are logical conditions on log fields. When the condition is met, an alert fires. Normalisation is critical — without consistent field names across log sources, rules can't match across systems.

**Examples:**

| Rule | What it detects |
|------|----------------|
| `EventID=1102` | Security log cleared — attacker covering tracks |
| `EventID=4688 AND process=whoami` | Typical post-exploitation enumeration |
| `Failed logins > 5 in 10s from same IP` | Brute force attempt |
| `Outbound traffic > 25MB` | Potential data exfiltration |
| `USB inserted on restricted system` | Policy violation |

---

## Key Takeaways

> The SIEM is only as good as its rules and the quality of the logs feeding it. Garbage in, garbage out.

What clicked for me in this room: normalisation is not just a nice-to-have — it's what makes correlation possible at all. If Windows calls it `EventID` and Linux calls it `syslog_priority`, you can't write a single rule that spans both without normalisation first.

---

## References

- [Splunk Documentation](https://docs.splunk.com/)
- [Elastic SIEM](https://www.elastic.co/security/siem)
- [MITRE ATT&CK — T1070.001 Clear Windows Event Logs](https://attack.mitre.org/techniques/T1070/001/)
