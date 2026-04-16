# O\*NET Database — Canonical Reference

> **Last updated:** 2026-04-16
> **Current version:** O\*NET 30.2 (February 2026 release)
> **Maintained by:** National Center for O\*NET Development, funded by U.S. DOL
> **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## What Is O\*NET?

The **Occupational Information Network (O\*NET)** is the richest publicly available database of occupational information in the U.S. It builds on SOC codes by adding structured data about skills, tasks, education requirements, tools/technology, alternate job titles, and more for ~1,016 occupations covering the entire U.S. economy.

For staffing intelligence, O\*NET is critical because it provides:
- **Alternate job titles** — maps messy real-world titles to standardized codes
- **Skills per occupation** — what skills does a Machinist need?
- **Tasks per occupation** — what does a CNC Operator actually do?
- **Education/experience requirements** — what qualifications to look for
- **Tools and technology** — what software/tools each role uses

---

## O\*NET-SOC Code Format

O\*NET extends the 6-digit SOC code with a 2-digit suffix:

```
SOC:      XX-XXXX       (e.g., 11-1011)
O*NET:    XX-XXXX.XX    (e.g., 11-1011.00 or 11-1011.03)
```

| Suffix | Meaning |
|--------|---------|
| `.00` | Maps 1:1 to the SOC detailed occupation (no subdivision) |
| `.01`, `.02`, `.03`, etc. | O\*NET-specific subdivision of the SOC code |

**Example:**
- SOC `11-1011` "Chief Executives" → O\*NET has two entries:
  - `11-1011.00` Chief Executives
  - `11-1011.03` Chief Sustainability Officers

**Total occupations in O\*NET 30.2:** 1,016 (of which 923 have full survey data; 93 are title-only — military-specific and "All Other" residuals)

---

## Data Sources and Download

### Bulk Download (Recommended for Ingestion)

**URL:** `https://www.onetcenter.org/database.html`

Available in 5 formats:

| Format | URL |
|--------|-----|
| **Text (TSV)** | `https://www.onetcenter.org/dl_files/database/db_30_2_text.zip` |
| Excel | `https://www.onetcenter.org/dl_files/database/db_30_2_excel.zip` |
| MySQL | `https://www.onetcenter.org/dl_files/database/db_30_2_mysql.zip` |
| SQL Server | `https://www.onetcenter.org/dl_files/database/db_30_2_mssql.zip` |
| Oracle | `https://www.onetcenter.org/dl_files/database/db_30_2_oracle.zip` |

**Recommendation:** Use the **Text (TSV)** format. Files are tab-delimited, UTF-8, easily parseable. The zip is ~13MB, extracts to ~95MB across 41 files.

### Web Services API

**URL:** `https://services.onetcenter.org/`

- **Auth:** API key required (register at `/developer/signup`), sent via `X-API-Key` header
- **Format:** JSON responses, REST/GET only
- **Rate limits:** Best-effort; 429 responses with 200ms retry recommendation
- **Current data:** O\*NET 30.2
- **Endpoints:** Occupation search, crosswalks (SOC, DOT, RAPIDS, ESCO), detailed data access, taxonomy services
- **Pagination:** `start`, `end`, `total` fields, max 2000 per page

**Key API endpoints:**
- `GET /database/` — List all data tables
- `GET /database/info/{table}` — Table column information
- `GET /database/rows/{table}` — Data rows with filter/sort (programmatic access to ALL 40 files)
- `GET /online/search?keyword=machinist` — Occupation search
- `GET /online/occupations/{code}/summary/skills` — Skills for an occupation

**Data dictionary:** `https://www.onetcenter.org/dictionary/30.2/text/`

**Recommendation for initial load:** Use bulk download, not API. API is better for real-time lookups, staying current between releases, and search.

---

## Complete File Inventory (O\*NET 30.2)

### Key Tables for Staffing Intelligence

These are the files most relevant for a staffing intelligence product:

