# NAICS Codes — Canonical Reference

> **Produced:** 2026-04-15
> **Purpose:** Reference for building a NAICS code ingestion pipeline into Postgres
> **Revision:** 2022 NAICS (current; next revision expected ~2027)

---

## 1. What Is a NAICS Code?

The **North American Industry Classification System (NAICS)** is the standard used by the U.S., Canada, and Mexico to classify business establishments by type of economic activity. Every business in federal datasets (USASpending, SAM.gov, SBA, Census, etc.) is tagged with one or more NAICS codes.

NAICS replaced the older **SIC (Standard Industrial Classification)** system in 1997. The current version is **2022 NAICS**, effective for data collected from January 1, 2022 onward.

---

## 2. Hierarchy Structure

NAICS is a 6-level hierarchy encoded in the code itself. You derive parent levels by truncating digits:

| Level | Digits | Name | Example | Count (2022) |
|-------|--------|------|---------|--------------|
| 1 | 2 | **Sector** | `11` = Agriculture, Forestry, Fishing and Hunting | 20 sectors* |
| 2 | 3 | **Subsector** | `111` = Crop Production | 96 |
| 3 | 4 | **Industry Group** | `1111` = Oilseed and Grain Farming | 308 |
| 4 | 5 | **NAICS Industry** | `11111` = Soybean Farming | 692 |
| 5 | 6 | **National Industry** | `111110` = Soybean Farming | 1,012 |

*\*20 sectors includes 3 ranges: `31-33` (Manufacturing), `44-45` (Retail Trade), `48-49` (Transportation & Warehousing). These use range codes, not single 2-digit codes.*

**Total codes in the 2022 NAICS structure: 2,125** (across all hierarchy levels).

The hierarchy is **implicit in the code**: the first 2 digits of any NAICS code identify its sector, the first 3 identify its subsector, etc. No separate parent-child linking table is needed — you derive it from the code.

**The 20 NAICS Sectors:**

| Code | Sector |
|------|--------|
| 11 | Agriculture, Forestry, Fishing and Hunting |
| 21 | Mining, Quarrying, and Oil and Gas Extraction |
| 22 | Utilities |
| 23 | Construction |
| 31-33 | Manufacturing |
| 42 | Wholesale Trade |
| 44-45 | Retail Trade |
| 48-49 | Transportation and Warehousing |
| 51 | Information |
| 52 | Finance and Insurance |
| 53 | Real Estate and Rental and Leasing |
| 54 | Professional, Scientific and Technical Services |
| 55 | Management of Companies and Enterprises |
| 56 | Administrative and Support and Waste Management and Remediation Services |
| 61 | Educational Services |
| 62 | Health Care and Social Assistance |
| 71 | Arts, Entertainment and Recreation |
| 72 | Accommodation and Food Services |
| 81 | Other Services (except Public Administration) |
| 92 | Public Administration |

---

## 3. Sources Investigated

### 3a. Census Bureau — 2022 NAICS Structure (XLSX) ⭐ RECOMMENDED

- **URL:** `https://www.census.gov/naics/2022NAICS/2022_NAICS_Structure.xlsx`
- **Format:** XLSX, single sheet ("2022 NAICS Structure")
- **Size:** 88 KB, 2,147 rows (including 2 header/metadata rows)
- **Saved as:** `naics/2022_NAICS_Structure.xlsx`

**Column structure:**

| Column | Content |
|--------|---------|
| A | Change Indicator (*, **, ***, **** — see below) |
| B | 2022 NAICS Code (integer, 2-6 digits) |
| C | 2022 NAICS Title |

**Change indicators:**
- `*` = title change, no content change
- `**` = new code for 2022
- `***` = re-used code, content change
- `****` = re-used code, content change at lower level

**Row 1** is the sheet title. **Row 2** is the change indicator legend. **Row 3** is the column headers. **Data starts at row 4.**

**Sample records:**

