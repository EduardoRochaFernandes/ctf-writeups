#!/usr/bin/env python3
"""
update_issues.py

1. Updates the 5 closed issues whose rooms moved from supplementary
   to their correct path (edits title + body, keeps closed)
2. Updates the 3 open progress tracking issues (SOC1/2/3)
3. Creates 2 new open progress tracking issues (Security Engineer, DevSecOps)
4. Creates new closed issues for all new rooms in SOC2, SOC3, SE, DevSecOps

Usage:
    python update_issues.py --repo EduardoRochaFernandes/ctf-writeups
"""

import argparse, os, sys, time
from github import Github, Auth

TOKEN = os.getenv("GITHUB_TOKEN", "")

# ── Rooms that moved from supplementary ──────────────────────────────
MOVED_ROOMS = [
    {
        "old_title_contains": "[Supplementary] intro-to-logs",
        "new_title": "[SOC Level 2 — 01 — Log Analysis] intro-to-logs",
        "new_section": "01 — Log Analysis",
        "new_path": "soc-level-2/01-log-analysis/intro-to-logs/README.md",
        "new_path_name": "SOC Level 2",
        "slug": "introtologs",
    },
    {
        "old_title_contains": "[Supplementary] log-operations",
        "new_title": "[SOC Level 2 — 01 — Log Analysis] log-operations",
        "new_section": "01 — Log Analysis",
        "new_path": "soc-level-2/01-log-analysis/log-operations/README.md",
        "new_path_name": "SOC Level 2",
        "slug": "logoperations",
    },
    {
        "old_title_contains": "[Supplementary] intro-to-log-analysis",
        "new_title": "[SOC Level 2 — 01 — Log Analysis] intro-to-log-analysis",
        "new_section": "01 — Log Analysis",
        "new_path": "soc-level-2/01-log-analysis/intro-to-log-analysis/README.md",
        "new_path_name": "SOC Level 2",
        "slug": "introloganalysis",
    },
    {
        "old_title_contains": "[Supplementary] windows-internals",
        "new_title": "[SOC Level 3 — 03 — Windows Endpoint Investigation] windows-internals",
        "new_section": "03 — Windows Endpoint Investigation",
        "new_path": "soc-level-3/03-windows-endpoint-investigation/windows-internals/README.md",
        "new_path_name": "SOC Level 3",
        "slug": "windowsinternals",
    },
    {
        "old_title_contains": "[Supplementary] logless-hunt",
        "new_title": "[SOC Level 3 — 03 — Windows Endpoint Investigation] logless-hunt",
        "new_section": "03 — Windows Endpoint Investigation",
        "new_path": "soc-level-3/03-windows-endpoint-investigation/logless-hunt/README.md",
        "new_path_name": "SOC Level 3",
        "slug": "loglesshunt",
    },
]

# ── New progress tracking issues ──────────────────────────────────────
NEW_PROGRESS = [
    {
        "title": "track: Security Engineer — learning progress",
        "body": (
            "## Security Engineer — TryHackMe\n\n"
            "Tracks progress through the TryHackMe Security Engineer path.\n\n"
            "**Status:** Planned.\n\n"
            "**Path:** https://tryhackme.com/path/outline/security-engineer-training\n\n"
            "## Sections\n\n"
            "- Section 01: Introduction to Security Engineering\n"
            "- Section 02: Threats and Risks\n"
            "- Section 03: Network and System Security\n"
            "- Section 04: Software Security\n"
            "- Section 05: Managing Incidents\n"
            "- Section 06: OWASP Top 10 (2025)\n\n"
            "This issue remains open until the full path is complete."
        ),
    },
    {
        "title": "track: DevSecOps — learning progress",
        "body": (
            "## DevSecOps — TryHackMe\n\n"
            "Tracks progress through the TryHackMe DevSecOps path.\n\n"
            "**Status:** Planned.\n\n"
            "**Path:** https://tryhackme.com/path/outline/devsecops\n\n"
            "## Sections\n\n"
            "- Section 01: Secure Software Development\n"
            "- Section 02: Security of the Pipeline\n"
            "- Section 03: Security in the Pipeline\n"
            "- Section 04: Container Security\n"
            "- Section 05: Infrastructure as Code\n\n"
            "This issue remains open until the full path is complete."
        ),
    },
]

# ── New room issues for all new paths ────────────────────────────────
NEW_ROOM_ISSUES = []

