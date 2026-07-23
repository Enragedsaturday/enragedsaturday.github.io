import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import style from "./styles/draftBanner.scss"
import { classNames } from "../util/lang"
import { isCasePage, resolveLakeStatus, shouldDraftBanner } from "./caseHelpers"

// S5 · R15 — draft-state banner (self-interview SD4). Defense-in-depth behind
// S2 R12's page↔record publish gate: any case page whose `lake.status` is
// `draft`/`under_review`, or whose resolved Field-I composite is `unverified`
// (incl. an UNMAPPED legacy status via R14), renders a top-of-content ⚪ banner
// so S1 R2's "⚪ never reaches a reader unbannered" holds even on previews.
// First-class `slip_opinion` pages render a distinct informational banner because
// their identity is verified even though an official reporter citation is pending.
//
// Fully data-driven off frontmatter (no content edits). Renders nothing on a
// verified case page, and nothing on non-case pages.
//
// NOTE (S2 handoff): the two projected pages *New York v. Belton* / *United
// States v. Smith* are `under_review` post-S2, so they WILL banner until R15's
// publish gates flip them to `verified` — that is correct defense-in-depth
// behavior, not a bug.

export default (() => {
  const DraftBanner: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
    if (!isCasePage(fileData)) return null
    const fm = fileData.frontmatter as Record<string, any>
    const lakeStatus = resolveLakeStatus(fm) ?? "unverified"
    if (lakeStatus === "slip_opinion") {
      return (
        <aside
          class={classNames(displayClass, "slip-banner")}
          role="note"
          data-lake-status="slip_opinion"
        >
          <span class="slip-banner-icon" aria-hidden="true">
            📄
          </span>
          <span class="slip-banner-text">
            Slip opinion — recent decision, not yet assigned an official reporter citation. Identity
            verified against the court's slip opinion; the official cite will be added when it
            issues, and subsequent-treatment verification is pending.
          </span>
        </aside>
      )
    }
    if (!shouldDraftBanner(fm)) return null
    return (
      <aside
        class={classNames(displayClass, "draft-banner")}
        role="note"
        data-lake-status={lakeStatus}
      >
        <span class="draft-banner-dot" aria-hidden="true">
          ⚪
        </span>
        <span class="draft-banner-text">
          This entry has not completed verification — treat as unverified.
        </span>
      </aside>
    )
  }

  DraftBanner.css = style
  return DraftBanner
}) satisfies QuartzComponentConstructor