```
Row 4:  [None, 11, "Agriculture, Forestry, Fishing and HuntingT"]
Row 5:  [None, 111, "Crop ProductionT"]
Row 6:  [None, 1111, "Oilseed and Grain FarmingT"]
Row 7:  [None, 11111, "Soybean FarmingT"]
Row 8:  [None, 111110, "Soybean Farming"]
```

**Notes:**
- Titles at non-leaf levels (2-5 digits) have a `T` suffix indicating trilateral (US/CA/MX) agreement. Strip the `T` during ingestion.
- Some titles have trailing spaces — trim during ingestion.
- Code column is numeric (integer), not text. Leading zeros are not an issue for NAICS (no codes start with 0).

**Code counts (verified):**

| Level | Count |
|-------|-------|
| 2-digit sectors | 17 (range sectors 31-33, 44-45, 48-49 are stored as single entries) |
| 3-digit subsectors | 96 |
| 4-digit industry groups | 308 |
| 5-digit industries | 692 |
| 6-digit national industries | 1,012 |
| **Total** | **2,125** |

### 3b. Census Bureau — 6-Digit Codes Only (XLSX)

- **URL:** `https://www.census.gov/naics/2022NAICS/6-digit_2022_Codes.xlsx`
- **Format:** XLSX, single sheet ("2022_6-digit_industries")
- **Size:** 44 KB, 1,014 rows
- **Saved as:** `naics/6-digit_2022_Codes.xlsx`

**Columns:** `2022 NAICS Code` (integer), `2022 NAICS Title` (text)

Contains exactly the 1,012 six-digit (leaf) codes. Useful if you only need leaf-level codes, but **the full structure file is better** because it includes the hierarchy.

### 3c. SBA NAICS API (JSON)

- **URL:** `https://api.sba.gov/naics/naics.json`
- **Format:** JSON array, no auth required
- **Size:** 538 KB, 997 records
- **Saved as:** `naics/sba_naics.json`

**Record shape:**

```json
{
  "id": "111110",
  "description": "Soybean Farming",
  "sectorId": "11",
  "sectorDescription": "Agriculture, Forestry, Fishing and Hunting",
  "subsectorId": "111",
  "subsectorDescription": "Crop Production",
  "revenueLimit": 2.25,
  "assetLimit": null,
  "employeeCountLimit": null,
  "parent": null,
  "footnote": null
}
```

**Key characteristics:**
- **Only 6-digit codes** (996 valid records + 1 placeholder for sector 92 Public Administration with empty id). Missing 16 codes compared to Census (997 vs 1,012).
- **SBA-specific fields:** `revenueLimit` (in $ millions), `employeeCountLimit` — these are SBA small business size standards, not part of the NAICS classification itself.
- **Parent/exception records:** 14 records have a `parent` field and use IDs like `115310_a_Except`. These represent SBA sub-industry size exceptions (e.g., "Forest Fire Suppression" as a sub-exception of NAICS 115310).
- **259 records** have footnotes explaining SBA size standard exceptions.
- **87 unique subsectors** (vs 96 in Census) — does not cover all subsectors.

**Verdict:** Good as a **supplementary** source for SBA size standards. **Not suitable as the primary NAICS reference** because it only covers 6-digit codes, is missing ~16 codes vs Census, and includes SBA-specific exception records that are not part of the standard NAICS hierarchy.

### 3d. BenDoyle GitHub CSV

- **URL:** `https://github.com/BenDoyle/NAICS` → `naics.csv`
- **Format:** CSV with columns: `level`, `code`, `name`, `notes`
- **Size:** 2,075 records
- **Saved as:** `naics/naics_bendoyle.csv`

**Sample:**

```csv
level,code,name,notes
2,11,"Agriculture, Forestry, Fishing and Hunting",""
3,111,Crop Production,""
4,1111,Oilseed and Grain Farming,""
5,11111,Soybean Farming,""
6,111110,Soybean Farming,""
```