| File | Rows | Join Key | What It Contains |
|------|------|----------|-----------------|
| **Occupation Data.txt** | 1,016 | `O*NET-SOC Code` | Master occupation list: code, title, description |
| **Alternate Titles.txt** | 57,543 | `O*NET-SOC Code` | ~57K alternate/lay job titles mapped to occupations |
| **Sample of Reported Titles.txt** | 7,953 | `O*NET-SOC Code` | Real job titles reported by workers in surveys |
| **Skills.txt** | 62,580 | `O*NET-SOC Code` | 35 skills rated per occupation (importance + level) |
| **Knowledge.txt** | 59,004 | `O*NET-SOC Code` | 33 knowledge areas rated per occupation |
| **Task Statements.txt** | 18,796 | `O*NET-SOC Code` | Specific tasks performed in each occupation |
| **Education, Training, and Experience.txt** | 37,125 | `O*NET-SOC Code` | Education level, experience, training requirements |
| **Job Zones.txt** | 923 | `O*NET-SOC Code` | 5-level preparation scale (1=minimal → 5=extensive) |
| **Technology Skills.txt** | 32,773 | `O*NET-SOC Code` | Software/technology used per occupation |
| **Tools Used.txt** | 41,662 | `O*NET-SOC Code` | Physical tools used per occupation (legacy — no longer updated) |
| **Related Occupations.txt** | 18,460 | `O*NET-SOC Code` | Related occupations with relatedness tier |

### All Files (41 total)

| File | Rows | Description |
|------|------|-------------|
| **Abilities.txt** | 92,976 | 52 abilities rated per occupation (IM=importance, LV=level) |
| **Abilities to Work Activities.txt** | 381 | Crosswalk: abilities → work activities |
| **Abilities to Work Context.txt** | 139 | Crosswalk: abilities → work context |
| **Alternate Titles.txt** | 57,543 | Alternate job titles per occupation |
| **Basic Interests to RIASEC.txt** | 53 | Maps basic interests to Holland RIASEC types |
| **Content Model Reference.txt** | 630 | Taxonomy of all O\*NET content model elements |
| **DWA Reference.txt** | 2,087 | Detailed Work Activity reference list |
| **Education, Training, and Experience Categories.txt** | 41 | Category definitions for education/training scales |
| **Education, Training, and Experience.txt** | 37,125 | Education/training/experience data per occupation |
| **Emerging Tasks.txt** | 328 | New/revised tasks identified in recent surveys |
| **Interests.txt** | 8,307 | Holland RIASEC interest profiles per occupation |
| **Interests Illustrative Activities.txt** | 188 | Example activities for each interest type |
| **Interests Illustrative Occupations.txt** | 186 | Example occupations for each interest type |
| **IWA Reference.txt** | 332 | Intermediate Work Activity reference list |
| **Job Zone Reference.txt** | 4 | Definitions for 4 job zone levels |
| **Job Zones.txt** | 923 | Job zone assignment per occupation |
| **Knowledge.txt** | 59,004 | 33 knowledge areas rated per occupation |
| **Level Scale Anchors.txt** | 483 | Anchor descriptions for level scales |
| **Occupation Data.txt** | 1,016 | Master occupation list (code, title, description) |
| **Occupation Level Metadata.txt** | 32,202 | Survey metadata per occupation |
| **Read Me.txt** | 16 | Version and license info |
| **Related Occupations.txt** | 18,460 | Related occupations with relatedness tier |
| **RIASEC Keywords.txt** | 75 | Keywords for Holland RIASEC interest types |
| **Sample of Reported Titles.txt** | 7,953 | Real job titles reported by survey incumbents |
| **Scales Reference.txt** | 31 | Scale definitions (IM, LV, etc.) |
| **Skills.txt** | 62,580 | 35 skills rated per occupation |
| **Skills to Work Activities.txt** | 232 | Crosswalk: skills → work activities |
| **Skills to Work Context.txt** | 96 | Crosswalk: skills → work context |
| **Survey Booklet Locations.txt** | 211 | Survey instrument reference |
| **Task Categories.txt** | 7 | Task frequency scale definitions |
| **Task Ratings.txt** | 161,559 | Task importance/frequency ratings |
| **Task Statements.txt** | 18,796 | Specific tasks per occupation |
| **Tasks to DWAs.txt** | 23,850 | Maps tasks to Detailed Work Activities |
| **Technology Skills.txt** | 32,773 | Software/technology per occupation |
| **Tools Used.txt** | 41,662 | Physical tools per occupation |
| **UNSPSC Reference.txt** | 4,264 | UN product classification reference |
| **Work Activities.txt** | 73,308 | 41 generalized work activities per occupation |
| **Work Context.txt** | 297,676 | 57 work context elements per occupation |
| **Work Context Categories.txt** | 281 | Work context category definitions |
| **Work Styles.txt** | 37,422 | 16 work style traits per occupation |
| **Work Values.txt** | 7,866 | 6 work value dimensions per occupation (legacy — no longer updated) |

---

## Key File Schemas

### Occupation Data.txt (Master List)

