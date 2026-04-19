# Room: Phishing Prevention

**Platform:** TryHackMe
**Path:** SOC Level 1
**Category:** Phishing Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Cost:** Premium
**Room Link:** https://tryhackme.com/room/phishingemails4gkxh

---

## What is this room about?

Identifying phishing is half the job. This room covers the technical defences that prevent phishing emails from reaching users in the first place — the email authentication protocols that form the backbone of modern email security.

---

## The Problem: Email Spoofing

SMTP was designed in 1982 with no authentication whatsoever. Any server can claim to be sending email from any domain. Attackers exploit this to impersonate legitimate organisations — your bank, Microsoft, your CEO.

The three protocols below were created specifically to fix this.

---

## SPF — Sender Policy Framework

**What it does:** Defines which IP addresses are authorised to send email on behalf of a domain.

**How it works:**
1. Domain owner publishes a DNS TXT record listing authorised senders:
   `v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all`
2. Receiving mail server checks the DNS record of the sender's domain
3. If the sending IP is not in the list → SPF fails

**Limitation:** SPF breaks when email is forwarded — the forwarding server's IP isn't in the original list.

---

## DKIM — DomainKeys Identified Mail

**What it does:** Adds a cryptographic signature to outgoing email that the receiver can verify.

**How it works:**
1. Sending server adds a `DKIM-Signature` header with a digital signature
2. The public key is published in DNS
3. Receiving server fetches the public key and verifies the signature

**Advantage over SPF:** DKIM survives forwarding because the signature is in the email itself, not tied to the sending IP.

**Example DNS record:** `v=DKIM1; k=rsa; p=<public_key>`

---

## DMARC — Domain-based Message Authentication Reporting and Conformance

**What it does:** Combines SPF and DKIM, aligns the `From` header with both, and defines what to do when either fails.

**Policy options:**
| Policy | What happens when SPF/DKIM fail |
|--------|--------------------------------|
| `none` | Do nothing — monitoring only |
| `quarantine` | Move to spam/quarantine |
| `reject` | Block the email entirely |

**Example DNS record:**
`v=DMARC1; p=reject; rua=mailto:dmarc-reports@example.com`

The `rua` parameter sends aggregate reports — you can see who's trying to spoof your domain.

---

## Additional Defences

### S/MIME (Secure/Multipurpose Internet Mail Extensions)
Encrypts the email body and allows digital signatures. Requires both parties to have certificates — complex to deploy at scale but used in high-security environments.

### Secure Email Gateways (SEGs)
Sit in front of your email infrastructure and scan every inbound and outbound email. They catch spoofing and impersonation that the protocol-level checks miss, rewrite links, sandbox attachments, and apply threat intelligence.

### Link Rewriting
SEGs replace URLs in emails with safe versions. When the user clicks, the link first goes to the gateway which checks the destination in real time — if it's now malicious (even if it wasn't when delivered), it blocks access.

---

## Checking Email Authentication in Practice

When analysing a suspicious email, look at the `Authentication-Results` header:

```
Authentication-Results: mx.google.com;
   spf=pass (google.com: domain of sender@legit.com designates 1.2.3.4 as permitted sender)
   dkim=pass header.i=@legit.com
   dmarc=pass (p=REJECT) header.from=legit.com
```

A phishing email will often show `spf=fail`, `dkim=fail`, or `dmarc=fail`.

---

## Key Takeaways

> SPF + DKIM + DMARC together form a strong baseline. Without all three, spoofing your domain is trivial.

SPF alone is insufficient. DKIM alone survives forwarding but doesn't prevent display name spoofing. DMARC ties them together and adds enforcement. All three should be deployed with `p=reject` for a production domain.

---

## References

- [DMARC.org](https://dmarc.org/)
- [MXToolbox SPF/DKIM/DMARC checker](https://mxtoolbox.com/)
- [MITRE ATT&CK — T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
