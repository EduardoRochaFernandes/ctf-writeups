# Room: Phishing Analysis Fundamentals

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Phishing Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Free
**Room Link:** https://tryhackme.com/room/phishingemails1tryoe

---

## What is this room about?

Phishing remains the most common initial access vector. This room covers the fundamentals of email structure, email flow, types of phishing attacks, and how to start analysing a suspicious email.

---

## How Email Works

```
1. Sender writes email in their client
2. Client sends to outbound SMTP server
3. SMTP server does DNS MX lookup for recipient's domain
4. Email travels across the internet via SMTP relays
5. Arrives at recipient's SMTP server
6. Delivered to user's mailbox via POP3/IMAP
7. User's email client fetches it
```

**Three protocols:**
| Protocol | Port | Role |
|----------|------|------|
| SMTP | 25 | Sending email between servers |
| POP3 | 110 | Download to one device, remove from server |
| IMAP | 143 | Sync across multiple devices (modern standard) |

---

## Anatomy of an Email

### Headers (Critical for Analysis)
| Header | What it tells you |
|--------|-----------------|
| `From` | Sender address — **can be spoofed** |
| `Reply-To` | Where replies go — if different from From, highly suspicious |
| `X-Originating-IP` | The real IP that sent the email |
| `Received` | The chain of SMTP hops the email passed through |
| `Authentication-Results` | SPF/DKIM/DMARC results |

The **Reply-To trick** is used in BEC (Business Email Compromise): the From looks legitimate, but Reply-To points to the attacker's mailbox. The victim replies thinking they're talking to their CFO.

### Body
Can be plain text or HTML. HTML allows pixel-perfect brand impersonation with images and styled buttons. Attachments appear in the source as Base64-encoded data.

---

## Types of Phishing

| Type | Target | Sophistication |
|------|--------|---------------|
| **Spam / MalSpam** | Everyone | Low — mass campaign |
| **Phishing** | General users | Medium — impersonates trusted brands |
| **Spear Phishing** | Specific person/org | High — uses personal details |
| **Whaling** | C-level executives | Very high — researched, personalised |
| **Smishing** | Mobile via SMS | Medium |
| **Vishing** | Phone call | Variable — can include deepfakes |

---

## Red Flags in a Phishing Email

- Sender domain doesn't match the displayed company name
- Urgency language ("Act now!", "Your account is suspended")
- Generic greeting ("Dear Customer", "Dear User")
- Shortened or obfuscated URLs hiding the real destination
- Mismatched `Reply-To` and `From` addresses
- Attachments with unusual extensions or double extensions (`.pdf.exe`)

---

## Defanging — Sharing IoCs Safely

When sharing suspicious URLs or email addresses in reports or chat, always defang them first:

```
Original:   http://malicious.example.com/payload
Defanged:   hxxp[://]malicious[.]example[.]com/payload

Original:   attacker@evil.com
Defanged:   attacker[@]evil[.]com
```

**CyberChef** does this automatically with the "Defang URL" recipe.

---

## Real Phishing Techniques (Case Studies)

- **URL shorteners** (bit.ly, tinyurl) — hide malicious destination. Always expand before clicking.
- **Tracking pixels** — 1x1 invisible images that confirm you opened the email and reveal your IP. Email clients block images by default for this reason.
- **Credential harvesting pages** — even if you type wrong credentials, the attacker captures what you typed.
- **Malicious PDF attachments** — PDFs can contain embedded links and JavaScript.
- **Excel macros** — `.xlsm` files with auto-running VBA code. Macros should be disabled org-wide.
- **BCC targeting** — victim is added in BCC instead of To, making the email harder to detect and analyse.

---

## Key Takeaways

> The Reply-To field is one of the most underappreciated phishing indicators. Always verify it matches the From field.

Phishing analysis is part art, part checklist. The checklist catches the obvious stuff — the art is recognising when something feels slightly wrong even if it passes all the automated checks.

---

## References

- [MITRE ATT&CK — T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [PhishTool](https://www.phishtool.com/)