The core file. Every other file joins to this via `O*NET-SOC Code`.

| Column | Type | Description |
|--------|------|-------------|
| `O*NET-SOC Code` | string | 10-char code: `XX-XXXX.XX` |
| `Title` | string | Official occupation title |
| `Description` | string | Full occupation description |

**Sample:**
```
O*NET-SOC Code	Title	Description
11-1011.00	Chief Executives	Determine and formulate policies and provide overall direction of companies...
51-4041.00	Machinists	Set up and operate a variety of machine tools to produce precision parts...
```

### Alternate Titles.txt (Critical for Title Matching)

Maps ~57K real-world job titles to standardized O\*NET codes. This is the key file for matching messy job titles from resumes, job postings, or contracts to standardized occupations.

| Column | Type | Description |
|--------|------|-------------|
| `O*NET-SOC Code` | string | O\*NET-SOC code |
| `Alternate Title` | string | Alternate/lay job title |
| `Short Title` | string | Abbreviated title (often `n/a`) |
| `Source(s)` | string | Data source codes |

**Sample:**
```
O*NET-SOC Code	Alternate Title	Short Title	Source(s)
51-4041.00	CNC Machinist	n/a	08
51-4041.00	Manual Machinist	n/a	08
51-4041.00	Job Shop Machinist	n/a	10
```

### Skills.txt

| Column | Type | Description |
|--------|------|-------------|
| `O*NET-SOC Code` | string | O\*NET-SOC code |
| `Element ID` | string | Skill taxonomy ID (e.g., `2.A.1.a`) |
| `Element Name` | string | Skill name (e.g., `Reading Comprehension`) |
| `Scale ID` | string | `IM` = Importance, `LV` = Level |
| `Data Value` | float | Rating value |
| `N` | integer | Sample size |
| `Standard Error` | float | SE of the estimate |
| `Lower CI Bound` | float | Lower 95% CI |
| `Upper CI Bound` | float | Upper 95% CI |
| `Recommend Suppress` | string | `Y`/`N` — suppress if unreliable |
| `Not Relevant` | string | `Y`/`N`/`n/a` |
| `Date` | string | Survey date (MM/YYYY) |
| `Domain Source` | string | Data source (Analyst, Incumbent, etc.) |

**Scale values:** Importance (IM) ranges 1-5. Level (LV) ranges 0-7.

### Task Statements.txt

| Column | Type | Description |
|--------|------|-------------|
| `O*NET-SOC Code` | string | O\*NET-SOC code |
| `Task ID` | integer | Unique task identifier |
| `Task` | string | Task description text |
| `Task Type` | string | `Core` or `Supplemental` |
| `Incumbents Responding` | integer | Number of workers surveyed |
| `Date` | string | Survey date |
| `Domain Source` | string | Data source |

### Education, Training, and Experience.txt

| Column | Type | Description |
|--------|------|-------------|
| `O*NET-SOC Code` | string | O\*NET-SOC code |
| `Element ID` | string | `2.D.1` (education), etc. |
| `Element Name` | string | E.g., `Required Level of Education` |
| `Scale ID` | string | `RL` = Required Level |
| `Category` | integer | Education category (1-12) |
| `Data Value` | float | Percentage of workers at this level |
| `N` | integer | Sample size |
| ... | | Standard error, CI bounds, etc. |

**Education categories (from Categories file):**
1. Less than High School
2. High School Diploma/GED
3. Post-Secondary Certificate
4. Some College
5. Associate's Degree
6. Bachelor's Degree
7. Post-Baccalaureate Certificate
8. Master's Degree
9. Post-Master's Certificate
10. First Professional Degree
11. Doctoral Degree
12. Post-Doctoral Training

### Job Zones.txt

A simpler preparation-level indicator than the full education table.

| Column | Type | Description |
|--------|------|-------------|
| `O*NET-SOC Code` | string | O\*NET-SOC code |
| `Job Zone` | integer | 2-5 (preparation level) |
| `Date` | string | Survey date |
| `Domain Source` | string | Data source |

**Job Zone levels (v30.2 has 4 zones):**
- 2 = Very Little to Some Preparation
- 3 = Medium Preparation
- 4 = Considerable Preparation
- 5 = Extensive Preparation

### Technology Skills.txt (New in v30+)

Replaces the old `Tools and Technology.txt` file (which combined both). Now split into separate files.

