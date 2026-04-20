# Room: Windows PowerShell

**Platform:** TryHackMe
**Path:** Supplementary
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Status:** Complete
**Room Link:** https://tryhackme.com/room/windowspowershell

---

## Overview

PowerShell is an object-oriented shell built on the .NET framework. Unlike CMD, which treats
everything as text, PowerShell passes objects between commands â€” enabling far more powerful and
flexible data manipulation. Created by Jeffrey Snover in 2006, it has been open-source and
cross-platform (Windows, macOS, Linux) since 2016 as PowerShell Core.

---

## Cmdlet Syntax: Verb-Noun

All commands follow the Verb-Noun pattern:

| Cmdlet | What it does |
|--------|-------------|
| Get-Content | Read file contents |
| Set-Location | Change current directory |
| Get-Process | List running processes |
| Get-Service | List services and their state |

Common aliases: dir = Get-ChildItem, cd = Set-Location, cat = Get-Content, echo = Write-Output

---

## Discovery and Help

    Get-Command                          # all available commands
    Get-Command -CommandType "Function"  # filter by type
    Get-Command -Verb Remove             # filter by verb
    Get-Help Get-Date                    # help for a cmdlet
    Get-Help New-LocalUser -examples     # usage examples
    Get-Alias                            # list all aliases

---

## File System Navigation

    Get-ChildItem                                             # list current directory
    Get-ChildItem -Path C:\Users                             # list specific path
    Set-Location -Path ".\Documents"                         # change directory
    New-Item -Path ".\notes.txt" -ItemType "File"            # create file
    New-Item -Path ".\backup" -ItemType "Directory"          # create folder
    Remove-Item -Path ".\notes.txt"                          # delete
    Copy-Item -Path .\original.txt -Destination .\copy.txt  # copy
    Move-Item -Path .\copy.txt -Destination ..\             # move
    Get-Content -Path ".\file.txt"                           # read file
    Get-Item -Path ".\file.txt" -Stream *                    # view Alternate Data Streams

---

## Filtering and Piping

The pipe operator passes objects (not text) between cmdlets.

    Get-ChildItem | Sort-Object Length
    Get-ChildItem | Sort-Object Length -Descending
    Get-ChildItem | Where-Object -Property "Extension" -eq ".txt"
    Get-ChildItem | Where-Object -Property Length -gt 100
    Get-ChildItem | Where-Object -Property "Name" -like "ship*"
    Get-ChildItem | Select-Object Name, Length
    Get-ChildItem | Sort-Object Length -Descending | Select-Object -First 1
    Select-String -Path ".\file.txt" -Pattern "password"

Comparison operators: -eq, -ne, -gt, -ge, -lt, -le, -like (wildcard with *)

---

## System and Network Information

    Get-ComputerInfo        # full system information
    Get-LocalUser           # local user accounts
    Get-NetIPConfiguration  # IP, DNS, gateway
    Get-NetIPAddress        # all IPs across all interfaces

---

## Processes, Services, and Live Network State

    Get-Process                    # processes with CPU and memory usage
    Get-Service                    # service states
    Get-NetTCPConnection           # active TCP connections and listening ports
    Get-FileHash -Path .\file.txt  # file hash for integrity verification

Get-NetTCPConnection includes OwningProcess (PID of the responsible process) â€” useful for
detecting backdoors listening on unexpected ports.

---

## Remote Execution

    Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service }
    Invoke-Command -FilePath c:\scripts\scan.ps1 -ComputerName Server01
    Invoke-Command -ComputerName Server01 -Credential Domain01\User01 -ScriptBlock { Get-Culture }

---

## Key Takeaways

PowerShell operates on objects rather than text, making it significantly more powerful than CMD
for system investigation. For a SOC analyst, the four most relevant cmdlets are Get-Process,
Get-Service, Get-NetTCPConnection, and Get-FileHash â€” covering anomalous process detection,
tampered services, suspicious network connections, and file integrity verification respectively.
Invoke-Command makes PowerShell indispensable in enterprise environments where investigation
spans multiple machines simultaneously.

---

## References

- TryHackMe: https://tryhackme.com/room/windowspowershell
- Microsoft Docs: https://learn.microsoft.com/en-us/powershell/
