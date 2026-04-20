#!/usr/bin/env python3
"""
fix_issues.py

Reopens all issues for rooms that are placeholders (not yet completed).
Leaves closed only the issues for rooms with real writeups.

Completed rooms (49 total):
  SOC1: all of sections 01, 02, 03(edr+siem), 04, 05(minus snapped+unfolding),
        06(nta-basics, wireshark-packet-ops, wireshark-traffic-analysis),
        07(man-in-the-middle), 08(all 4)
  Supplementary: all 16 remaining

Usage:
    python fix_issues.py --repo EduardoRochaFernandes/ctf-writeups
"""

import argparse, os, sys, time
from github import Github, Auth

TOKEN = os.getenv("GITHUB_TOKEN", "")

# Issues whose title contains any of these strings should stay CLOSED
COMPLETED = {
    # SOC1 Section 01
    "blue-team-introduction",
    "junior-security-analyst-intro",
    "soc-role-in-blue-team",
    "humans-as-attack-vectors",
    "systems-as-attack-vectors",
    # SOC1 Section 02
    "soc-l1-alert-triage",
    "soc-l1-alert-reporting",
    "soc-workbooks-and-lookups",
    "soc-metrics-and-objectives",
    "introduction-to-phishing",
    # SOC1 Section 03
    "introduction-to-edr",
    "introduction-to-siem",
    # SOC1 Section 04
    "pyramid-of-pain",
    "cyber-kill-chain",
    "unified-kill-chain",
    "mitre",
    "summit",
    "eviction",
    # SOC1 Section 05 (minus snapped and unfolding)
    "phishing-analysis-fundamentals",
    "phishing-emails-in-action",
    "phishing-analysis-tools",
    "phishing-prevention",
    "the-greenholt-phish",
    # SOC1 Section 06 (partial)
    "network-traffic-basics",
    "wireshark-packet-operations",
    "wireshark-traffic-analysis",
    # SOC1 Section 07 (partial)
    "man-in-the-middle-detection",
    # SOC1 Section 08
    "web-security-essentials",
    "detecting-web-attacks",
    "detecting-web-shells",
    "detecting-web-ddos",
    # Supplementary (all)
    "defensive-security-intro",
    "offensive-security-intro",
    "http-in-detail",
    "web-application-basics",
    "web-application-security",
    "core-windows-processes",
    "windows-fundamentals-1",
    "windows-fundamentals-2",
    "windows-fundamentals-3",
    "windows-basics",
    "windows-cli-basics",
    "evading-logging-and-monitoring",
    "log-universe",
    "advanced-log-detection",
    "careers-in-cyber",
    "carnage",
    # Also keep setup issues closed
    "initialize repository",
    "add README.md and .gitignore",
}

def is_completed(title):
    t = title.lower()
    return any(slug.lower() in t for slug in COMPLETED)

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

    # Get all closed issues (these are the ones we need to evaluate)
    closed = list(repo.get_issues(state="closed"))
    print(f"Total closed issues: {len(closed)}")

    to_reopen = []
    stay_closed = []

    for issue in closed:
        if is_completed(issue.title):
            stay_closed.append(issue)
        else:
            to_reopen.append(issue)

    print(f"Stay closed (completed): {len(stay_closed)}")
    print(f"To reopen (placeholder): {len(to_reopen)}")

    if args.dry_run:
        print("\nDRY RUN — issues that would be reopened:")
        for i in to_reopen[:10]:
            print(f"  #{i.number}: {i.title[:80]}")
        if len(to_reopen) > 10:
            print(f"  ... and {len(to_reopen) - 10} more")
        return

    print(f"\nReopening {len(to_reopen)} issues...")
    reopened = 0
    for issue in to_reopen:
        issue.edit(state="open")
        reopened += 1
        if reopened % 10 == 0:
            print(f"  {reopened}/{len(to_reopen)} reopened...")
        time.sleep(0.4)

    print(f"\nDone. {reopened} issues reopened.")
    print(f"Open (pending rooms): {reopened}")
    print(f"Closed (completed):   {len(stay_closed)}")
    print(f"\nhttps://github.com/{args.repo}/issues")

if __name__ == "__main__":
    main()
