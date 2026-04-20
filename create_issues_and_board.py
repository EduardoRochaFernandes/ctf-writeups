#!/usr/bin/env python3
"""
create_issues_and_board.py

Creates and closes all room issues, creates 3 open progress-tracking issues,
and builds a GitHub Projects (classic) board with columns:
  Backlog | To Do | In Progress | Done

Usage:
    pip install PyGithub python-dotenv
    python create_issues_and_board.py --repo EduardoRochaFernandes/ctf-writeups
"""

import argparse
import os
import sys
import time

try:
    from github import Github, GithubException
    from dotenv import load_dotenv
except ImportError:
    print("Run: pip install PyGithub python-dotenv")
    sys.exit(1)

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN", "")

# ──────────────────────────────────────────────────────────────────────
# ISSUE DEFINITIONS
# ──────────────────────────────────────────────────────────────────────

SETUP_ISSUES = [
    {
        "title": "setup: initialize repository structure — ctf-writeups",
        "body": (
            "## Summary\n\n"
            "Initialize the ctf-writeups repository with the full directory structure "
            "for the TryHackMe SOC Level 1 path (14 sections, 67 rooms), SOC Level 2, "
            "SOC Level 3, and the supplementary study folder.\n\n"
            "## Work Completed\n\n"
            "- Created all section directories under `soc-level-1/`\n"
            "- Created placeholder directories for `soc-level-2/` and `soc-level-3/`\n"
            "- Created `supplementary/` directory for rooms outside the official SOC1 path\n\n"
            "Closed upon completion."
        ),
        "close": True,
    },
    {
        "title": "docs: add README.md and .gitignore",
        "body": (
            "## Summary\n\n"
            "Add the repository root README and .gitignore file.\n\n"
            "## Work Completed\n\n"
            "- `README.md` — project overview, platform description, folder structure "
            "reference, and link to the related SOC home lab project\n"
            "- `.gitignore` — ignores `.env`, `__pycache__`, OS artefacts, and PCAP files\n\n"
            "Closed upon completion."
        ),
        "close": True,
    },
]