soc2_rooms = [
    ("01 — Log Analysis", "splunk-exploring-spl", "soc-level-2/01-log-analysis/splunk-exploring-spl/README.md"),
    ("01 — Log Analysis", "splunk-setting-up-a-soc-lab", "soc-level-2/01-log-analysis/splunk-setting-up-a-soc-lab/README.md"),
    ("01 — Log Analysis", "splunk-dashboards-and-reports", "soc-level-2/01-log-analysis/splunk-dashboards-and-reports/README.md"),
    ("01 — Log Analysis", "splunk-data-manipulation", "soc-level-2/01-log-analysis/splunk-data-manipulation/README.md"),
    ("01 — Log Analysis", "fixit", "soc-level-2/01-log-analysis/fixit/README.md"),
    ("02 — Advanced Splunk", "splunk-exploring-spl", "soc-level-2/02-advanced-splunk/splunk-exploring-spl/README.md"),
    ("02 — Advanced Splunk", "splunk-setting-up-a-soc-lab", "soc-level-2/02-advanced-splunk/splunk-setting-up-a-soc-lab/README.md"),
    ("02 — Advanced Splunk", "splunk-dashboards-and-reports", "soc-level-2/02-advanced-splunk/splunk-dashboards-and-reports/README.md"),
    ("02 — Advanced Splunk", "splunk-data-manipulation", "soc-level-2/02-advanced-splunk/splunk-data-manipulation/README.md"),
    ("02 — Advanced Splunk", "fixit", "soc-level-2/02-advanced-splunk/fixit/README.md"),
    ("03 — Advanced ELK", "elastic-using-logstash", "soc-level-2/03-advanced-elk/elastic-using-logstash/README.md"),
    ("03 — Advanced ELK", "custom-alert-rules-in-wazuh", "soc-level-2/03-advanced-elk/custom-alert-rules-in-wazuh/README.md"),
    ("03 — Advanced ELK", "elastic-query-languages", "soc-level-2/03-advanced-elk/elastic-query-languages/README.md"),
    ("03 — Advanced ELK", "slingshot", "soc-level-2/03-advanced-elk/slingshot/README.md"),
    ("04 — Detection Engineering", "intro-to-detection-engineering", "soc-level-2/04-detection-engineering/intro-to-detection-engineering/README.md"),
    ("04 — Detection Engineering", "tactical-detection", "soc-level-2/04-detection-engineering/tactical-detection/README.md"),
    ("04 — Detection Engineering", "threat-intelligence-for-soc", "soc-level-2/04-detection-engineering/threat-intelligence-for-soc/README.md"),
    ("04 — Detection Engineering", "sigma", "soc-level-2/04-detection-engineering/sigma/README.md"),
    ("04 — Detection Engineering", "sighunt", "soc-level-2/04-detection-engineering/sighunt/README.md"),
    ("04 — Detection Engineering", "aurora-edr", "soc-level-2/04-detection-engineering/aurora-edr/README.md"),
    ("04 — Detection Engineering", "introduction-to-soar", "soc-level-2/04-detection-engineering/introduction-to-soar/README.md"),
    ("05 — Threat Hunting", "threat-hunting-introduction", "soc-level-2/05-threat-hunting/threat-hunting-introduction/README.md"),
    ("05 — Threat Hunting", "threat-hunting-foothold", "soc-level-2/05-threat-hunting/threat-hunting-foothold/README.md"),
    ("05 — Threat Hunting", "threat-hunting-pivoting", "soc-level-2/05-threat-hunting/threat-hunting-pivoting/README.md"),
    ("05 — Threat Hunting", "threat-hunting-endgame", "soc-level-2/05-threat-hunting/threat-hunting-endgame/README.md"),
    ("05 — Threat Hunting", "hunt-me-i-payment-collectors", "soc-level-2/05-threat-hunting/hunt-me-i-payment-collectors/README.md"),
    ("05 — Threat Hunting", "hunt-me-ii-typo-squatters", "soc-level-2/05-threat-hunting/hunt-me-ii-typo-squatters/README.md"),
    ("05 — Threat Hunting", "health-hazard", "soc-level-2/05-threat-hunting/health-hazard/README.md"),
    ("05 — Threat Hunting", "typo-snare", "soc-level-2/05-threat-hunting/typo-snare/README.md"),
    ("06 — Threat Emulation", "intro-to-threat-emulation", "soc-level-2/06-threat-emulation/intro-to-threat-emulation/README.md"),
    ("06 — Threat Emulation", "threat-modelling", "soc-level-2/06-threat-emulation/threat-modelling/README.md"),
    ("06 — Threat Emulation", "atomic-red-team", "soc-level-2/06-threat-emulation/atomic-red-team/README.md"),
    ("06 — Threat Emulation", "caldera", "soc-level-2/06-threat-emulation/caldera/README.md"),
    ("06 — Threat Emulation", "atomic-bird-goes-purple-1", "soc-level-2/06-threat-emulation/atomic-bird-goes-purple-1/README.md"),
    ("06 — Threat Emulation", "atomic-bird-goes-purple-2", "soc-level-2/06-threat-emulation/atomic-bird-goes-purple-2/README.md"),
    ("07 — Incident Response", "preparation", "soc-level-2/07-incident-response/preparation/README.md"),
    ("07 — Incident Response", "identification-and-scoping", "soc-level-2/07-incident-response/identification-and-scoping/README.md"),
    ("07 — Incident Response", "threat-intel-and-containment", "soc-level-2/07-incident-response/threat-intel-and-containment/README.md"),
    ("07 — Incident Response", "eradication-and-remediation", "soc-level-2/07-incident-response/eradication-and-remediation/README.md"),
    ("07 — Incident Response", "lessons-learned", "soc-level-2/07-incident-response/lessons-learned/README.md"),
    ("07 — Incident Response", "tardigrade", "soc-level-2/07-incident-response/tardigrade/README.md"),
    ("08 — Malware Analysis", "x86-architecture-overview", "soc-level-2/08-malware-analysis/x86-architecture-overview/README.md"),
    ("08 — Malware Analysis", "x86-assembly-crash-course", "soc-level-2/08-malware-analysis/x86-assembly-crash-course/README.md"),
    ("08 — Malware Analysis", "dissecting-pe-headers", "soc-level-2/08-malware-analysis/dissecting-pe-headers/README.md"),
    ("08 — Malware Analysis", "basic-static-analysis", "soc-level-2/08-malware-analysis/basic-static-analysis/README.md"),
    ("08 — Malware Analysis", "malbuster", "soc-level-2/08-malware-analysis/malbuster/README.md"),
    ("08 — Malware Analysis", "advanced-static-analysis", "soc-level-2/08-malware-analysis/advanced-static-analysis/README.md"),
    ("08 — Malware Analysis", "basic-dynamic-analysis", "soc-level-2/08-malware-analysis/basic-dynamic-analysis/README.md"),
    ("08 — Malware Analysis", "dynamic-analysis-debugging", "soc-level-2/08-malware-analysis/dynamic-analysis-debugging/README.md"),
    ("08 — Malware Analysis", "anti-reverse-engineering", "soc-level-2/08-malware-analysis/anti-reverse-engineering/README.md"),
    ("08 — Malware Analysis", "maldoc-static-analysis", "soc-level-2/08-malware-analysis/maldoc-static-analysis/README.md"),
]
for s, r, p in soc2_rooms:
    NEW_ROOM_ISSUES.append(("[SOC Level 2", s, r, p, "SOC Level 2"))

