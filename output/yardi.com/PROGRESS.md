# Dossier: yardi.com
Started: 2026-07-08T23:26:47Z
Iteration: 0

## Phases
- [x] P1 Discovery — complete 2026-07-08 (01-discovery.md; raw/whois.json, raw/dns.json, raw/website-content.json)
- [x] P2 Market — complete 2026-07-08 (02-market.md)
- [x] P3 Technical — complete 2026-07-08T23:59Z (03-technical.md; raw/github-repos.json, raw/github-org-yardisystems.json)
- [ ] P4 Claims — blocked (needs P1, P3)
- [ ] P4.5 Red Team — blocked (needs P4)
- [ ] P5 Academic
- [ ] P6 Valuation — blocked (needs P1-P4.5)
- [ ] P7 Report — blocked (needs P6)

## Blockers
- P1 environment gaps (non-fatal, work around applied): direct fetch of yardi.com blocked (Cloudflare + egress proxy 403) -> first-party content captured via WebSearch snippets; WHOIS port 43/RDAP blocked -> registration data from whois.com snippet (single independent source); TXT DNS lookup timed out; llms.txt / .well-known check UNCONFIRMED (no indexed llms.txt found, but could not probe directly) — downstream phases with direct access must re-check.

## Notes
- P3 key facts: GitHub org YardiSystems = 13 repos, ALL forks, 0 original code ever, 2 stars total, entire org archived ~Sep 15 2025 — AI-tooling forks (Flowise, bolt.diy) pushed days before archiving => likely moved private, not engineering halt (inference). Official API = SOAP/WSDL only, partner-gated (2yrs + 3 Voyager clients; $25k/yr/interface per SINGLE independent source — P4 verify), no public REST/SDK/portal (VERIFIED, 2+ independent: yhavin/yardi-sdk, api-evangelist/yardi, integration vendors); integrators resort to Playwright browser automation. Voyager = per-client instances at {client}.yardiasp13.com in Yardi's OWN ~15 data centers (own-DC corroborated independently; DC count first-party) — ASP-era hosted monolith, dedicated DB per client. Front end AngularJS/jQuery-era (EOL). Real ML hiring (PyTorch/spaCy production, LinkedIn — INDEPENDENT) lends consistency to first-party "Virtuoso" AI claims (incl. Claude connectors — unverified). Pockets of EKS/Terraform/GitHub Actions (SF DevOps posting, attribution uncertain). Kooboo CMS copyright "Yardi Technology Limited" — relationship unconfirmed, P4 flag. Biggest gap: ~all code private, quality/security/modernization unobservable.
- P2 key facts: TAM ~$7B global core PM software 2026 (analyst cluster $6.5-7.7B corroborated by bottom-up JCHS units x AppFolio audited $101/unit ARPU); broad-scope TAM $25-30B (low confidence, scope ambiguity). Yardi SOM = its own est. revenue $1.6-3B (~20-40% of core). Quadrant: Yardi Leader, Vision 7 / Execution 9; AppFolio 8/8, Entrata 8/7, RealPage 7/7, MRI 7/7; Buildium/Rent Manager/ResMan niche. Top market risk: algorithmic-pricing legal storm — DOJ/RealPage consent decree (Nov 2025, 7-yr conduct remedies) is now plaintiffs' template while Duffy v. Yardi proceeds under per se standard (narrowed Apr 2026, still in discovery). MRI for sale at up to $10B; Entrata $4.3B valuation w/ Blackstone. Gaps for P4/P6: Yardi revenue 2x spread unresolved; Revenue IQ revenue share unknown; competitor "best software" content is ADVERSARIAL (vendors ranking themselves) — corroborates but does not independently verify Yardi UX complaints.
- P1 key facts: Yardi Systems Inc., founded 1984 by Anant Yardi, HQ Santa Barbara CA; private/founder-owned, reportedly no outside capital (Crunchbase lists 'Rabil Ventures' — discrepancy to verify in P4); headcount conflicting 6,990-10,000; revenue estimates conflict ($1.6B Getlatka vs ~$3B press) — no audited figures. Products: Voyager (enterprise), Breeze (SMB, $1-2/unit/mo), RentCafe, CommercialEdge, Matrix. Stack: ASP.NET/C#/SQL Server/SOAP behind Cloudflare + Route53 + Proofpoint. GitHub org archived Sep 2025. Live antitrust class action Duffy v. Yardi (W.D. Wash.) over algorithmic rent pricing — material for P2/P4/P6. G2/Capterra 4.0-4.6 with recurring complaints: slow, dated UI, no open API. Glassdoor 4.0 (3,102 reviews).