# SOC Level 1 rooms — 14 sections, 67 rooms
SOC1_ROOMS = [
    # Section 01
    ("01 — Blue Team Introduction", "blue-team-introduction", "soc-level-1/01-blue-team-introduction/blue-team-introduction/README.md", True),
    ("01 — Blue Team Introduction", "junior-security-analyst-intro", "soc-level-1/01-blue-team-introduction/junior-security-analyst-intro/README.md", True),
    ("01 — Blue Team Introduction", "soc-role-in-blue-team", "soc-level-1/01-blue-team-introduction/soc-role-in-blue-team/README.md", True),
    ("01 — Blue Team Introduction", "humans-as-attack-vectors", "soc-level-1/01-blue-team-introduction/humans-as-attack-vectors/README.md", True),
    ("01 — Blue Team Introduction", "systems-as-attack-vectors", "soc-level-1/01-blue-team-introduction/systems-as-attack-vectors/README.md", True),
    # Section 02
    ("02 — SOC Team Internals", "soc-l1-alert-triage", "soc-level-1/02-soc-team-internals/soc-l1-alert-triage/README.md", True),
    ("02 — SOC Team Internals", "soc-l1-alert-reporting", "soc-level-1/02-soc-team-internals/soc-l1-alert-reporting/README.md", True),
    ("02 — SOC Team Internals", "soc-workbooks-and-lookups", "soc-level-1/02-soc-team-internals/soc-workbooks-and-lookups/README.md", True),
    ("02 — SOC Team Internals", "soc-metrics-and-objectives", "soc-level-1/02-soc-team-internals/soc-metrics-and-objectives/README.md", True),
    ("02 — SOC Team Internals", "introduction-to-phishing", "soc-level-1/02-soc-team-internals/introduction-to-phishing/README.md", True),
    # Section 03
    ("03 — Core SOC Solutions", "introduction-to-edr", "soc-level-1/03-core-soc-solutions/introduction-to-edr/README.md", True),
    ("03 — Core SOC Solutions", "introduction-to-siem", "soc-level-1/03-core-soc-solutions/introduction-to-siem/README.md", True),
    ("03 — Core SOC Solutions", "splunk-the-basics", "soc-level-1/03-core-soc-solutions/splunk-the-basics/README.md", False),
    ("03 — Core SOC Solutions", "elastic-stack-the-basics", "soc-level-1/03-core-soc-solutions/elastic-stack-the-basics/README.md", False),
    ("03 — Core SOC Solutions", "introduction-to-soar", "soc-level-1/03-core-soc-solutions/introduction-to-soar/README.md", False),
    # Section 04
    ("04 — Cyber Defence Frameworks", "pyramid-of-pain", "soc-level-1/04-cyber-defence-frameworks/pyramid-of-pain/README.md", True),
    ("04 — Cyber Defence Frameworks", "cyber-kill-chain", "soc-level-1/04-cyber-defence-frameworks/cyber-kill-chain/README.md", True),
    ("04 — Cyber Defence Frameworks", "unified-kill-chain", "soc-level-1/04-cyber-defence-frameworks/unified-kill-chain/README.md", True),
    ("04 — Cyber Defence Frameworks", "mitre", "soc-level-1/04-cyber-defence-frameworks/mitre/README.md", True),
    ("04 — Cyber Defence Frameworks", "summit", "soc-level-1/04-cyber-defence-frameworks/summit/README.md", True),
    ("04 — Cyber Defence Frameworks", "eviction", "soc-level-1/04-cyber-defence-frameworks/eviction/README.md", True),
    # Section 05
    ("05 — Phishing Analysis", "phishing-analysis-fundamentals", "soc-level-1/05-phishing-analysis/phishing-analysis-fundamentals/README.md", True),
    ("05 — Phishing Analysis", "phishing-emails-in-action", "soc-level-1/05-phishing-analysis/phishing-emails-in-action/README.md", True),
    ("05 — Phishing Analysis", "phishing-analysis-tools", "soc-level-1/05-phishing-analysis/phishing-analysis-tools/README.md", True),
    ("05 — Phishing Analysis", "phishing-prevention", "soc-level-1/05-phishing-analysis/phishing-prevention/README.md", True),
    ("05 — Phishing Analysis", "the-greenholt-phish", "soc-level-1/05-phishing-analysis/the-greenholt-phish/README.md", True),
    ("05 — Phishing Analysis", "snapped-phish-ing-line", "soc-level-1/05-phishing-analysis/snapped-phish-ing-line/README.md", False),
    ("05 — Phishing Analysis", "phishing-unfolding", "soc-level-1/05-phishing-analysis/phishing-unfolding/README.md", False),
    # Section 06
    ("06 — Network Traffic Analysis", "network-traffic-basics", "soc-level-1/06-network-traffic-analysis/network-traffic-basics/README.md", True),
    ("06 — Network Traffic Analysis", "wireshark-the-basics", "soc-level-1/06-network-traffic-analysis/wireshark-the-basics/README.md", False),
    ("06 — Network Traffic Analysis", "wireshark-packet-operations", "soc-level-1/06-network-traffic-analysis/wireshark-packet-operations/README.md", True),
    ("06 — Network Traffic Analysis", "wireshark-traffic-analysis", "soc-level-1/06-network-traffic-analysis/wireshark-traffic-analysis/README.md", True),
    ("06 — Network Traffic Analysis", "networkminer", "soc-level-1/06-network-traffic-analysis/networkminer/README.md", False),
    # Section 07
    ("07 — Network Security Monitoring", "network-security-essentials", "soc-level-1/07-network-security-monitoring/network-security-essentials/README.md", False),
    ("07 — Network Security Monitoring", "network-discovery-detection", "soc-level-1/07-network-security-monitoring/network-discovery-detection/README.md", False),
    ("07 — Network Security Monitoring", "data-exfiltration-detection", "soc-level-1/07-network-security-monitoring/data-exfiltration-detection/README.md", False),
    ("07 — Network Security Monitoring", "man-in-the-middle-detection", "soc-level-1/07-network-security-monitoring/man-in-the-middle-detection/README.md", True),
    ("07 — Network Security Monitoring", "ids-fundamentals", "soc-level-1/07-network-security-monitoring/ids-fundamentals/README.md", False),
    ("07 — Network Security Monitoring", "snort", "soc-level-1/07-network-security-monitoring/snort/README.md", False),
    # Section 08
    ("08 — Web Security Monitoring", "web-security-essentials", "soc-level-1/08-web-security-monitoring/web-security-essentials/README.md", True),
    ("08 — Web Security Monitoring", "detecting-web-attacks", "soc-level-1/08-web-security-monitoring/detecting-web-attacks/README.md", True),
    ("08 — Web Security Monitoring", "detecting-web-shells", "soc-level-1/08-web-security-monitoring/detecting-web-shells/README.md", True),
    ("08 — Web Security Monitoring", "detecting-web-ddos", "soc-level-1/08-web-security-monitoring/detecting-web-ddos/README.md", True),
    # Section 09
    ("09 — Windows Security Monitoring", "windows-logging-for-soc", "soc-level-1/09-windows-security-monitoring/windows-logging-for-soc/README.md", False),
    ("09 — Windows Security Monitoring", "windows-threat-detection-1", "soc-level-1/09-windows-security-monitoring/windows-threat-detection-1/README.md", False),
    ("09 — Windows Security Monitoring", "windows-threat-detection-2", "soc-level-1/09-windows-security-monitoring/windows-threat-detection-2/README.md", False),
    ("09 — Windows Security Monitoring", "windows-threat-detection-3", "soc-level-1/09-windows-security-monitoring/windows-threat-detection-3/README.md", False),
    # Section 10
    ("10 — Linux Security Monitoring", "linux-logging-for-soc", "soc-level-1/10-linux-security-monitoring/linux-logging-for-soc/README.md", False),
    ("10 — Linux Security Monitoring", "linux-threat-detection-1", "soc-level-1/10-linux-security-monitoring/linux-threat-detection-1/README.md", False),
    ("10 — Linux Security Monitoring", "linux-threat-detection-2", "soc-level-1/10-linux-security-monitoring/linux-threat-detection-2/README.md", False),
    ("10 — Linux Security Monitoring", "linux-threat-detection-3", "soc-level-1/10-linux-security-monitoring/linux-threat-detection-3/README.md", False),
    # Section 11
    ("11 — Malware Concepts for SOC", "malware-classification", "soc-level-1/11-malware-concepts-for-soc/malware-classification/README.md", False),
    ("11 — Malware Concepts for SOC", "intro-to-malware-analysis", "soc-level-1/11-malware-concepts-for-soc/intro-to-malware-analysis/README.md", False),
    ("11 — Malware Concepts for SOC", "living-off-the-land-attacks", "soc-level-1/11-malware-concepts-for-soc/living-off-the-land-attacks/README.md", False),
    ("11 — Malware Concepts for SOC", "shadow-trace", "soc-level-1/11-malware-concepts-for-soc/shadow-trace/README.md", False),
    # Section 12
    ("12 — Threat Analysis Tools", "intro-to-cyber-threat-intel", "soc-level-1/12-threat-analysis-tools/intro-to-cyber-threat-intel/README.md", False),
    ("12 — Threat Analysis Tools", "file-and-hash-threat-intel", "soc-level-1/12-threat-analysis-tools/file-and-hash-threat-intel/README.md", False),
    ("12 — Threat Analysis Tools", "ip-and-domain-threat-intel", "soc-level-1/12-threat-analysis-tools/ip-and-domain-threat-intel/README.md", False),
    # Section 13
    ("13 — SIEM Triage for SOC", "log-analysis-with-siem", "soc-level-1/13-siem-triage-for-soc/log-analysis-with-siem/README.md", False),
    ("13 — SIEM Triage for SOC", "alert-triage-with-splunk", "soc-level-1/13-siem-triage-for-soc/alert-triage-with-splunk/README.md", False),
    ("13 — SIEM Triage for SOC", "alert-triage-with-elastic", "soc-level-1/13-siem-triage-for-soc/alert-triage-with-elastic/README.md", False),
    ("13 — SIEM Triage for SOC", "itsybitsy", "soc-level-1/13-siem-triage-for-soc/itsybitsy/README.md", False),
    ("13 — SIEM Triage for SOC", "benign", "soc-level-1/13-siem-triage-for-soc/benign/README.md", False),
    # Section 14
    ("14 — Capstone Challenges", "tempest", "soc-level-1/14-capstone-challenges/tempest/README.md", False),
    ("14 — Capstone Challenges", "boogeyman-1", "soc-level-1/14-capstone-challenges/boogeyman-1/README.md", False),
    ("14 — Capstone Challenges", "boogeyman-2", "soc-level-1/14-capstone-challenges/boogeyman-2/README.md", False),
    ("14 — Capstone Challenges", "boogeyman-3", "soc-level-1/14-capstone-challenges/boogeyman-3/README.md", False),
]

