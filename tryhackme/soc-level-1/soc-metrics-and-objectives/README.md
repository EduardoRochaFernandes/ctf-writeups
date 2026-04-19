# Room: SOC Metrics and Objectives

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** SOC Fundamentals
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/socmetricsandobjectives

---

## What is this room about?

How do you know if your SOC is doing a good job? Through metrics. This room introduces the four core performance metrics for L1 analysts and the time-based SLA metrics that govern how quickly alerts must be handled.

---

## The Four Core Metrics

### 1. Alerts Count (Volume)

Total alerts received per day. Both extremes are problematic:
- **Too many** (80+/day per analyst) → alert fatigue, real threats buried in noise
- **Too few** → possible SIEM misconfiguration, lack of visibility, or actual silence (which itself might mean attacks are succeeding undetected)

**Healthy range:** 5–30 alerts per analyst per day.

### 2. False Positive Rate

`False Positives ÷ Total Alerts`

The most dangerous operational risk in a SOC. When 90%+ of alerts are false positives, analysts develop **alert fatigue** — they start treating every alert as noise, which is exactly when a real attack slips through. 

**Target:** Below 20% ideally. Above 80% requires urgent rule tuning (**False Positive Remediation** — reviewing and updating detection rules, automation scripts, and SIEM configurations).

### 3. Alert Escalation Rate

`Escalated Alerts ÷ Total Alerts`

Measures the balance between autonomy and appropriate escalation.
- **Too high** → L1 is overdependent on L2, not building skills
- **Too low** → L1 is overconfident, potentially closing alerts that need L2 review

**Target:** Below 20–50% depending on team maturity.

### 4. Threat Detection Rate (Most Critical)

`Threats Detected ÷ Total Real Threats`

The only metric that truly measures whether the SOC is doing its job. A 67% TDR means 1 in 3 real attacks goes undetected. There is no acceptable threshold below 100% — every undetected threat is a potential ransomware attack, data breach, or worse.

---

## Time-Based SLA Metrics

SLAs (Service Level Agreements) define the maximum time allowed for each phase of incident handling:

| Metric | Full Name | Target | What it measures |
|--------|-----------|--------|-----------------|
| **MTTD** | Mean Time To Detect | ≤ 5 min | Time from attack start to SIEM alert firing |
| **MTTA** | Mean Time To Acknowledge | ≤ 10 min | Time from alert to analyst starting investigation |
| **MTTR** | Mean Time To Respond | ≤ 1 hour | Time from detection to remediation complete |

**When SLAs are breached:**
- High MTTD → engineering problem, contact SOC Engineers to tune SIEM and review sensor coverage
- High MTTA → notification or staffing problem, review SIEM alert delivery and analyst workload distribution
- High MTTR → depends on incident complexity; for common cases, review playbooks and automation

---

## Key Takeaways

> Metrics without action are just numbers. The value of tracking MTTD and false positive rates is that they tell you exactly where to improve.

The metric I found most eye-opening is the False Positive Rate — not because a high rate is surprising, but because of *what it does to human behaviour*. Alert fatigue is a psychological phenomenon, not just a productivity problem. A SOC with 90% false positives isn't just inefficient — it's dangerous.

---

## References

- [TryHackMe SOC Metrics and Objectives](https://tryhackme.com/room/socmetricsandobjectives)
