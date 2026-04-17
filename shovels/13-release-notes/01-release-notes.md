# Release Notes

> **Source:** https://docs.shovels.ai/release-notes/release-notes
> **Fetched:** 2026-04-16

This file archives the full release history of the Shovels platform (API + Online + EDL) as published on the Shovels docs site. The most recent release (v2.1.7, 2026-04-02) introduced several breaking changes for API consumers — consult that section before relying on any pre-2026-04-02 assumptions about contractor IDs, `first_seen_date` semantics, or permit/contractor counts.

---

## v2.1.7 — 2026-04-02

**Major changes**

- Transitioned to a fully Shovels-owned data pipeline; all third-party provider data removed.
- Added 11.6M new permits (NY +4.0M, TX +3.5M, FL +1.9M). Total permits now 129.9M.
- Introduced `description_derived` field on 81M permits (62.4% coverage).

**Breaking changes**

- **Contractor IDs regenerated.** 81.8% of pre-2026-04-02 IDs map to new IDs via changelog; 18.2% have no mapping.
- Permit count decreased from 216M → 130M (~98M third-party permits removed).
- Contractor count decreased from 3.9M → 2.5M.
- Jurisdictions with >80% permit loss: VT, RI, MA, CT, DE, WI, NM. DC was dropped entirely.
- `first_seen_date` values reset; all values now fall in the range 2025-05-19 through 2026-03-28.

**Data quality improvements (coverage)**

- Subtype: 75.7% (+18%)
- Final date: 70.5% (+16%)
- Fees: 65.0% (+11%)
- Job value: 62.6% (+10%)
- Issue date: 80.5% (+9%)
- File date: 90.5% (+4%)

**Contractor intelligence**

- License coverage: 63.5% (+20%)
- Phone coverage: 57.7% (+7%)
- Email coverage: 30.2% (+6%)
- Added 3 new state licensing boards: MA plumbing, NC plumbing & electrical, IA plumbing.
- CSL dataset: 3.14M records (+4%).

**Other metrics**

- 352K permits filed in March 2026.
- Geocoding coverage: 72% → 67%.
- Inspection data coverage: 15% → 3%.
- Address-ID coverage: 78% → 74%.
- Employee records: 38.1M → 12.8M.
- Resident records: 45.9M → 27.6M.

---

## v2.1.6 — 2026-03-02

**New features**

- Launched the Shovels CLI — a single-binary command-line tool for querying permits, contractors, and addresses.
- CLI features: JSON stdout output, auto-pagination via `--limit all`, auto-retry with exponential backoff.
- Added result counts to 7 paginated endpoints via `include_count=true`.
- Enhanced usage dashboard with daily breakdown, `is_over_limit` flag, and `available_at` projection.
- Fixed contractor metrics accuracy for `tag=all` queries.

**Permits dataset**

- Added 1.8M new permits.
- Permits filed in February 2026: 156K.
- Year-to-date 2026: 462K.
- Additional 1.4M records geocoded.

**Permit activity by category**

- Electrical +388K; New construction +203K; HVAC +136K; Remodel +136K; Roofing +91K; Plumbing +71K; Solar +23K; Demolition +19K; ADU +12K; EV charger +2.2K.

---

## v2.1.5 — 2026-02-01

**Permits dataset**

- Added 6.1M new permits.
- Permits filed in January 2026: 197K.

**Permit activity by category**

- Electrical +911K; New construction +803K; HVAC +620K; Remodel +549K; Plumbing +447K; Roofing +268K; Solar +234K; Demolition +120K; ADU +100K; EV charger +9K.

**Geocoding**

- Additional 5.2M records geocoded with latitude/longitude.

**Contractor intelligence**

- Added 142K new contractors.
- **Breaking change:** 5M contractor IDs updated (Oregon, Douglas County, and Omaha most affected).

**Charlie AI agent updates**

- Automatic error recovery with backend reconnections.
- Clickable profile links for contractors and permits.
- Fixed county-based query formatting issues.

---

## v2.1.4 — 2026-01-01

**Permits dataset**

- Added 5.5M new permits.
- Permits filed in December 2025: 295K.
- Total geocoded permits: 143.9M.
- Additional 4.7M records geocoded.

**Permit activity by category**

- Electrical +1.3M; Plumbing +803K; HVAC +569K; New construction +460K; Remodel +351K; Roofing +267K; Solar +131K; ADU +82K; Demolition +65K; EV charger +18K.

**Contractor intelligence**