SUPPLEMENTARY_ROOMS = [
    "defensive-security-intro", "offensive-security-intro", "http-in-detail",
    "web-application-basics", "web-application-security", "core-windows-processes",
    "windows-fundamentals-1", "windows-fundamentals-2", "windows-fundamentals-3",
    "windows-basics", "windows-cli-basics", "windows-internals",
    "evading-logging-and-monitoring", "intro-to-logs", "intro-to-log-analysis",
    "log-operations", "log-universe", "logless-hunt", "advanced-log-detection",
    "careers-in-cyber", "carnage",
]

PROGRESS_ISSUES = [
    {
        "title": "track: SOC Level 1 — learning progress",
        "body": (
            "## SOC Level 1 — TryHackMe\n\n"
            "This issue tracks overall progress through the TryHackMe SOC Level 1 path.\n\n"
            "**Path:** https://tryhackme.com/path/outline/soclevel1\n\n"
            "## Sections\n\n"
            "- Section 01: Blue Team Introduction\n"
            "- Section 02: SOC Team Internals\n"
            "- Section 03: Core SOC Solutions\n"
            "- Section 04: Cyber Defence Frameworks\n"
            "- Section 05: Phishing Analysis\n"
            "- Section 06: Network Traffic Analysis\n"
            "- Section 07: Network Security Monitoring\n"
            "- Section 08: Web Security Monitoring\n"
            "- Section 09: Windows Security Monitoring\n"
            "- Section 10: Linux Security Monitoring\n"
            "- Section 11: Malware Concepts for SOC\n"
            "- Section 12: Threat Analysis Tools\n"
            "- Section 13: SIEM Triage for SOC\n"
            "- Section 14: Capstone Challenges\n\n"
            "This issue remains open until the full path is complete."
        ),
        "close": False,
    },
    {
        "title": "track: SOC Level 2 — learning progress",
        "body": (
            "## SOC Level 2 — TryHackMe\n\n"
            "This issue tracks progress through the TryHackMe SOC Level 2 path.\n\n"
            "**Status:** Planned — starting after SOC Level 1 completion.\n\n"
            "This issue remains open until the full path is complete."
        ),
        "close": False,
    },
    {
        "title": "track: SOC Level 3 — learning progress",
        "body": (
            "## SOC Level 3 — TryHackMe\n\n"
            "This issue tracks progress through the TryHackMe SOC Level 3 path.\n\n"
            "**Status:** Planned — starting after SOC Level 2 completion.\n\n"
            "This issue remains open until the full path is complete."
        ),
        "close": False,
    },
]


