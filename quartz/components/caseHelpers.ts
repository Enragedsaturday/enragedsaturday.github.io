// Shared server-side helpers for the CSSI case-data component layer (S3 · R4 / S4 · R9).
// These read the documented Appendix-B case frontmatter convention ONLY — no bespoke,
// component-only load-bearing syntax (R5 portability guardrail). All inputs are plain
// frontmatter keys + Obsidian `[[wikilinks]]`, so content stays portable markdown.

import { QuartzPluginData } from "../plugins/vfile"
import { FilePath, FullSlug, resolveRelative, simplifySlug, slugifyFilePath } from "../util/path"

// S4 · R5 — the pill/anchor target: ONE exported constant (audit COH-18; S3's
// restructure re-homes the page, at which point this is the one edit).
export const GOOD_LAW_SLUG = "2-legal-system-research/Verifying-Good-Law" as FullSlug

// Canonical good-law treatment axis (S1 §3.D / N13). Kept STRICTLY separate from the
// orthogonal authority-weight axis — the two are never merged.
export const TREATMENT_STATUSES = [
  "good",
  "criticized",
  "limited",
  "abrogated",
  "overruled",
] as const

export type TreatmentStatus = (typeof TREATMENT_STATUSES)[number]

export const TREATMENT_LABELS: Record<string, string> = {
  good: "Good law",
  criticized: "Criticized",
  limited: "Limited",
  abrogated: "Abrogated",
  overruled: "Overruled",
}

// ---------------------------------------------------------------------------
// S5 — Field-I composite validity (PRACTICES §2 / S1 R2), rendered everywhere a
// treatment signal appears. Pages that still carry the LEGACY single-status
// frontmatter render THROUGH the S1 Amendment A4 migration mapping (audit COH-11 —
// the only sanctioned old→new translation), so the reader sees one vocabulary
// before and after S2's projector lands.

export const FIELD_I_KEYS = [
  "good_law",
  "history",
  "caution",
  "questioned",
  "superseded",
  "unverified",
] as const
export type FieldIKey = (typeof FIELD_I_KEYS)[number]

export const FIELD_I_LABELS: Record<string, string> = {
  good_law: "Good law",
  history: "History",
  caution: "Caution",
  questioned: "Questioned",
  superseded: "Superseded",
  unverified: "Unverified",
}

// css-safe key for status classes (treatment-good-law, treatment-caution, …)
export function fieldICssKey(fieldI: string): string {
  return fieldI.replace(/_/g, "-")
}

// S1 A4 — legacy `treatment.status` → Field-I composite.
export const LEGACY_TO_FIELD_I: Record<string, FieldIKey> = {
  good: "good_law",
  limited: "caution",
  criticized: "caution",
  overruled: "superseded",
  abrogated: "superseded",
}

// Normalize a projected Field-I value: strips glyphs, tolerates the long
// PRACTICES-§2 spellings ("superseded/not_current", "questioned/overruling_risk").
export function normFieldI(v: unknown): FieldIKey | undefined {
  if (typeof v !== "string") return undefined
  const s = v.toLowerCase().trim().split("/")[0].replace(/[^a-z_]/g, "")
  return (FIELD_I_KEYS as readonly string[]).includes(s) ? (s as FieldIKey) : undefined
}

export interface PointOverride {
  point?: string
  point_label?: string
  field_i_validity?: string
  field_ii?: string
  by?: string
  by_cite?: string
  as_of_treatment?: string
  scope_note?: string
}

export interface ResolvedTreatment {
  fieldI: FieldIKey
  label: string
  varies: boolean
  legacy?: string // set when the page predates the S2 projection (rendered via A4)
  asOfContent?: string
  asOfTreatment?: string
  note?: string
  overrides: PointOverride[]
}

