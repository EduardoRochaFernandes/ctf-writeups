# Room: Windows Fundamentals 3

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Windows
**Difficulty:** Info
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/windowsfundamentals3rdx

---

## What is this room about?

Covers built-in Windows security tools: Windows Update, Windows Defender/Security, BitLocker, and Volume Shadow Copy Service.

---

## Windows Defender Event IDs

| Event ID | Meaning |
|----------|---------|
| 1116 | Malware detected |
| 1117 | Action taken (quarantine/remove) |
| 5001 | Real-time protection disabled |
| 5007 | Settings modified |
| 5013 | Tamper protection triggered |

Events 5001 and 5013 are high-priority alerts — attackers disable Defender before running their tools.

---

## Windows Updates

Patch Tuesday: second Tuesday each month. Critical zero-day patches released immediately.

Check installed patches:
```powershell
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
```

---

## BitLocker

Full disk encryption using TPM chip. Stolen laptop = unreadable data.

SOC relevance: encrypted drives require recovery keys for forensic analysis. Store keys centrally in Active Directory or Azure AD.

---

## Volume Shadow Copy Service (VSS)

Windows snapshots the file system automatically. Ransomware's primary target before encrypting:

```cmd
vssadmin delete shadows /all /quiet
```

This command in any log = active ransomware incident. MITRE ATT&CK T1490 — Inhibit System Recovery.

---

## Key Takeaways

> Ransomware deletes shadow copies first, then encrypts. `vssadmin delete shadows` in your logs is one of the highest-fidelity ransomware indicators that exists.

---

## References

- [MITRE ATT&CK T1490 Inhibit System Recovery](https://attack.mitre.org/techniques/T1490/)
