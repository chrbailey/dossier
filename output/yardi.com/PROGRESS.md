# Dossier: yardi.com
Started: 2026-07-08T23:26:47Z
Iteration: 0

## Phases
- [x] P1 Discovery — complete 2026-07-08 (01-discovery.md; raw/whois.json, raw/dns.json, raw/website-content.json)
- [ ] P2 Market
- [ ] P3 Technical
- [ ] P4 Claims — blocked (needs P1, P3)
- [ ] P4.5 Red Team — blocked (needs P4)
- [ ] P5 Academic
- [ ] P6 Valuation — blocked (needs P1-P4.5)
- [ ] P7 Report — blocked (needs P6)

## Blockers
- P1 environment gaps (non-fatal, work around applied): direct fetch of yardi.com blocked (Cloudflare + egress proxy 403) -> first-party content captured via WebSearch snippets; WHOIS port 43/RDAP blocked -> registration data from whois.com snippet (single independent source); TXT DNS lookup timed out; llms.txt / .well-known check UNCONFIRMED (no indexed llms.txt found, but could not probe directly) — downstream phases with direct access must re-check.

## Notes
- P1 key facts: Yardi Systems Inc., founded 1984 by Anant Yardi, HQ Santa Barbara CA; private/founder-owned, reportedly no outside capital (Crunchbase lists 'Rabil Ventures' — discrepancy to verify in P4); headcount conflicting 6,990-10,000; revenue estimates conflict ($1.6B Getlatka vs ~$3B press) — no audited figures. Products: Voyager (enterprise), Breeze (SMB, $1-2/unit/mo), RentCafe, CommercialEdge, Matrix. Stack: ASP.NET/C#/SQL Server/SOAP behind Cloudflare + Route53 + Proofpoint. GitHub org archived Sep 2025. Live antitrust class action Duffy v. Yardi (W.D. Wash.) over algorithmic rent pricing — material for P2/P4/P6. G2/Capterra 4.0-4.6 with recurring complaints: slow, dated UI, no open API. Glassdoor 4.0 (3,102 reviews).
