---
title: "Chatrie v. United States"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2026
date_decided: 2026-06-29
docket: 25-112
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2026-06-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chatrie v. United States
  varies_by_point: false
  scope_note: "New Binding — SCOTUS anchor (decided 2026-06-29, post-capture). Geofence/Google Location History acquisition IS a Fourth Amendment search; the probable-cause/particularity of geofence warrants was left open on remand. Slip-op sourced; CL-verified 2026-07-02 (cluster 10881683 → lead opinion 11349205)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/"
  cluster_id: 10881683
  opinion_id: 11349205
  identity_checked: false
homes:
  - page: "[[Two Definitions of Search]]"
    role: "Key — Anchor"
  - page: "[[The Third-Party Doctrine and Digital Surveillance]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carpenter v. United States]]", "[[United States v. Jones]]", "[[Katz v. United States]]", "[[Smith v. Maryland]]", "[[The Warrant Requirement]]", "[[Standing to Challenge a Search]]", "[[The Exclusionary Rule]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "digital-privacy", "geofence", "location-history", "third-party-doctrine"]
holding: "Acquiring a cell-phone user's Google Location History (geofence) data is a Fourth Amendment search — there is a reasonable expectation of privacy in the record of one's phone's location, even for a short period and even when the data is held by a third party; the Court did not decide whether geofence warrants satisfy probable cause and particularity, vacating and remanding."
lake:
  record_id: Chatrie v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Chatrie v. United States

*609 U.S. ___ (2026)* (No. 25-112) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-02: cluster 10881683 → lead opinion 11349205 — see frontmatter/Sources. -->

## Background
Investigating a 2019 armed robbery of a Midlothian, Virginia credit union, police obtained a **geofence warrant** directing Google to disclose **Location History** for every device within a 150-meter radius of the bank during a roughly one-hour window around the robbery. That "reverse-location" process ultimately identified Okello Chatrie. He moved to suppress, arguing that compelling Google to produce his Location History was a warrantless Fourth Amendment search. The Fourth Circuit — on rehearing **en banc**, splitting 7–7 on whether a search occurred — affirmed the denial of suppression (136 F.4th 100), teeing up the threshold question for the Supreme Court.

## Issue
Whether the government conducts a Fourth Amendment "search" when it acquires a person's Google Location History (geofence) data — records of a cell phone's location — held by a third-party provider.

## Rule
Yes. Acquiring a cell-phone user's **Google Location History is a Fourth Amendment search**. In the Court's words: "An individual has a reasonable expectation of privacy in records about his cell phone's location, and police intrude on that constitutionally protected interest when they demand the information—even though for only a limited time, and from a third-party tech company." The protection holds **even for a limited time** and **even though a third party holds the records**. The Court rejected the argument that Location History (off by default / opt-in) is "voluntarily shared" and thus stripped of protection by the third-party doctrine, **applying and extending *[[Carpenter v. United States|Carpenter]]*** to bulk reverse-location data. *Chatrie v. United States*, 609 U.S. ___ (2026) (No. 25-112) (slip op.). ^pin-op

Critically, the Court **did not** hold geofence warrants categorically unconstitutional. It **expressly declined** to decide whether *this* geofence warrant satisfied the Fourth Amendment's **probable-cause and particularity** requirements, leaving that question for remand.

## Application
Police compelled Google to produce Location History for all devices in a geographic area and time window — an "all-encompassing" record of individuals' movements generated automatically and held by a third party. Under *Carpenter*'s logic, that acquisition invaded a reasonable expectation of privacy and was therefore a search; the third-party/opt-in rationale the Fourth Circuit panel had relied on did not defeat that protection.

## Conclusion
Acquiring geofence Location History is a Fourth Amendment search. The judgment was **vacated and remanded** for the lower courts to decide the **probable-cause and particularity** of the geofence warrant — the question the Court left open. **Kagan, J.**, delivered the opinion of the Court, joined by Roberts, C.J., and Sotomayor, Kavanaugh, and Jackson, JJ.; Jackson, J., filed a concurring opinion, joined by Sotomayor, J.; Gorsuch, J., concurred in the judgment (making the judgment **6–3**); Alito, J., dissented, joined by Thomas, J., as to Part I and by Barrett, J., as to Parts II–B, II–C–1, and II–C–2; Barrett, J., filed a separate dissenting opinion.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** anchor on the geofence search-threshold question.
- **Doctrinal effect:** **RESOLVES** the former circuit split on whether acquiring geofence Location History is a *search* (5th Cir. *[[The Warrant Requirement|Smith]]* = yes; 4th Cir. en banc *Chatrie* = fractured) — **it is a search**. *Smith*'s further holding that geofence warrants are "modern-day general warrants" and **categorically unconstitutional** was **not** adopted; it is now the persuasive minority position feeding the **remanded** probable-cause/particularity question — the new live frontier.
- **CL-confirm: VERIFIED (2026-07-02).** CourtListener **cluster** `10881683` **is** the genuine SCOTUS *Chatrie* (`scotus / 25-112 / 2026-06-29`); its lead opinion is `11349205`, against which the Rule quote above was matched verbatim. The earlier "corrupted object" warning was a cluster-vs-opinion ID mix-up: `10881683` is a *cluster* id, and fetching it from the `/opinions/` endpoint returns an unrelated case — use `/clusters/10881683/` or opinion `11349205` instead. See Sources.

## Appears on
- [[Two Definitions of Search]] — *Key — Anchor*
- [[The Third-Party Doctrine and Digital Surveillance]] — *Key — Progeny / Refinement*

## Sources
- *Chatrie v. United States*, 609 U.S. ___ (2026) (No. 25-112) — **slip opinion (PRIMARY):** https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf — decided June 29, 2026.
- SCOTUSblog case page — https://www.scotusblog.com/cases/chatrie-v-united-states/
- Justia, *Chatrie v. United States*, 609 U.S. ___ (2026) — https://supreme.justia.com/cases/federal/us/609/25-112/
- Cornell LII (Supreme Court text, No. 25-112) — https://www.law.cornell.edu/supremecourt/text/25-112
- Decision below: *United States v. Chatrie*, 136 F.4th 100 (4th Cir. 2025) (en banc) — https://www.courtlistener.com/opinion/10443725/united-states-v-okello-chatrie/
- CourtListener: *Chatrie v. United States* — https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/ — **verified 2026-07-02** (cluster 10881683 → lead opinion 11349205; case name, docket 25-112, and decision date 2026-06-29 confirmed against the cluster record and opinion text). The earlier "corrupted object" warning was a cluster-vs-opinion ID confusion: `10881683` is the **cluster** id and must not be fetched from the `/opinions/` endpoint (that resolves to an unrelated case); the lead **opinion** id is `11349205`.
