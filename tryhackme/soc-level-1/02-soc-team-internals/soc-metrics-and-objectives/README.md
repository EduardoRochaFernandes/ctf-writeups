# SOC Metrics and Objectives

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 02: SOC Team Internals
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

How does a SOC know if it is performing well? Through measurable metrics that track both the volume and quality of analyst work. This room covers the four core performance metrics for L1 analysts and the time-based SLAs that govern how quickly alerts must be handled.

---

## Core Performance Metrics

### Alerts Count — Volume

Total alerts received per analyst per day. Both extremes are problematic:

- **Too high (80+ per analyst per day):** Analysts become overwhelmed. Alert fatigue sets in — the psychological state where the volume of noise causes analysts to treat every alert with reduced attention. This is when real threats are most likely to be missed.
- **Too low:** May indicate a monitoring gap — sensors not collecting, agents not reporting, or an attacker who has disabled logging.

Healthy range: **5–30 alerts per analyst per day** in a well-tuned environment.

### False Positive Rate

`False Positives / Total Alerts`

The most operationally dangerous metric when poorly managed. A 90% false positive rate does not just waste analyst time — it creates the conditions for alert fatigue that allows genuine attacks to pass unnoticed.

**Target:** Below 20% ideally. Above 80% requires immediate remediation of detection rules.

**False Positive Remediation:** The process of reviewing overfiring detection rules, updating them to reduce noise without sacrificing coverage. Typically involves adding exceptions for known-good behaviour, tightening field conditions, or adding time-window thresholds.

### Alert Escalation Rate

`Escalated Alerts / Total Alerts`

Tracks whether L1 analysts are using appropriate judgment about escalation:

- **Too high:** L1 is over-relying on L2, not developing autonomy, and creating unnecessary L2 workload
- **Too low:** L1 may be closing alerts that require deeper investigation, potentially missing genuine breaches

Target: **Below 20–50%** depending on alert mix and team experience level.

### Threat Detection Rate

`Threats Detected / Total Actual Threats`

The most critical metric. Measures whether the SOC is actually catching what it should. A 67% detection rate means one in three real attacks is going undetected.

There is no acceptable threshold below 100%. Every undetected threat is a potential breach waiting to be discovered through other means — or not discovered at all.

---

## Time-Based SLA Metrics

Service Level Agreements define maximum acceptable times for each phase of alert handling:

| Metric | Name | Target | What It Measures |
|--------|------|--------|-----------------|
| MTTD | Mean Time To Detect | 5 minutes | From attack start to alert firing |
| MTTA | Mean Time To Acknowledge | 10 minutes | From alert arrival to analyst beginning work |
| MTTR | Mean Time To Respond | 1 hour | From detection to containment/remediation |

**When MTTD is persistently high:** Engineering problem. Contact the SOC engineering team to review sensor coverage, SIEM ingestion latency, and detection rule performance.

**When MTTA is persistently high:** Staffing or notification problem. Review whether alerts are being routed to analysts effectively and whether shift coverage is adequate.

**When MTTR is persistently high:** May indicate process inefficiency, missing runbooks, or that alert classification is taking too long. Review the triage workflow and playbook quality.

---

## Key Takeaways

Metrics without action are just numbers. The purpose of tracking these figures is to identify which part of the detection and response pipeline is underperforming and direct improvement effort there. A SOC that reviews its metrics regularly and acts on what they reveal will consistently outperform one that does not, regardless of the tools in use.

---

## References

- [SANS SOC Survey Metrics](https://www.sans.org/reading-room/whitepapers/analyst/paper/38240)