// Read a case page's treatment from frontmatter, whichever generation it carries:
// (a) the S2-projected 3-field shape (`field_i_validity` + dual dates + overrides),
// (b) the legacy single-status shape, mapped via S1 A4. Returns null when the page
// carries no treatment block at all.
export function resolveTreatment(fm: Record<string, any> | undefined): ResolvedTreatment | null {
  const t = fm?.treatment as Record<string, any> | undefined
  if (!t) return null

  const projected = normFieldI(t.field_i_validity)
  if (projected) {
    const overrides = Array.isArray(t.point_overrides) ? (t.point_overrides as PointOverride[]) : []
    return {
      fieldI: projected,
      label: FIELD_I_LABELS[projected],
      varies: t.varies_by_point === true || overrides.length > 0,
      asOfContent: t.as_of_content ? String(t.as_of_content) : undefined,
      asOfTreatment: t.as_of_treatment ? String(t.as_of_treatment) : undefined,
      note: t.scope_note ? String(t.scope_note) : t.note ? String(t.note) : undefined,
      overrides,
    }
  }

  const legacy = normStatus(t.status)
  if (!legacy) return null
  const mapped = LEGACY_TO_FIELD_I[legacy] ?? "unverified"
  return {
    fieldI: mapped,
    label: FIELD_I_LABELS[mapped],
    // A4: every `limited` case carries ≥1 point override post-projection; pre-projection
    // the varies warning rides on the mapped composite so the reader is never unwarned.
    varies: legacy === "limited",
    asOfTreatment: t.as_of ? String(t.as_of) : undefined,
    note: t.note ? String(t.note) : undefined,
    legacy,
    overrides: [],
  }
}

// S4 · R6 — the provenance tooltip template (title attr), shared by the page-header
// pill and every table-injected pill: status · dual dates (degrading to single
// as-of) · one-line note · methodology pointer.
export function treatmentHoverTitle(rt: ResolvedTreatment): string {
  const dates =
    rt.asOfContent && rt.asOfTreatment
      ? `content verified ${rt.asOfContent} · treatment checked ${rt.asOfTreatment}`
      : rt.asOfTreatment
        ? `checked as of ${rt.asOfTreatment}`
        : undefined
  return [
    `Treatment: ${rt.label}${rt.varies ? " (varies by point)" : ""}`,
    dates,
    rt.note,
    "Click: how we verify good law",
  ]
    .filter(Boolean)
    .join(" · ")
}

// The orthogonal six-tier authority-weight lexicon (S1 §4). Used only to derive a
// stable css key for the (visually distinct) weight label — never to color the
// treatment badge.
export function weightTierKey(weight: unknown): string {
  if (typeof weight !== "string") return "unknown"
  const w = weight.toLowerCase()
  if (w.includes("binding") && w.includes("scotus")) return "binding-scotus"
  if (w.includes("binding")) return "binding-circuit"
  if (w.includes("non-precedential") || w.includes("nonprecedential")) return "persuasive-nonprec"
  if (w.includes("state")) return "persuasive-state"
  if (w.includes("persuasive")) return "persuasive"
  if (w.includes("historical")) return "historical"
  return "other"
}

export function normStatus(status: unknown): string | undefined {
  if (typeof status !== "string") return undefined
  const s = status.toLowerCase().trim()
  return s.length > 0 ? s : undefined
}

export function isKnownStatus(status: string | undefined): status is TreatmentStatus {
  return !!status && (TREATMENT_STATUSES as readonly string[]).includes(status)
}

export interface ParsedWikilink {
  target: string // page name, e.g. "Brigham City v. Stuart"
  anchor?: string // "#rule" or "#^pin-404"
  alias?: string // display text after the pipe
}

// Parse an Obsidian wikilink string from frontmatter, e.g. "[[Case#rule|alias]]".
// Tolerates bare strings (no brackets) so partially-authored frontmatter still works.
export function parseWikilink(raw: unknown): ParsedWikilink | null {
  if (typeof raw !== "string") return null
  let s = raw.trim()
  if (s.length === 0) return null
  const m = s.match(/^\[\[(.+?)\]\]$/)
  if (m) s = m[1]
  let alias: string | undefined
  const pipeIdx = s.indexOf("|")
  if (pipeIdx >= 0) {
    alias = s.slice(pipeIdx + 1).trim()
    s = s.slice(0, pipeIdx)
  }
  let anchor: string | undefined
  const hashIdx = s.indexOf("#")
  if (hashIdx >= 0) {
    anchor = s.slice(hashIdx) // keep leading '#'
    s = s.slice(0, hashIdx)
  }
  const target = s.trim()
  if (target.length === 0) return null
  return { target, anchor, alias }
}