- Added 171K new contractors; total 3.6M.
- New licenses: +256K. New primary phone numbers: +69K. New primary emails: +40K.

**API features**

- Added negative query filters via dash-prefix syntax for exclusions.
- Dynamic tallies with `include_tallies=true` for `tag_tally` and `status_tally`.
- Performance improvements for contractor and text search.
- Added English stemming to full-text search.
- Fixed invalid date-range handling — now returns 422 instead of 500.
- Fixed a contractor-search pagination bug.

---

## v2.1.3 — 2025-12-01

**Permits dataset**

- Added 6.6M historical permits.
- Permits filed in November 2025: 222K.
- Expanded fee information on 14M records.
- Job values added: +10M. Issue dates added: +13M.
- Added `APN` field to 40M permits.

**Coverage**

- 160 new jurisdictions added.

**Contractor intelligence**

- Added 63K new contractors.
- Additional parsed addresses: 50K. Additional phone numbers: 40K. Additional license issue dates: 7K.

---

## v2.1.2 — 2025-11-01

**Permits dataset**

- Enhanced property-type classification on 20M+ permits.
- 4M additional addresses labeled as commercial or residential.
- Permits filed in October 2025: 180K.
- Historical permits added: 3.4M.
- Enhanced FIPS code coverage.

**Contractor intelligence**

- Added 66K new contractors.
- Phone coverage +3.6%. Email coverage +4.5%. License field coverage +10.6%.

**API changes**

- Introduced `contractor_classification_derived` parameter with a standardized taxonomy.
- **Deprecated:** the legacy `contractor_classifications` parameter.

---

## v2.1.1 — 2025-10-01

**Permits dataset**

- Total records: 185M (+10M new permits).
- Permits filed in September 2025: 80K.
- Year-to-date 2026: 4.5M.
- First offline permit acquisition: 500K+ records from Cook County, IL and Oak Ridge North, TX.

**Contractor intelligence**

- Added 190K new contractors.
- New license records: 70K. New phone numbers: 200K+. New email addresses: 100K+.

---

## v2.1.0 — 2025-09-14

**Permits dataset**

- Total records: 174M (+700K from previous month).
- Permits filed in August 2025: 162,281.
- Permits transitioned to finalized status: 560K.
- New address points: 450K with geo-coordinate mapping.
- New jurisdictions: 119.
- Job value entries added: 2.3M+.
- New construction permits: 55,000. HVAC permits: 124,000.

**Contractor intelligence**

- New contractors added: 13,000.
- New license records: 70,000. New phone numbers: 8,000. New email addresses: 30,000.

---

## v2.0.9 — 2025-07-15

**Permits dataset**

- Added 3M+ new permits nationwide; California: +2M.
- Year-to-date 2025 (through July 15): 2.9M permits.
- Permits filed since June 1: 250K+ (22K filed in July).

**Permit activity**

- Construction: 130,000. Solar: 125,000. EV chargers: 10,000.

**Contractor intelligence**

- New primary phone numbers: 35,000+.

**API changes**

- Improved contractor-classification standardization.
- **Warning:** page-based pagination deprecated; token-based pagination fully live. Page-parameter removal scheduled for August 1, 2025.

---

## v2.0.8 — 2025-07-02

**General**

- Minor UX improvements and speed enhancements.

**Bug fixes**

- Fixed geo change on the download-list button.
- Fixed sticky filter persistence.
- Fixed geography-profile filter updates for charts.

**API**

- Final reminder: page-based pagination discontinued August 1, 2025. Migrate to token-based (cursor) pagination.

---

## v2.0.7 — 2025-06-10

**Online**

- Faster pagination for deeper pages.
- Increased jurisdiction coverage.

**API**

- Cursor-based pagination added to all endpoints for improved deep-search pagination.
- **Deprecation:** Old `page` parameter deprecated; supported for 3 additional months.

**EDL**

- Added 1.2M permits (248K from May alone).
- 300 new jurisdictions added.
- Added 70K new contractors (total: 2.96M).
- Enhanced deduplication logic.
- 40K additional contact details linked (phone, email, address).
- **Breaking change:** ~2M duplicate permits removed (Florida and Texas most affected; ~6% of permits received new IDs).
- **Breaking change:** ~170K contractors received regenerated IDs.
- Permit attributes (`permit_number`, address) remained unchanged; contractors remained searchable by areas-of-work, permit projects, and business names.

---

## v2.0.6 — 2025-05-06

**Online**

- Improved permit-search logic to order by newest first.

**API**

