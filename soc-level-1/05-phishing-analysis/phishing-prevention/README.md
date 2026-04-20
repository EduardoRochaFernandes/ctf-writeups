# Phishing Prevention

**Platform:** TryHackMe
**Path:** SOC Level 1 — Section 05: Phishing Analysis
**Difficulty:** Easy
**Type:** Walkthrough
**Status:** Complete

---

## Overview

Detection and analysis skills are one side of phishing defence. This room covers the prevention side: the email authentication protocols that prevent domain spoofing, the gateway technologies that filter malicious email, and the organisational controls that reduce user susceptibility.

---

## The Core Problem — SMTP Has No Authentication

SMTP was designed in 1982 with no provision for verifying that a server sending email for a domain is actually authorised to do so. Any server can send email claiming to be from any domain. Three protocols were developed to address this:

---

## SPF — Sender Policy Framework

SPF defines which IP addresses are authorised to send email on behalf of a domain. Published as a DNS TXT record:

```
v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all
```

- `ip4:192.0.2.0/24` — this IP range is authorised
- `include:_spf.google.com` — also include Google's authorised ranges
- `-all` — reject email from any other source (hard fail)

**Limitation:** SPF breaks on email forwarding. When a message is forwarded, the forwarding server's IP is not in the original domain's SPF record, causing a failure even for legitimate email.

---

## DKIM — DomainKeys Identified Mail

DKIM adds a cryptographic signature to every outgoing message. The private key signs selected headers and the message body; the public key is published in DNS. The receiving server fetches the public key and verifies the signature.

```
v=DKIM1; k=rsa; p=<base64_encoded_public_key>
```

**Advantage over SPF:** DKIM signatures are part of the message and survive forwarding, because the signature is validated against the message content, not the sending IP.

---

## DMARC — Domain-based Message Authentication, Reporting, and Conformance

DMARC builds on SPF and DKIM by:
- Aligning the visible From header with SPF and DKIM domains
- Defining what to do when checks fail (policy)
- Providing aggregate reporting on how the domain's email is being authenticated

```
v=DMARC1; p=reject; rua=mailto:dmarc-reports@example.com; ruf=mailto:forensics@example.com
```

Policies:
- `p=none` — monitoring only, no enforcement. Starting point for new implementations.
- `p=quarantine` — failed messages delivered to spam/junk folder
- `p=reject` — failed messages rejected at the SMTP level. Maximum protection.

The `rua` tag sends aggregate reports (showing who is sending email as your domain) to the specified address. This is valuable for identifying spoofing campaigns against your domain.

---

## S/MIME

Secure/Multipurpose Internet Mail Extensions provides end-to-end encryption and digital signatures for email content. Both sender and recipient require certificates. Protects against interception in transit but requires PKI infrastructure and certificate management.

---

## Secure Email Gateways

A Secure Email Gateway (SEG) sits in front of the mail infrastructure and inspects every inbound and outbound message:

- **Reputation filtering** — blocks email from known-malicious IPs and domains
- **Attachment sandboxing** — executes attachments in an isolated environment before delivery
- **Link rewriting** — replaces URLs with proxied versions that are checked at click-time
- **Impersonation detection** — identifies display name spoofing even when SPF/DKIM pass
- **Machine learning classification** — identifies novel phishing patterns

Popular SEGs: Proofpoint, Mimecast, Microsoft Defender for Office 365, Cisco Email Security.

---

## Checking Authentication Results in Practice

When analysing a suspicious email, the `Authentication-Results` header shows the outcome of all three checks:

```
Authentication-Results: mx.google.com;
   spf=pass (google.com: domain of legit@example.com designates 203.0.113.1 as permitted sender)
   dkim=pass header.i=@example.com header.s=selector1
   dmarc=pass (p=REJECT) header.from=example.com
```

A phishing email will typically show `spf=fail` or `dmarc=fail`, particularly if attempting to spoof a well-protected domain.

---

## Key Takeaways

SPF alone is insufficient. DKIM alone prevents forgery but not display name spoofing. DMARC ties them together with enforcement and reporting. All three, deployed with `p=reject`, provide comprehensive protection against domain spoofing. Organisations that have not deployed DMARC with enforcement are exposing their employees and customers to impersonation attacks with no technical protection.

---

## References

- [DMARC.org](https://dmarc.org/)
- [MXToolbox SPF/DKIM/DMARC Checker](https://mxtoolbox.com/SuperTool.aspx)
- [MITRE ATT&CK — T1566 Phishing](https://attack.mitre.org/techniques/T1566/)
