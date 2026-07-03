import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// "TOC-tree" left nav (O2: S3 owns the 13-category tree, S4 owns this nav model —
// audit CODE-05 comment refresh). Top-level categories are the only accordion;
// nested folders render as always-open branches whose header links to their
// overview. The displayNames table targets the O2 Appendix-A tree; until S3's
// restructure lands at execution, unmatched folders fall back to their own names.
// ORDERING (S3 A8 — user decision 2026-07-03): final ordering reads frontmatter
// `weight:` (pages) + folder-index `weight:` (categories); the numeric-prefix
// `sortFn` below is the mockup interim and is superseded on this point.
//
// `mapFn`/`sortFn` MUST be closure-free: Quartz serializes them with `.toString()`
// and re-evaluates them client-side, so they cannot reference any outer-scope
// variable — the slug→display-name table is declared INSIDE the function body.
const categoryExplorer = Component.Explorer({
  folderDefaultState: "collapsed",
  folderClickBehavior: "collapse",
  useSavedState: true,
  // About is footer-owned (S4); keep it (and tags) out of the tree
  filterFn: (node) => node.slugSegment !== "tags" && node.slugSegment !== "about",
  // Order by the numeric filename/slug prefix at every level, so authored page
  // order (e.g. Proof Ladder first) holds instead of alphabetical. Closure-free.
  sortFn: (a, b) =>
    (a.slugSegment ?? "").localeCompare(b.slugSegment ?? "", undefined, {
      numeric: true,
      sensitivity: "base",
    }),
  mapFn: (node) => {
    const displayNames: Record<string, string> = {
      "1-foundations": "1 · Foundations & the Fourth Amendment",
      "2-standards-of-proof": "2 · Standards of Proof",
      "3-searches": "3 · Searches",
      "01-two-definitions-of-search": "Two Definitions of Search",
      "4-seizures": "4 · Seizures",
      "06-arrests": "Arrests",
      "5-the-warrant": "5 · The Warrant",
      "01-getting-a-warrant": "Getting a Warrant",
      "02-executing-a-warrant": "Executing a Warrant",
      "6-warrant-exceptions": "6 · Warrant Exceptions",
      "01-searching-a-person": "Searching a Person",
      "02-searching-a-vehicle": "Searching a Vehicle",
      "03-home-entry-and-search": "Home Entry & Search",
      "06-programmatic-special-needs": "Programmatic & Special-Needs Searches",
      "7-exclusionary-rule": "7 · The Exclusionary Rule, Remedies & Standing",
      "8-confessions-fifth-amendment": "8 · Confessions, Interrogation & the Fifth Amendment",
      "9-right-to-counsel": "9 · The Right to Counsel",
      "10-fair-trial-reliability": "10 · Fair-Trial & Reliability Doctrines",
      "11-force-liability": "11 · Use of Force & Liability",
      "12-research-reference": "12 · Legal System, Research & Reference",
      "13-instructor-craft": "13 · Instructor Craft & Study",
    }
    if (node.isFolder) {
      const mapped = displayNames[node.slugSegment]
      if (mapped) {
        node.displayName = mapped
      }
    }
  },
})

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  // S3 · R4/R5 — case-data component layer (progressive enhancement over portable
  // markdown + frontmatter). These self-gate and degrade safely on every page type:
  //   • CaseTable      — emits a hidden case-index data island ONLY on pages with a
  //                      table; its script enhances any GFM table that has a Case/Name
  //                      column into a sortable/filterable view. JS off ⇒ static table.
  //   • DoctrineFlowchart — renders nothing; its script makes mermaid `click` nodes
  //                      SPA-safe deep-links. JS off ⇒ static mermaid diagram.
  //   • CaseBrowser    — renders its faceted UI ONLY on a page with frontmatter
  //                      `type: case-browser` (or `caseBrowser: true`); else null.
  //                      JS off ⇒ static list of case links + Case Index link.
  afterBody: [
    Component.CaseTable(),
    Component.DoctrineFlowchart(),
    Component.CaseBrowser(),
  ],
  // S4 · stock Quartz GitHub/Discord links dropped; attribution lives on About.
  footer: Component.Footer({
    links: {
      "About this site": "/about",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    // S3 · R4 #1 — treatment + authority-weight badges (case pages only; degrades to
    // the plain-markdown header line already on the page).
    Component.TreatmentBadge(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    categoryExplorer,
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
    // S3 · R4 #6 — cross-reference panel (case pages only; multi-homing N6 + related +
    // limited/abrogated/overruled-by, from frontmatter). Degrades to nothing.
    Component.CrossRefPanel(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    categoryExplorer,
  ],
  right: [],
}