- Cursor-based pagination added for all endpoints.
- Response ordering now chronological, descending.
- **Deprecation:** `page` parameter deprecated; supported for 3 additional months.

**EDL**

- New `apn` column added to the `addresses` table.
- New `status` and `status_detailed` columns added to `csl` and `contractors` tables with standardized status schema.
- CSL table expanded to 11 new states: CT, GA, IL, MD, MO, OK, NY, OR, SC, TN, UT.
- Bug fix: address parsing for NV contractors in CSL table resolved.

---

## v2.0.5 — 2025-04-03

**Online**

- Speed improvements.
- New and improved onboarding flow.

**Bug fixes**

- Fixed geo change on download-list button.
- Fixed sticky filter persistence.
- Fixed geography-profile filter updates.

**EDL**

- Total permits: 171M (+2M).
- 8 new jurisdictions added.
- `first_seen_date` coverage: ~150M permits.
- Contractors: 3M+ total. New contractor records: 50K+.
- License linkage: additional 80K contractors linked.
- All licensed contractors now have a `classification_derived` field with standardized categories.
- New CSL table: 1.8M contractors from 26 state files.
- ~200K contractors linked to existing contractors table.
- ~700K new contractor phone numbers.
- ~200K new emails.

---

## v2.0.4 — 2025-03-14

**Online**

- Added website search filter in Contractor Filters.
- Tooltips for better functionality explanation.
- Search-filter auto-caching.
- New user onboarding experience.
- Monthly datepicker adjustment for date-range selection.

**API**

- New fields added to `/contractors/` endpoint: `first_seen_date`, `license_act_date`, `license_inact_date`, `review_count`, `rating`, `dba`, `sic`, `naics`, `linkedin_url`, `revenue`, `employee_count`, `primary_industry`.
- New API rate limits: 1M requests/month (~33K requests/day).

**EDL**

- `first_seen_date` added to `permits` table (distinct from contractor `first_seen_date`).

---

## v2.0.3 — 2025-02-06

**Online**

- Added Address Profiles.
- Added Free Forever plan (replaces Free Trial).

**Bug fixes**

- Fixed Contractor Profiles loading issue.

**API**

- New endpoints: `/v2/{geography}/{geo_id}/metrics/monthly` and `/v2/{geography}/{geo_id}/metrics/current`.
- **Breaking change:** removed `/v2/{geography}/{geo_id}/metrics` endpoint.
- **Breaking change:** monetary data types changed from decimal to integer (dollars → cents) — affects `property_assess_market_value`, `job_value`, `fees`, `avg_job_value`, `total_job_value`.
- **Breaking change:** percentage data types changed from decimal to integer (0.75 → 75) — affects `inspection_pass_rate`, `avg_inspection_pass_rate`.

**Deprecation**

- V1 API deprecated.

---

## v2.0.2 — 2025-01-09

**Online**

- Added `employees` to Contractor Profiles.
- Added links to Jurisdiction Profiles for permits.
- Added links to City and County Profiles.

**Bug fixes**

- Fixed password-reset bug.

**API**

- New `/v2/contractors/{id}/employees` endpoint.
- New `/v2/addresses/{id}/metrics` endpoint.
- Fixed metrics-calculation algorithm.
- **End-of-life notice:** API V1 deprecated by end of January 2025.

**EDL coverage**

- Added 6M permits nationwide.
- Added 9 new permit jurisdictions.

**EDL breaking changes**

- `first_seen_at` renamed to `first_seen_date` (type changed to DATE).
- `reviews` renamed to `review_count`.
- `residents` table foreign key changed from `permit_id` to `address_id`.

---

## v2.0.1 — 2024-12-04

**Online**

- Added 2M permits in Texas.
- Added metric visualizations to Contractor Profiles.

**Bug fixes**

- Fixed Contractor Profiles loading issue.

**API**

- New `residents` endpoint.
- Improved address validation for geography-related fields.
- **Breaking change:** `property_type` values now lowercase (e.g., `"residential"`).

**EDL**

- New `first_seen_at` column on the `contractor` table.
- New `employees` table with extensive firmographic data linked to contractors.
- Additional columns on the `residents` table: validation statuses, business emails, LinkedIn URLs, demographic data, marital/children status, income/net-worth ranges, job details, work history, education, social connections, and company information.
- **Breaking changes — casing standardizations:** `property_owner_type` now snake_case; `owner_name`, `owner_street`, `owner_city`, `applicant_name`, `applicant_street`, `applicant_city` now uppercase.
- **Planned change:** `permits_ids` to be replaced with `address_id` in `residents` table (effective January 2025).
