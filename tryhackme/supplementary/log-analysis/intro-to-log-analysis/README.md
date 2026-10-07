# Intro to Log Analysis

**Platform:** TryHackMe
**Path:** Supplementary — completed to reinforce foundational knowledge
**Status:** Complete

---

## Key Notes

Core pipeline: `cut -d' ' -f1 access.log | sort | uniq -c | sort -rn`. Attack patterns in logs: SQL keywords in URL parameters, path traversal sequences (`../`), XSS payloads (`<script>`), rapid 404 sequences (enumeration), identical-timestamp bursts (automation). Regex for extraction: `grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b'` for IPs.

---

## Placeholder

Detailed writeup can be expanded here.