def room_issue_body(section_label, slug, writeup_path, is_done, repo_name):
    status = "Complete" if is_done else "Pending"
    writeup_url = f"https://github.com/{repo_name}/blob/main/{writeup_path}"
    folder = "soc-level-1" if "soc-level-1" in writeup_path else "supplementary"
    return (
        f"## Room Details\n\n"
        f"| Field | Value |\n"
        f"|-------|-------|\n"
        f"| **Platform** | TryHackMe |\n"
        f"| **Folder** | `{folder}` |\n"
        f"| **Section** | {section_label} |\n"
        f"| **Room slug** | `{slug}` |\n"
        f"| **Status** | {status} |\n\n"
        f"## Room Link\n\n"
        f"https://tryhackme.com/room/{slug.replace('-', '')}\n\n"
        f"## Writeup\n\n"
        f"[{writeup_path}]({writeup_url})\n\n"
        f"---\n\n"
        f"Closed upon writeup creation."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="owner/repo")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not TOKEN:
        print("Set GITHUB_TOKEN in .env")
        sys.exit(1)

    g = Github(TOKEN)
    try:
        repo = g.get_repo(args.repo)
        print(f"Connected: {repo.full_name}")
    except GithubException as e:
        print(f"Cannot access repo: {e}")
        sys.exit(1)

    if args.dry_run:
        soc1_count = len(SOC1_ROOMS)
        sup_count = len(SUPPLEMENTARY_ROOMS)
        total = 2 + soc1_count + sup_count + 3
        print(f"\nDRY RUN — would create {total} issues total:")
        print(f"  2 setup issues (close)")
        print(f"  {soc1_count} SOC1 room issues (close)")
        print(f"  {sup_count} supplementary room issues (close)")
        print(f"  3 progress tracking issues (open)")
        print(f"  1 GitHub Projects board with 4 columns")
        return

    created_issues = {"setup": [], "soc1_done": [], "soc1_pending": [],
                      "sup": [], "progress": []}

    # ── Setup issues ─────────────────────────────────────────────
    print("\n-- Setup issues --")
    for spec in SETUP_ISSUES:
        issue = repo.create_issue(title=spec["title"], body=spec["body"])
        print(f"  Created #{issue.number}: {spec['title']}")
        time.sleep(0.5)
        if spec["close"]:
            issue.edit(state="closed")
        created_issues["setup"].append(issue)
        time.sleep(0.8)

    # ── SOC1 room issues ──────────────────────────────────────────
    print("\n-- SOC1 room issues --")
    for section_label, slug, path, is_done in SOC1_ROOMS:
        title = f"[SOC Level 1 — {section_label}] {slug}"
        body = room_issue_body(section_label, slug, path, is_done, args.repo)
        issue = repo.create_issue(title=title, body=body)
        print(f"  Created #{issue.number}: {title[:60]}")
        time.sleep(0.5)
        issue.edit(state="closed")
        bucket = "soc1_done" if is_done else "soc1_pending"
        created_issues[bucket].append(issue)
        time.sleep(0.8)

    # ── Supplementary room issues ─────────────────────────────────
    print("\n-- Supplementary room issues --")
    for slug in SUPPLEMENTARY_ROOMS:
        path = f"supplementary/{slug}/README.md"
        title = f"[Supplementary] {slug}"
        body = room_issue_body("Supplementary", slug, path, True, args.repo)
        issue = repo.create_issue(title=title, body=body)
        print(f"  Created #{issue.number}: {title}")
        time.sleep(0.5)
        issue.edit(state="closed")
        created_issues["sup"].append(issue)
        time.sleep(0.8)

    # ── Progress tracking issues (remain open) ────────────────────
    print("\n-- Progress tracking issues (open) --")
    for spec in PROGRESS_ISSUES:
        issue = repo.create_issue(title=spec["title"], body=spec["body"])
        print(f"  Created #{issue.number}: {spec['title']}")
        created_issues["progress"].append(issue)
        time.sleep(0.8)

    # ── GitHub Projects board ─────────────────────────────────────
    print("\n-- Creating project board --")
    try:
        project = repo.create_project(
            name="ctf-writeups Learning Tracker",
            body="Tracks progress through TryHackMe SOC Level 1, Level 2, and Level 3 paths."
        )
        print(f"  Project created: {project.name}")
        time.sleep(1)

        col_backlog   = project.create_column("Backlog")
        col_todo      = project.create_column("To Do")
        col_inprogress= project.create_column("In Progress")
        col_review    = project.create_column("Review")
        col_done      = project.create_column("Done")
        time.sleep(1)

        # Done: setup issues + SOC1 completed rooms + supplementary rooms
        for issue in (created_issues["setup"] +
                      created_issues["soc1_done"] +
                      created_issues["sup"]):
            col_done.create_card(content_id=issue.id, content_type="Issue")
            time.sleep(0.3)

        # To Do: SOC1 pending rooms
        for issue in created_issues["soc1_pending"]:
            col_todo.create_card(content_id=issue.id, content_type="Issue")
            time.sleep(0.3)

        # In Progress: SOC Level 1 progress (active)
        col_inprogress.create_card(
            content_id=created_issues["progress"][0].id, content_type="Issue"
        )
        time.sleep(0.3)

        # Backlog: SOC Level 2 and SOC Level 3
        for issue in created_issues["progress"][1:]:
            col_backlog.create_card(content_id=issue.id, content_type="Issue")
            time.sleep(0.3)

        print("  Board populated")
    except GithubException as e:
        print(f"  Board creation failed: {e}")
        print("  (Issues were still created successfully)")

    # ── Summary ───────────────────────────────────────────────────
    total = (len(created_issues["setup"]) + len(created_issues["soc1_done"]) +
             len(created_issues["soc1_pending"]) + len(created_issues["sup"]) +
             len(created_issues["progress"]))
    print(f"\nComplete. Created {total} issues.")
    print(f"Issues: https://github.com/{args.repo}/issues")
    print(f"Board:  https://github.com/{args.repo}/projects")


if __name__ == "__main__":
    main()
