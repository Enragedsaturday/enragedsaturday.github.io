import test, { describe } from "node:test"
import assert from "node:assert"
import { resolveTreatment, shouldDraftBanner } from "./caseHelpers"

// S5 — entry-model resolver + R15 banner predicate unit checks. Pure functions
// over the documented Appendix-B frontmatter shape (no component / SCSS imports),
// runnable under `tsx --test`.

describe("resolveTreatment (S5 R14 — one vocabulary before/after the projector)", () => {
  test("projected 3-field shape (Belton-like): caution + varies + overrides", () => {
    const rt = resolveTreatment({
      treatment: {
        field_i_validity: "caution",
        varies_by_point: true,
        as_of_content: "2026-06-30",
        as_of_treatment: "2026-06-30",
        point_overrides: [{ point: "search.vehicle.sia-recent-occupant", field_i_validity: "superseded" }],
      },
    })
    assert.ok(rt)
    assert.equal(rt!.fieldI, "caution")
    assert.equal(rt!.label, "Caution")
    assert.equal(rt!.varies, true)
    assert.equal(rt!.overrides.length, 1)
  })

  test("legacy `limited` maps to caution + carries the varies warning (S1 A4)", () => {
    const rt = resolveTreatment({ treatment: { status: "limited", as_of: "2026-06-30" } })
    assert.ok(rt)
    assert.equal(rt!.fieldI, "caution")
    assert.equal(rt!.varies, true) // A4: a legacy `limited` case always warns varies
    assert.equal(rt!.legacy, "limited")
  })

  test("legacy `overruled` / `abrogated` map to superseded", () => {
    assert.equal(resolveTreatment({ treatment: { status: "overruled" } })!.fieldI, "superseded")
    assert.equal(resolveTreatment({ treatment: { status: "abrogated" } })!.fieldI, "superseded")
  })

  test("legacy `good` maps to good_law", () => {
    assert.equal(resolveTreatment({ treatment: { status: "good" } })!.fieldI, "good_law")
  })

  test("R14 fail-visible: an UNMAPPED legacy status renders `unverified`", () => {
    const rt = resolveTreatment({ treatment: { status: "frobnicate" } })
    assert.ok(rt)
    assert.equal(rt!.fieldI, "unverified")
  })

  test("no treatment block => null", () => {
    assert.equal(resolveTreatment({}), null)
    assert.equal(resolveTreatment(undefined), null)
  })
})

describe("shouldDraftBanner (S5 R15 — defense-in-depth behind the publish gate)", () => {
  test("lake.status under_review banners (projected Belton/Smith state)", () => {
    assert.equal(
      shouldDraftBanner({ type: "case", lake: { status: "under_review" }, treatment: { field_i_validity: "caution" } }),
      true,
    )
  })

  test("lake.status draft banners", () => {
    assert.equal(shouldDraftBanner({ type: "case", lake: { status: "draft" } }), true)
  })

  test("verified good-law case does NOT banner", () => {
    assert.equal(
      shouldDraftBanner({ type: "case", lake: { status: "verified" }, treatment: { field_i_validity: "good_law" } }),
      false,
    )
  })

  test("verified caution case does NOT banner (banner gates on draft/unverified only)", () => {
    assert.equal(
      shouldDraftBanner({ type: "case", lake: { status: "verified" }, treatment: { field_i_validity: "caution" } }),
      false,
    )
  })

  test("R14 crossover: an unmapped legacy status (=> unverified) banners even if lake says verified", () => {
    assert.equal(
      shouldDraftBanner({ type: "case", lake: { status: "verified" }, treatment: { status: "frobnicate" } }),
      true,
    )
  })

  test("Field-I unverified banners with no lake block at all", () => {
    assert.equal(shouldDraftBanner({ type: "case", treatment: { field_i_validity: "unverified" } }), true)
  })

  test("empty / missing frontmatter does not banner", () => {
    assert.equal(shouldDraftBanner({}), false)
    assert.equal(shouldDraftBanner(undefined), false)
  })
})
