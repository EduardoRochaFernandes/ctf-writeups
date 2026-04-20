# SOC Workbooks and Lookups

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 02: SOC Team Internals
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Raw technical data from an alert is rarely sufficient to make a confident classification. Context — about the user involved, the system affected, and the network it operates on — transforms ambiguous data into a clear picture. This room covers the contextual resources that make alert investigation effective: identity inventories, asset inventories, network diagrams, and SOC workbooks.

---

## Identity Inventories

When an alert involves a user account, the first enrichment step is pulling account context from the identity system.

**Active Directory (on-premises):** The authoritative source for user accounts, groups, and computer objects in most enterprise Windows environments. Stored on Domain Controllers. Key attributes to check during investigation:
- Account type (standard user, service account, privileged/admin account)
- Group memberships (which systems and resources can this account access?)
- Last logon timestamp and logon history
- Account status (enabled, disabled, locked)
- Password last set date

**Cloud IAM / SSO providers:** Okta, Azure Active Directory, Google Workspace fulfil the same role in cloud-first or hybrid environments. Often include additional context such as device trust status, MFA method, and conditional access policy evaluation results.

**HR systems:** Can provide organisational context — department, manager, employment status, start/end dates. Useful for determining whether an account should still be active or whether its access level matches its current role.

---

## Asset Inventories

Understanding what a system does is essential for judging the significance of an alert involving it.

Key attributes for each asset:
- Hostname and IP address (static or DHCP-assigned)
- Operating system and version
- Purpose and criticality (web server, database, developer workstation, finance system)
- Owner — which team is responsible for it
- Network location — which segment, subnet, or security zone

**Sources of asset data:** Active Directory (for domain-joined systems), SIEM agent inventory, EDR deployment console, vulnerability scanner asset database, CMDB (Configuration Management Database).

---

## Network Diagrams

When an alert involves IP addresses and network traffic, a network diagram converts raw addressing into spatial context. Without it, a sequence of connection events is difficult to interpret. With it, the same events tell a clear story.

**Worked example:**

Without diagram context:
```
External IP 103.61.240.174 connects to internal port 10443
Translated to 10.10.0.53
10.10.0.53 scans 172.16.15.0/24
```

With diagram context (knowing that 10443 is the VPN endpoint, 10.10.0.53 is in the VPN pool, 172.16.15.0/24 is the database segment):
```
08:00 — Attacker executes brute force against the corporate VPN endpoint
08:23 — Brute force succeeds. Attacker receives VPN IP 10.10.0.53
08:25 — Attacker begins reconnaissance of the database subnet
08:32 — Pivots to the office subnet after database access is blocked by firewall
```

The diagram made it possible to assign meaning to each event and construct a timeline.

---

## SOC Workbooks

A SOC workbook is a structured procedure document for a specific alert type. It defines exactly how an analyst should investigate, classify, and respond to that category of alert — removing ambiguity and ensuring consistency regardless of who is on shift.

A complete workbook covers:

1. **Enrichment** — what context to gather before investigating (user account lookup, asset inventory, IP reputation)
2. **Investigation** — specific SIEM queries to run, fields to examine, indicators to look for
3. **Classification criteria** — explicit conditions that constitute a true positive for this alert type
4. **Escalation path** — when and how to escalate, what to include in the escalation note
5. **Response actions** — immediate containment steps the L1 analyst is authorised to take

Workbooks reduce the time to complete an investigation, reduce the error rate on classifications, and make the onboarding of new analysts faster.

---

## Key Takeaways

The difference between an analyst who closes a case quickly with high confidence and one who spends an hour on the same case is often access to contextual resources. Investing time at the start of a new role to understand where the identity inventory is, where the asset inventory is, and where the network diagrams are — and building relationships with the people who maintain them — pays dividends on every investigation that follows.