// Resolve a case/page name to a file in the corpus via the documented conventions:
// exact title match, alias slug, or shortest-path slug match (Quartz
// markdownLinkResolution: "shortest"). Returns undefined if unresolved (degraded path).
export function findFileByName(
  allFiles: QuartzPluginData[],
  name: string,
): QuartzPluginData | undefined {
  const wanted = name.trim().toLowerCase()
  if (!wanted) return undefined

  // 1) exact title match
  const byTitle = allFiles.find(
    (f) => (f.frontmatter?.title ?? "").toString().toLowerCase() === wanted,
  )
  if (byTitle) return byTitle

  // 2) slug match (shortest path)
  let wantedSlug: FullSlug | undefined
  try {
    wantedSlug = slugifyFilePath((name.trim() + ".md") as FilePath)
  } catch {
    wantedSlug = undefined
  }
  if (wantedSlug) {
    const bySlug = allFiles.find(
      (f) => f.slug === wantedSlug || (f.slug?.endsWith("/" + wantedSlug) ?? false),
    )
    if (bySlug) return bySlug

    // 3) alias slug match (frontmatter aliases are slugified into file.aliases)
    const byAlias = allFiles.find((f) =>
      ((f as { aliases?: FullSlug[] }).aliases ?? []).some(
        (a) => a === wantedSlug || a.endsWith("/" + wantedSlug),
      ),
    )
    if (byAlias) return byAlias
  }

  return undefined
}

export interface ResolvedLink {
  href: string
  title: string
  resolved: boolean
  anchor?: string
}

// Resolve a frontmatter wikilink to a real href when possible; otherwise hand back the
// bare name so callers degrade to plain (still-legible) text.
export function resolveLink(
  allFiles: QuartzPluginData[],
  currentSlug: FullSlug,
  raw: unknown,
): ResolvedLink | null {
  const parsed = parseWikilink(raw)
  if (!parsed) return null
  const file = findFileByName(allFiles, parsed.target)
  if (file?.slug) {
    const base = resolveRelative(currentSlug, file.slug)
    return {
      href: base + (parsed.anchor ? slugAnchor(parsed.anchor) : ""),
      title: parsed.alias ?? (file.frontmatter?.title ?? parsed.target).toString(),
      resolved: true,
      anchor: parsed.anchor,
    }
  }
  return {
    href: "",
    title: parsed.alias ?? parsed.target,
    resolved: false,
    anchor: parsed.anchor,
  }
}

// Convert "#rule" / "#^pin-404" to the auto-slugged anchor Quartz emits.
function slugAnchor(anchor: string): string {
  if (anchor.startsWith("#^")) return anchor // block ref kept as-is
  // heading anchor: Quartz lowercases + dashes
  return "#" + anchor.slice(1).toLowerCase().replace(/\s+/g, "-")
}

export function decadeOf(year: unknown): string | undefined {
  const y = typeof year === "number" ? year : parseInt(String(year ?? ""), 10)
  if (!Number.isFinite(y) || y < 100) return undefined
  return `${Math.floor(y / 10) * 10}s`
}

export const COURT_LEVEL_LABELS: Record<string, string> = {
  scotus: "U.S. Supreme Court",
  circuit: "Federal Circuit",
  district: "Federal District",
  "state-high": "State High Court",
  "state-app": "State Appellate",
  other: "Other",
}

export function isCasePage(fileData: QuartzPluginData): boolean {
  return fileData.frontmatter?.type === "case"
}

// S5 · R15 — draft-state / unverified banner predicate. A case page renders the
// top-of-content ⚪ banner when its lake PUBLISH state is draft/under_review, OR
// when its resolved Field-I composite is `unverified`. Because resolveTreatment
// maps any UNMAPPED legacy status to `unverified` (S1 A4 / audit COH-11 → R14),
// an injected bogus status fails VISIBLE here (fail-visible, never silent). This
// is defense-in-depth behind S2 R12's page↔record publish gate, so S1 R2's "⚪
// never reaches a reader unbannered" holds even on previews.
export function shouldDraftBanner(fm: Record<string, any> | undefined): boolean {
  if (!fm) return false
  const lakeStatus = String(fm?.lake?.status ?? "")
    .toLowerCase()
    .trim()
  if (lakeStatus === "draft" || lakeStatus === "under_review") return true
  const rt = resolveTreatment(fm)
  return rt?.fieldI === "unverified"
}

export function caseSlugKey(file: QuartzPluginData): string {
  return simplifySlug(file.slug!)
}