| Column | Type | Description |
|--------|------|-------------|
| `O*NET-SOC Code` | string | O\*NET-SOC code |
| `Example` | string | Software/technology name |
| `Commodity Code` | string | UNSPSC product code |
| `Commodity Title` | string | UNSPSC product category |
| `Hot Technology` | string | `Y`/`N` — widely used in the field |
| `In Demand` | string | `Y`/`N` — growing demand |

---

## Update Cadence

O\*NET is updated **quarterly** with rolling updates:
- New occupations and data updates ~4 times/year
- Full database version bumps (e.g., 30.1 → 30.2)
- Recent releases: 30.2 (Feb 2026), 30.1 (Dec 2025), 30.0 (Aug 2025), 29.3 (May 2025)

---

## Licensing

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

- Free for commercial use (explicitly confirmed)
- Must give attribution
- Full terms: `https://www.onetcenter.org/license_db.html`

**Required attribution (verbatim use):**
> This product includes information from the O\*NET 30.2 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O\*NET is a trademark of USDOL/ETA.

**Required attribution (modified use):**
> This product includes information from the O\*NET 30.2 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O\*NET is a trademark of USDOL/ETA. [Company] has modified all or some of this information. USDOL/ETA has not approved, endorsed, or tested these modifications.

---

## Source Files in This Directory

| File/Dir | Description |
|----------|-------------|
| `db_30_2_text.zip` | Full O\*NET 30.2 database download (TSV format, ~13MB) |
| `db_30_2_text/` | Extracted database — 41 TSV files (~95MB total) |
| `2019_to_SOC_Crosswalk.csv` | O\*NET-SOC 2019 → 2018 SOC crosswalk (1,016 rows) |
| `2019_Occupations.csv` | O\*NET-SOC codes with titles AND full descriptions (1,016 rows) |
| `SOC_Structure.csv` | Full SOC hierarchy in sparse-matrix format from O\*NET (1,596 rows) |

---

## Ingestion Recommendations

### Priority Files for Staffing Intelligence

**Tier 1 — Must ingest:**
1. `Occupation Data.txt` — Master list of 1,016 occupations with descriptions
2. `Alternate Titles.txt` — 57K alternate job titles (for fuzzy matching)
3. `Skills.txt` — Skills per occupation
4. `Task Statements.txt` — Tasks per occupation
5. `Education, Training, and Experience.txt` — Education requirements
6. `Job Zones.txt` — Preparation level (simpler than full education data)
7. `Technology Skills.txt` — Software/tech per occupation

**Tier 2 — High value:**
8. `Knowledge.txt` — Knowledge domains per occupation
9. `Sample of Reported Titles.txt` — Additional real-world titles
10. `Related Occupations.txt` — Occupation similarity graph
11. `Tools Used.txt` — Physical tools per occupation

**Tier 3 — Nice to have:**
12. `Abilities.txt` — Cognitive/physical abilities per occupation
13. `Work Activities.txt` — Generalized work activities
14. `Interests.txt` — Holland RIASEC profiles
15. `Work Styles.txt` — Personality/work style traits

### Join Strategy

All occupation-level files join on `O*NET-SOC Code` (VARCHAR(10), format `XX-XXXX.XX`).

To join O\*NET data to SOC codes: strip the `.XX` suffix (first 7 characters = SOC code with dash).

To join O\*NET occupations to NAICS industries: use the SOC-NAICS crosswalk (see `SOC_NAICS_CROSSWALK_REFERENCE.md`).

---

## Gotchas and Quirks

1. **Files are TSV, not CSV.** Tab-delimited, despite the .txt extension. Make sure your parser uses tab as delimiter.
2. **Scale ID matters.** Skills, abilities, and knowledge files have TWO rows per element per occupation: one for `IM` (Importance, 1-5) and one for `LV` (Level, 0-7). Don't accidentally double-count.
3. **`Recommend Suppress` = `Y`** means the data is unreliable and should be filtered out.
4. **O\*NET-SOC codes are 10 characters.** Format: `XX-XXXX.XX` — store as VARCHAR(10).
5. **Alternate Titles is the crown jewel** for title matching. But it's not exhaustive — the `Sample of Reported Titles.txt` has additional titles reported by actual workers.
6. **v30.2 split `Tools and Technology.txt`** into two separate files: `Technology Skills.txt` and `Tools Used.txt`. Older documentation may reference the combined file.
7. **No salary/wage data in O\*NET.** For wage data, use BLS OES/OEWS data (separate dataset, also keyed by SOC code).
8. **Job Zones changed in v30.x** — reduced from 5 zones to 4 zones (zones 1 and 2 were merged).
