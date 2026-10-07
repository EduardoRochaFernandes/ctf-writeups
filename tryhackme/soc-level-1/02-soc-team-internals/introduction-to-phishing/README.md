# Introduction to Phishing

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 02: SOC Team Internals
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Phishing is consistently the most common initial access vector in real-world breaches. Before beginning the dedicated phishing analysis section, this room establishes the technical foundations: how email works at the protocol level, the anatomy of an email message, the types of phishing attacks, and the authentication protocols that exist to prevent email spoofing.

---

## How Email Works

Understanding the email transport chain is essential for header analysis in phishing investigations.

```
Sender composes email in client application
    Client connects to outbound SMTP server
    SMTP server performs DNS MX lookup for recipient domain
    Email traverses the internet via SMTP relay chain
    Arrives at recipient's inbound SMTP server
    Delivered to user mailbox via POP3 or IMAP
    User client fetches and displays the message
```

**The three email protocols:**

| Protocol | Port | Function |
|----------|------|---------|
| SMTP | 25 (server-to-server), 587 (client submission) | Sending and relaying email |
| POP3 | 110 | Downloads email to one device, removes from server |
| IMAP | 143 | Synchronises email across multiple devices (modern standard) |

---

## Email Message Anatomy

An email consists of two parts: headers and body.

**Headers** — structured metadata fields. Key fields for security analysis:

| Header | Significance |
|--------|-------------|
| From | Sender address. Can be freely spoofed in SMTP. Do not trust without authentication results. |
| Reply-To | Where replies are directed. If different from From, highly suspicious — attacker may be redirecting correspondence. |
| X-Originating-IP | The IP address of the system that first injected the email into the SMTP infrastructure. Often reveals the actual sender location. |
| Received | A chain of SMTP relay headers, added by each server that handled the message. Read bottom-to-top for the true delivery path. |
| Authentication-Results | SPF, DKIM, and DMARC evaluation results from the receiving server. |

**Body** — can be plain text or HTML. HTML bodies allow for pixel-perfect brand impersonation. Attachments are encoded in Base64 within the message and identified by MIME type headers.

---

## Types of Phishing Attack

| Type | Targeting | Sophistication |
|------|-----------|---------------|
| Spam / MalSpam | Mass, untargeted | Low — high volume, low conversion |
| Phishing | General users | Medium — impersonates trusted brands |
| Spear Phishing | Specific individual or organisation | High — uses personal reconnaissance data |
| Whaling | C-level executives | Very high — extensive preparation, high reward |
| Smishing | Via SMS | Variable |
| Vishing | Via phone call | Variable — increasingly combined with AI voice synthesis |

---

## Email Authentication Protocols

SMTP was designed without authentication — any server can claim to send email from any domain. Three protocols address this:

**SPF (Sender Policy Framework)**
A DNS TXT record that lists which IP addresses are authorised to send email for a domain. Receiving servers check whether the sending IP appears in the record. Fails when email is forwarded, because the forwarding server's IP is not in the original record.

Example: `v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all`

**DKIM (DomainKeys Identified Mail)**
Adds a cryptographic signature to outgoing email. The private key signs the message; the public key is published in DNS. Receiving servers verify the signature. Survives forwarding because the signature is part of the message, not tied to the sending IP.

Example: `v=DKIM1; k=rsa; p=<public_key>`

**DMARC (Domain-based Message Authentication, Reporting and Conformance)**
Combines SPF and DKIM, aligns the visible From header with both, and defines what to do when checks fail:
- `p=none` — monitor only, no enforcement
- `p=quarantine` — failed messages to spam folder
- `p=reject` — failed messages are blocked entirely

Example: `v=DMARC1; p=reject; rua=mailto:dmarc@example.com`

**Defanging IoCs** — when sharing suspicious URLs or email addresses in reports, defang them to prevent accidental clicks:
```
http://evil.example.com  →  hxxp[://]evil[.]example[.]com
attacker@evil.com        →  attacker[@]evil[.]com
```

---

## Key Takeaways

The Reply-To field is the most underappreciated phishing indicator. In Business Email Compromise attacks, the From address is legitimate (or spoofed to appear so) but the Reply-To points to the attacker's inbox. The victim sends sensitive information directly to the attacker while believing they are communicating with a trusted colleague. Always verify Reply-To matches From.

---

## References

- [MITRE ATT&CK — T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
- [DMARC.org Reference](https://dmarc.org/)