**Level distribution:** 14 sectors (level 2), 102 subsectors (level 3), 324 industry groups (level 4), 713 industries (level 5), 922 national industries (level 6). Total: 2,075.

**Verdict:** This is based on the **2007 NAICS** (from Statistics Canada), **not 2022**. Code counts don't match current revision. **Do not use as primary source** — it's 15+ years out of date.

---

## 4. Recommended Primary Source

### Use: **Census Bureau 2022 NAICS Structure XLSX** (`2022_NAICS_Structure.xlsx`)

**Why:**

1. **Authoritative** — the Census Bureau is the official source for NAICS codes in the US.
2. **Complete hierarchy** — contains all 2,125 codes across all 5 levels (sectors through national industries), not just 6-digit leaf codes.
3. **Machine-readable** — single-sheet XLSX with simple 3-column structure. Easy to parse with openpyxl or pandas.
4. **Current** — 2022 revision, which is the active standard.
5. **No auth required** — direct download, no API key needed.

**Ingestion notes for the follow-up agent:**

- Skip rows 1-3 (metadata/headers). Data starts at row 4.
- Column B = code (integer), Column C = title (text). Column A = change indicator (optional, store if you want to track revision changes).
- Strip trailing `T` from titles (trilateral agreement marker).
- Trim whitespace from titles.
- Derive the hierarchy from the code length: `len(str(code))` gives you the level. Parent code = truncate to `n-1` digits.
- Special handling for range sectors: `31-33`, `44-45`, `48-49`. The XLSX stores these as single entries. Build a lookup map: codes starting with `31`, `32`, `33` → sector `31-33`, etc.

---

## 5. Recommended Postgres Schema

```sql
CREATE TABLE lookup.naics_codes (
    naics_code       TEXT PRIMARY KEY,       -- e.g., '111110'
    title            TEXT NOT NULL,           -- e.g., 'Soybean Farming'
    level            SMALLINT NOT NULL,       -- 2=sector, 3=subsector, 4=industry_group, 5=industry, 6=national_industry
    sector_code      TEXT,                    -- first 2 digits (or range like '31-33')
    subsector_code   TEXT,                    -- first 3 digits
    industry_group_code TEXT,                 -- first 4 digits
    industry_code    TEXT,                    -- first 5 digits
    change_indicator TEXT,                    -- *, **, ***, ****
    naics_year       SMALLINT DEFAULT 2022,   -- revision year
    created_at       TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for common lookups
CREATE INDEX idx_naics_sector ON lookup.naics_codes (sector_code);
CREATE INDEX idx_naics_level ON lookup.naics_codes (level);
```

---

## 6. Crosswalk Availability (NAICS ↔ SIC)

For future reference — not part of this ingestion:

- **Census Bureau:** Official NAICS-to-SIC and SIC-to-NAICS concordance tables at `https://www.census.gov/naics/concordances/`
- **naics.com:** Searchable NAICS/SIC crosswalk
- **data.world:** Community-maintained NAICS datasets with SIC mappings

---

## 7. Update Cadence

NAICS is revised every **5 years** by the U.S. Census Bureau, in coordination with Statistics Canada and Mexico's INEGI:

- 1997 (original)
- 2002
- 2007
- 2012
- 2017
- **2022** (current)
- ~2027 (expected next revision)

Between revisions, the code set is frozen. The 2022 revision added, removed, and reclassified approximately 160 codes vs 2017.

---

## 8. Source Files Saved

| File | Description |
|------|-------------|
| `naics/2022_NAICS_Structure.xlsx` | Census Bureau full hierarchy (recommended primary source) |
| `naics/6-digit_2022_Codes.xlsx` | Census Bureau 6-digit codes only |
| `naics/sba_naics.json` | SBA API response with size standards |
| `naics/naics_bendoyle.csv` | BenDoyle GitHub CSV (2007, outdated — reference only) |