soc3_rooms = [
    ("01 — File System Analysis", "mbr-and-gpt-analysis"), ("01 — File System Analysis", "fat32-analysis"),
    ("01 — File System Analysis", "ntfs-analysis"), ("01 — File System Analysis", "ext-analysis"),
    ("01 — File System Analysis", "file-carving"), ("01 — File System Analysis", "diskrupt"),
    ("02 — Linux Endpoint Investigation", "linux-incident-surface"), ("02 — Linux Endpoint Investigation", "linux-process-analysis"),
    ("02 — Linux Endpoint Investigation", "linux-logs-investigations"), ("02 — Linux Endpoint Investigation", "linux-live-analysis"),
    ("02 — Linux Endpoint Investigation", "ironshade"),
    ("03 — Windows Endpoint Investigation", "windows-incident-surface"), ("03 — Windows Endpoint Investigation", "compromised-windows-analysis"),
    ("03 — Windows Endpoint Investigation", "windows-user-account-forensics"), ("03 — Windows Endpoint Investigation", "windows-user-activity-analysis"),
    ("03 — Windows Endpoint Investigation", "expediting-registry-analysis"), ("03 — Windows Endpoint Investigation", "windows-applications-forensics"),
    ("03 — Windows Endpoint Investigation", "windows-network-analysis"), ("03 — Windows Endpoint Investigation", "blizzard"),
    ("04 — macOS Forensics", "macos-forensics-the-basics"), ("04 — macOS Forensics", "macos-forensics-artefacts"),
    ("04 — macOS Forensics", "macos-forensics-applications"), ("04 — macOS Forensics", "mac-hunt"),
    ("05 — Mobile Analysis", "mobile-acquisition"), ("05 — Mobile Analysis", "android-analysis"), ("05 — Mobile Analysis", "ios-analysis"),
    ("06 — Memory Analysis", "memory-analysis-introduction"), ("06 — Memory Analysis", "memory-acquisition"),
    ("06 — Memory Analysis", "volatility-essentials"), ("06 — Memory Analysis", "windows-memory-and-processes"),
    ("06 — Memory Analysis", "windows-memory-and-user-activity"), ("06 — Memory Analysis", "windows-memory-and-network"),
    ("06 — Memory Analysis", "linux-memory-analysis"), ("06 — Memory Analysis", "supplemental-memory"),
    ("07 — Disk Image Analysis", "intro-to-cold-system-forensics"), ("07 — Disk Image Analysis", "forensic-imaging"),
    ("07 — Disk Image Analysis", "autopsy"), ("07 — Disk Image Analysis", "diskfiltration"), ("07 — Disk Image Analysis", "exfilnode"),
    ("08 — Honeynet Collapse", "initial-access-pot"), ("08 — Honeynet Collapse", "elevating-movement"),
    ("08 — Honeynet Collapse", "lost-in-ramslation"), ("08 — Honeynet Collapse", "crm-snatch"),
    ("08 — Honeynet Collapse", "shock-and-silence"), ("08 — Honeynet Collapse", "the-last-trial"),
]
for s, r in soc3_rooms:
    sec = s.split(" — ")[0].lower().replace(" ", "-")
    p = f"soc-level-3/{sec}-{s.split(' — ')[1].lower().replace(' ', '-')}/{r}/README.md"
    NEW_ROOM_ISSUES.append(("[SOC Level 3", s, r, p, "SOC Level 3"))

