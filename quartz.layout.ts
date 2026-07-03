import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// Category-grouped left nav (S3 · R2/R3). Renders S2's 12 book-spine categories
// from the numbered content/ folders, with the warrant-exceptions cluster (#7) as
// the single 3-level branch (7a/7b) and a segregated, collapsed `Cases` node
// (S4 · R5/§9). The default numeric `sortFn` already collates 1,2,…,9,10,11,12 and
// sorts the lettered `cases` node after the numbered categories, so it is kept as-is.
//
// `mapFn` MUST be closure-free: Quartz serializes it with `.toString()` and
// re-evaluates it client-side, so it cannot reference any outer-scope variable —
// the slug→display-name table is declared INSIDE the function body.
const categoryExplorer = Component.Explorer({
  folderDefaultState: "collapsed",
  folderClickBehavior: "collapse",
  useSavedState: true,
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
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
      "Discord Community": "https://discord.gg/cRFFHYye7t",
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
