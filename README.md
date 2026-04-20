# CTF Writeups and Learning Journal

Personal documentation of cybersecurity learning, primarily through TryHackMe and Blue Team Labs Online. This repository tracks progression through structured learning paths with detailed notes, practical exercises, and key takeaways from each completed room.

The content here is oriented towards three complementary roles: SOC analyst operations, blue team defence engineering, and security engineering — reflecting the breadth of skills required to work effectively in a modern security operations environment.

---

## Platforms

**TryHackMe** — Primary learning platform. Structured paths with guided rooms, labs, and challenges covering both theoretical foundations and practical application. This repository tracks the SOC Level 1, SOC Level 2, and SOC Level 3 paths.

**Blue Team Labs Online** — Scenario-based investigations using real or near-real log data and artefacts. Planned for integration alongside TryHackMe coverage to reinforce analytical skills in unguided conditions.

---

## Repository Structure

```
ctf-writeups/
├── soc-level-1/          TryHackMe SOC Level 1 path — 14 sections
├── soc-level-2/          TryHackMe SOC Level 2 path — in progress
├── soc-level-3/          TryHackMe SOC Level 3 path — planned
└── supplementary/        Rooms completed outside the main paths
                          to reinforce foundational knowledge
```

Each room directory contains a single `README.md` with structured notes: an overview of the room, key concepts learned, practical commands or techniques, and takeaways relevant to real-world SOC work.

---

## SOC Level 1 — Current Progress

The SOC Level 1 path is divided into 14 sections, progressing from blue team fundamentals through capstone challenge investigations. See individual section directories for room-level writeups.

Sections: Blue Team Introduction, SOC Team Internals, Core SOC Solutions, Cyber Defence Frameworks, Phishing Analysis, Network Traffic Analysis, Network Security Monitoring, Web Security Monitoring, Windows Security Monitoring, Linux Security Monitoring, Malware Concepts for SOC, Threat Analysis Tools, SIEM Triage for SOC, Capstone Challenges.

---

## Supplementary Study

The `supplementary/` directory contains rooms completed outside the SOC Level 1 path. These were done to build foundational knowledge in areas such as Windows internals, log analysis mechanics, and web application security — topics that underpin the SOC1 curriculum but are covered in more depth in standalone rooms.

---

## Related Projects

- [soc-home-lab](https://github.com/EduardoRochaFernandes/soc-home-lab) — A full SOC home lab built from scratch: Wazuh, Elasticsearch, Kibana, Suricata, TheHive, and MISP running on local virtual machines. Detection rules, Sigma coverage, runbooks, and attack simulations.

---

## Notes on Format

Writeups are written as technical study notes, not answer guides. Flags and direct challenge solutions are not included. The goal is to document understanding, not to shortcut the learning process for others.