se_rooms = [
    ("01 — Introduction to Security Engineering", "security-engineer-intro"),
    ("01 — Introduction to Security Engineering", "security-principles"),
    ("01 — Introduction to Security Engineering", "introduction-to-cryptography"),
    ("01 — Introduction to Security Engineering", "identity-and-access-management"),
    ("02 — Threats and Risks", "governance-and-regulation"), ("02 — Threats and Risks", "threat-modelling"),
    ("02 — Threats and Risks", "risk-management"), ("02 — Threats and Risks", "vulnerability-management"),
    ("03 — Network and System Security", "secure-network-architecture"), ("03 — Network and System Security", "linux-system-hardening"),
    ("03 — Network and System Security", "microsoft-windows-hardening"), ("03 — Network and System Security", "active-directory-hardening"),
    ("03 — Network and System Security", "network-device-hardening"), ("03 — Network and System Security", "network-security-protocols"),
    ("03 — Network and System Security", "virtualization-and-containers"), ("03 — Network and System Security", "intro-to-cloud-security"),
    ("03 — Network and System Security", "auditing-and-monitoring"),
    ("04 — Software Security", "owasp-api-security-top-10-1"), ("04 — Software Security", "owasp-api-security-top-10-2"),
    ("04 — Software Security", "ssdlc"), ("04 — Software Security", "sast"), ("04 — Software Security", "dast"),
    ("04 — Software Security", "weaponizing-vulnerabilities"), ("04 — Software Security", "introduction-to-devsecops"),
    ("04 — Software Security", "mothers-secret"), ("04 — Software Security", "traverse"),
    ("05 — Managing Incidents", "intro-to-ir-and-im"), ("05 — Managing Incidents", "logging-for-accountability"),
    ("05 — Managing Incidents", "becoming-a-first-responder"), ("05 — Managing Incidents", "cyber-crisis-management"),
    ("06 — OWASP Top 10 2025", "owasp-top-10-2025-iaaa-failures"),
    ("06 — OWASP Top 10 2025", "owasp-top-10-2025-application-design-flaws"),
    ("06 — OWASP Top 10 2025", "owasp-top-10-2025-insecure-data-handling"),
]
for s, r in se_rooms:
    p = f"security-engineer/{r}/README.md"
    NEW_ROOM_ISSUES.append(("[Security Engineer", s, r, p, "Security Engineer"))

