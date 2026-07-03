import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/treatmentBadge.scss"
import { classNames } from "../util/lang"
import { resolveRelative } from "../util/path"
import {
  GOOD_LAW_SLUG,
  fieldICssKey,
  isCasePage,
  resolveTreatment,
  treatmentHoverTitle,
  weightTierKey,
} from "./caseHelpers"

// S4 · pill-as-anchor (mechanism — audit COH-18): the treatment pill links to the
// "how we verify" page via the ONE exported constant (caseHelpers.GOOD_LAW_SLUG), so
// hovering it fires the standard `a.internal` popover and clicking lands on the
// methodology.
//
// S5 · placement/format: the case-page header renders the Field-I COMPOSITE pill
// (PRACTICES §2 / S1 R2) + the varies-by-point chip (S2 R5: the marker rides with the
// composite everywhere) + the separate, neutral authority-weight label. Dates live
// BEHIND the hover (S1 R3 placement — data model + hover + About page, never inline);
// the hover carries the S4 R6 provenance template (dual dates, degrading to single
// as-of). Legacy single-status frontmatter renders through the S1 A4 mapping
// (caseHelpers.resolveTreatment — audit COH-11).
//
// Degraded state: the plain-markdown header line already on the page. This component
// ENHANCES that line; with components stripped, the text remains.

export default (() => {
  const TreatmentBadge: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
    if (!isCasePage(fileData)) return null
    const fm = fileData.frontmatter as Record<string, any>
    const rt = resolveTreatment(fm)
    const weight = fm.authority_weight

    // empty/degraded: nothing to enhance
    if (!rt && !weight) return null

    return (
      <div class={classNames(displayClass, "treatment-badges")}>
        {rt && (
          <a
            href={resolveRelative(fileData.slug!, GOOD_LAW_SLUG)}
            class={`internal treatment-badge treatment-${fieldICssKey(rt.fieldI)}`}
            data-treatment={rt.fieldI}
            title={treatmentHoverTitle(rt)}
          >
            <span class="treatment-dot" aria-hidden="true"></span>
            <span class="treatment-label">{rt.label}</span>
          </a>
        )}
        {rt?.varies && (
          <a
            href="#treatment--subsequent-history"
            class="treatment-varies"
            title="Treatment varies by point of law — see the Treatment section for the point-scoped status"
          >
            varies by point
          </a>
        )}
        {weight && (
          <span class="authority-weight" data-weight-tier={weightTierKey(weight)} title="Authority weight">
            {String(weight)}
          </span>
        )}
      </div>
    )
  }

  TreatmentBadge.css = style
  return TreatmentBadge
}) satisfies QuartzComponentConstructor
