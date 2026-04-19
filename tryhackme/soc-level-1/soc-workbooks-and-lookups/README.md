# Room: SOC Workbooks and Lookups

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SOC Fundamentals
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/socworkbooksandlookups

---

## What is this room about?

This room covers the corporate resources that help analysts do their job faster and with more context — identity inventories, asset inventories, network diagrams, and SOC workbooks. Raw technical data from an alert is rarely enough to make a good decision; you always need context.

---

## Identity and Asset Inventories

### Identity Systems

In most enterprises, **Active Directory (AD)** is the central identity store — it runs on dedicated servers called **Domain Controllers** and holds account information for every authenticated user. When you get an alert about an account, AD is your first stop for context:
- Is this account an admin or a regular user?
- Is the account enabled or disabled?
- What groups does it belong to?
- When was it last used?

In cloud-first companies, **SSO providers** (Okta, Google Workspace, Azure AD) serve the same role. HR systems can also have valuable user context (department, manager, employment status) but may be less precise than AD.

### Asset Inventory

A list of all computing resources in the organisation — servers, workstations, laptops. For each asset you ideally know:
- Hostname and IP
- Operating system and version
- Owner (user or team)
- Purpose (web server, developer workstation, finance system)
- Physical or cloud location

Both AD and SIEM/EDR agents usually collect this automatically.

---

## Network Diagrams in Alert Investigation

When an alert involves IP addresses and network traffic, a network diagram turns raw numbers into a meaningful story.

**Without a diagram**, a sequence like this is almost impossible to interpret:
- External IP `103.61.240.174` connects to port 10443
- Gets translated to internal IP `10.10.0.53`
- That internal host starts scanning `172.16.15.0/24`

**With a diagram** — knowing that port 10443 is the VPN endpoint, that `10.10.0.53` is in the VPN subnet, and that `172.16.15.0/24` is the database network — the same sequence tells a clear story:

```
08:00 — Attacker brute-forces the VPN
08:23 — Success. Attacker gets VPN IP 10.10.0.53
08:25 — Attacker scans database subnet (blocked by firewall)
08:32 — Pivots to office subnet instead
```

---

## SOC Workbooks

A SOC workbook is a structured document that defines exactly how to investigate, classify, and respond to a specific alert type. Think of it as a recipe for handling each kind of incident.

A good workbook covers:
1. **Enrichment** — what context to gather (user info, asset info, IP reputation)
2. **Investigation** — specific queries to run, fields to check, indicators to look for
3. **Classification** — criteria for True Positive vs False Positive
4. **Escalation** — when and how to escalate, what information to include

Workbooks make the SOC consistent — a new L1 analyst handles an alert the same way an experienced one would.

---

## Key Takeaways

> Technical skills get you to the data. Context — from identity systems, asset inventories, and network diagrams — tells you what the data means.

The biggest lesson from this room: before you try to interpret an IP address or a process, find out *what that IP or process is in your environment*. Context transforms noise into signal.

---

## References

- [TryHackMe SOC Workbooks and Lookups](https://tryhackme.com/room/socworkbooksandlookups)