dso_rooms = [
    ("01 — Secure Software Development", "introduction-to-devsecops"),
    ("01 — Secure Software Development", "sdlc"), ("01 — Secure Software Development", "ssdlc"),
    ("02 — Security of the Pipeline", "intro-to-pipeline-automation"),
    ("02 — Security of the Pipeline", "source-code-security"), ("02 — Security of the Pipeline", "ci-cd-and-build-security"),
    ("03 — Security in the Pipeline", "dependency-management"),
    ("03 — Security in the Pipeline", "sast"), ("03 — Security in the Pipeline", "dast"),
    ("03 — Security in the Pipeline", "mothers-secret"),
    ("04 — Container Security", "intro-to-containerisation"), ("04 — Container Security", "intro-to-docker"),
    ("04 — Container Security", "intro-to-kubernetes"), ("04 — Container Security", "container-vulnerabilities"),
    ("04 — Container Security", "container-hardening"),
    ("05 — Infrastructure as Code", "intro-to-iac"),
    ("05 — Infrastructure as Code", "on-premises-iac"), ("05 — Infrastructure as Code", "cloud-based-iac"),
]
for s, r in dso_rooms:
    p = f"devsecops/{r}/README.md"
    NEW_ROOM_ISSUES.append(("[DevSecOps", s, r, p, "DevSecOps"))


def room_body(path_prefix, section, slug, file_path, repo_name):
    writeup_url = f"https://github.com/{repo_name}/blob/main/{file_path}"
    folder = file_path.split("/")[0]
    return (
        f"## Room Details\n\n"
        f"| Field | Value |\n"
        f"|-------|-------|\n"
        f"| **Platform** | TryHackMe |\n"
        f"| **Folder** | `{folder}` |\n"
        f"| **Section** | {section} |\n"
        f"| **Room slug** | `{slug}` |\n"
        f"| **Status** | Pending |\n\n"
        f"## Writeup\n\n"
        f"[{file_path}]({writeup_url})\n\n"
        f"---\n\n"
        f"Closed upon writeup creation."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not TOKEN:
        print("Set GITHUB_TOKEN"); sys.exit(1)

    g = Github(auth=Auth.Token(TOKEN))
    repo = g.get_repo(args.repo)
    print(f"Connected: {repo.full_name}")

    all_issues = {i.title: i for i in repo.get_issues(state="all")}

    if args.dry_run:
        print(f"\nDRY RUN:")
        print(f"  {len(MOVED_ROOMS)} issues to update (title + body)")
        print(f"  {len(NEW_PROGRESS)} new open progress issues")
        print(f"  {len(NEW_ROOM_ISSUES)} new closed room issues")
        return

    # 1. Update moved room issues
    print("\n-- Updating moved room issues --")
    for spec in MOVED_ROOMS:
        match = next((i for t, i in all_issues.items() if spec["old_title_contains"] in t), None)
        if match:
            new_body = room_body(
                spec["new_path_name"], spec["new_section"],
                spec["old_title_contains"].replace("[Supplementary] ", ""),
                spec["new_path"], args.repo
            )
            match.edit(title=spec["new_title"], body=new_body)
            print(f"  Updated #{match.number}: {spec['new_title'][:70]}")
            time.sleep(0.8)
        else:
            print(f"  NOT FOUND: {spec['old_title_contains']}")

    # 2. New progress tracking issues
    print("\n-- Creating new progress tracking issues --")
    for spec in NEW_PROGRESS:
        if spec["title"] not in all_issues:
            issue = repo.create_issue(title=spec["title"], body=spec["body"])
            print(f"  Created #{issue.number}: {spec['title']}")
            time.sleep(0.8)
        else:
            print(f"  Already exists: {spec['title']}")

    # 3. New room issues (closed)
    print("\n-- Creating new room issues --")
    created = 0
    for path_prefix, section, slug, file_path, path_name in NEW_ROOM_ISSUES:
        title = f"{path_prefix} — {section}] {slug}"
        if title in all_issues:
            continue
        body = room_body(path_prefix, section, slug, file_path, args.repo)
        issue = repo.create_issue(title=title, body=body)
        time.sleep(0.5)
        issue.edit(state="closed")
        created += 1
        if created % 10 == 0:
            print(f"  ... {created} issues created")
        time.sleep(0.5)

    print(f"\nDone. {created} new room issues created and closed.")
    print(f"Issues: https://github.com/{args.repo}/issues")


if __name__ == "__main__":
    main()
