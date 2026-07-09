---
title: "United States v. Smith (2024)"
type: case
citation: "110 F.4th 817 (2024)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Court of Appeals for the Fifth Circuit
court_level: coa
circuit: 5th
year: 2024
date_decided: 2024-08-09
docket: 23-60321
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2026-07-03
  as_of_treatment: 2026-07-03
  composite_basis: principal-holding
  composite_basis_ref: search.digital.geofence-threshold
  varies_by_point: true
  scope_note: "Composite reflects the search-threshold holding (geofence acquisition IS a search), confirmed by Chatrie v. United States (2026). The categorical general-warrant holding is the point that varies — binding in the Fifth Circuit, not adopted by SCOTUS."
  point_overrides:
    - point: search.warrant.geofence-general-warrant
      point_label: Geofence warrants are categorically unconstitutional general warrants
      field_i_validity: caution
      as_of_treatment: 2026-07-03
      s3_binding_status: bound
      by:
        - name: Chatrie v. United States
          cluster_id: 10881683
          cite: "609 U.S. ___ (2026)"
          field_ii: limited
      scope_note: "Binding in the Fifth Circuit; SCOTUS in Chatrie expressly declined to adopt the categorical rule — the probable-cause/particularity of geofence warrants is the live question on Chatrie's remand."
lake:
  record_id: "United States v. Smith (2024)"
  status: verified
  projected_at: 2026-07-06
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10036119/united-states-v-smith/"
  cluster_id: 10036119
  opinion_id: 10502720
  identity_checked: true
homes:
  - page: "[[Reverse-Keyword and Geofence Warrants]]"
    role: "Key — Circuit anchor (geofence)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — umbrella)"
related: ["[[Chatrie v. United States]]", "[[Carpenter v. United States]]", "[[United States v. Leon]]", "[[The Warrant Requirement]]", "[[The Exclusionary Rule]]"]
aliases: ["United States v. Smith", "United States v. Smith (5th Cir. 2024)"]
tags: ["case", "fourth-amendment", "search", "digital-privacy", "geofence", "location-history", "good-faith-exception"]
holding: "Acquiring Google Location History through a geofence warrant is a Fourth Amendment search under Carpenter, and geofence warrants — which identify everyone in an area rather than a particularized suspect — are modern-day general warrants, unconstitutional under the Fourth Amendment; suppression was nonetheless denied under the Leon good-faith exception given the technology's novelty."
---

# United States v. Smith (2024)

*110 F.4th 817 (5th Cir. 2024)* (No. 23-60321) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Good law — varies by point**
<!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-03: cluster 10036119 → opinion 10502720 — see frontmatter/Sources. -->

## Background
On February 5, 2018, three men robbed Sylvester Cobbs, a contract route driver for the U.S. Postal Service, of registered mail bags containing over $60,000 as he arrived at the Lake Cormorant, Mississippi post office. Surveillance video showed the assailant apparently using a cell phone before and after the robbery, but nine months of investigation produced no suspect. Postal inspectors then obtained a **geofence warrant** directing Google to disclose Location History for every device within a roughly 98,000-square-meter box around the post office during the robbery window. The returns led to Jamarr Smith and Gilbert McThunel, and follow-up investigation identified Thomas Iroko Ayodele. A jury convicted all three of robbery and conspiracy; they appealed the denial of their motion to suppress the geofence-derived evidence.

## Issue
Whether obtaining Google Location History through a geofence warrant is a Fourth Amendment search, and whether a warrant that identifies everyone within a geographic area — rather than a particularized suspect — satisfies the Fourth Amendment.

## Rule
Acquiring geofence Location History is a **search** under *[[Carpenter v. United States|Carpenter]]* — the comprehensive, automatically generated record of a phone's movements invades a reasonable expectation of privacy even though Google holds the data. And because a geofence warrant works backwards — identifying every person in an area on the chance one is the suspect, rather than searching a particularized target — the panel held it fails the Fourth Amendment at the threshold: "We hold that geofence warrants are modern-day general warrants and are unconstitutional under the Fourth Amendment. However, considering law enforcement's reasonable conduct in this case in light of the novelty of this type of warrant, we uphold the district court's determination that suppression was unwarranted under the good-faith exception." — 110 F.4th at 838. ^pin-838

## Application
The geofence returns exposed the private movements of everyone near the Lake Cormorant post office, not just the eventual defendants — the inverted, dragnet character the panel found indistinguishable from a general warrant. But the inspectors had consulted prosecutors, obtained a magistrate's authorization, and navigated a genuinely novel technology with no controlling precedent; on those facts the court applied *[[United States v. Leon|Leon]]* good faith rather than the exclusionary rule.

## Conclusion
Convictions **affirmed**: the geofence warrant was unconstitutional, but suppression was unwarranted under the [[The Good-Faith Exception|good-faith exception]]. King, J., wrote for the panel (King, Ho, Engelhardt, JJ.).

## Treatment & subsequent history

**Composite: Good law — treatment varies by point.** *Smith*'s two holdings have diverged: the search-threshold holding is now nationally settled in its favor; the categorical general-warrant holding remains binding only in the Fifth Circuit.

| Point of law | Status | Controlling authority |
|---|---|---|
| Acquiring geofence Location History is a Fourth Amendment search | **Good law** | Confirmed by *[[Chatrie v. United States]]*, 609 U.S. ___ (2026) — SCOTUS reached the same result, applying and extending *[[Carpenter v. United States|Carpenter]]* |
| Geofence warrants are categorically unconstitutional general warrants | **Caution** | *[[Chatrie v. United States|Chatrie]]* expressly declined to adopt the categorical rule; the probable-cause/[[Particularity\|particularity]] question is live on *[[Chatrie v. United States|Chatrie]]*'s remand. Binding in the Fifth Circuit; the persuasive minority position elsewhere |

The Supreme Court's 2026 *[[Chatrie v. United States|Chatrie]]* decision resolved the circuit split *Smith* anchored: acquiring geofence Location History **is** a search, as *Smith* held (and the Fourth Circuit's [[Reading and Citing Cases#en-banc|en banc]] *[[Chatrie v. United States|Chatrie]]* had fractured over). But the Court stopped at the threshold — it did not decide whether any geofence warrant can satisfy probable cause and [[Particularity|particularity]], so *Smith*'s stronger point remains the minority answer to a question SCOTUS left open.

## Appears on
- [[Reverse-Keyword and Geofence Warrants]] — *Key — Circuit anchor (geofence)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — umbrella)*

## Sources
- [*United States v. Smith*, 110 F.4th 817 (5th Cir. 2024)](https://www.courtlistener.com/opinion/10036119/united-states-v-smith/) — pinpoint: 838 (general-warrant holding + good-faith disposition; quote string-matched against the CL opinion text 2026-07-03).
- [*Chatrie v. United States*, 609 U.S. ___ (2026)](https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/) — the search-threshold confirmation and the reserved probable-cause/particularity question.
