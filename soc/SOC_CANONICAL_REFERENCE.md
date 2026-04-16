# SOC (Standard Occupational Classification) — Canonical Reference

> **Last updated:** 2026-04-16
> **Current version:** 2018 SOC (next revision: 2028 SOC, expected spring 2027)
> **Maintained by:** U.S. Bureau of Labor Statistics (BLS) with OMB oversight

---

## What Is SOC?

The **Standard Occupational Classification (SOC)** system is used by all federal statistical agencies to classify workers into occupational categories. It is the job-level equivalent of NAICS (which classifies industries). Every occupation in the U.S. economy maps to exactly one SOC detailed occupation code.

SOC is the foundation that O\*NET builds upon — O\*NET extends SOC codes with a 2-digit suffix to create more granular occupation breakdowns.

---

## Hierarchy

SOC uses a 4-level hierarchy. The code format is **XX-XXXX** (with a dash after the first two digits):

| Level | Digits Used | Format | Count (2018) | Example |
|-------|-------------|--------|--------------|---------|
| **Major Group** | First 2 | `XX-0000` | 23 | `51-0000` Production Occupations |
| **Minor Group** | First 3 | `XX-X000` | 98 | `51-4000` Metal Workers and Plastic Workers |
| **Broad Occupation** | First 5 | `XX-XXX0` | 459 | `51-4040` Machinists |
| **Detailed Occupation** | All 6 | `XX-XXXX` | 867 | `51-4041` Machinists |

**Total codes across all levels: 1,447**

### Hierarchy Rules

- Parent-child relationships are **implicit in the code structure** — the first N digits of a child code always match its parent
- The 6th digit distinguishes detailed occupations within a broad occupation
- When a broad occupation is not subdivided, the detailed occupation has the same title and the 6th digit is `1` (e.g., broad `51-4040` Machinists → detailed `51-4041` Machinists)
- Residual/"All Other" codes end in `9` (e.g., `51-4099` Metal Workers and Plastic Workers, All Other)

### Major Groups (23 total)

| Code | Major Group |
|------|-------------|
| 11 | Management |
| 13 | Business and Financial Operations |
| 15 | Computer and Mathematical |
| 17 | Architecture and Engineering |
| 19 | Life, Physical, and Social Science |
| 21 | Community and Social Service |
| 23 | Legal |
| 25 | Educational Instruction and Library |
| 27 | Arts, Design, Entertainment, Sports, and Media |
| 29 | Healthcare Practitioners and Technical |
| 31 | Healthcare Support |
| 33 | Protective Service |
| 35 | Food Preparation and Serving Related |
| 37 | Building and Grounds Cleaning and Maintenance |
| 39 | Personal Care and Service |
| 41 | Sales and Related |
| 43 | Office and Administrative Support |
| 45 | Farming, Fishing, and Forestry |
| 47 | Construction and Extraction |
| 49 | Installation, Maintenance, and Repair |
| 51 | Production |
| 53 | Transportation and Material Moving |
| 55 | Military Specific |

---

## Code Format and Storage

- **Display format:** `XX-XXXX` (with dash) — e.g., `51-4041`
- **Storage recommendation:** Store WITH the dash. It's part of the official code. If you need a numeric index, strip the dash to get a 6-digit integer, but always display with dash.
- **Text column type:** `VARCHAR(7)` or `CHAR(7)` — 2 digits + dash + 4 digits
- **The dash is at position 3** (0-indexed position 2)

---

## Best Source for Ingestion

### Primary: `danielruss/codingsystems` GitHub Repository

**URL:** `https://github.com/danielruss/codingsystems`

This is the best machine-readable source. Clean CSVs, no auth required, no bot blocking.

**Key file: `soc2018_all.csv`**
- **Download URL:** `https://raw.githubusercontent.com/danielruss/codingsystems/master/soc2018_all.csv`
- **Rows:** 1,447 (+ header)
- **Format:** CSV, UTF-8

**Columns:**

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `code` | string | SOC code with dash | `51-4041` |
| `title` | string | Official occupation title | `Machinists` |
| `Level` | integer | Hierarchy level (2, 3, 5, 6) | `6` |
| `Hierarchical_structure` | string | Level name | `Detailed` |
| `parent` | string | Parent SOC code (or `NA` for major groups) | `51-4040` |
| `soc2d` | string | Major group code | `51-0000` |
| `soc3d` | string | Minor group code (or `NA`) | `51-4000` |
| `soc5d` | string | Broad occupation code (or `NA`) | `51-4040` |
| `soc6d` | string | Detailed occupation code (or `NA`) | `51-4041` |

**Sample records:**

```csv
code,title,Level,Hierarchical_structure,parent,soc2d,soc3d,soc5d,soc6d
51-0000,Production Occupations,2,Major,NA,51-0000,NA,NA,NA
51-4000,"Metal Workers and Plastic Workers",3,Minor,51-0000,51-0000,51-4000,NA,NA
51-4040,Machinists,5,Broad,51-4000,51-0000,51-4000,51-4040,NA
51-4041,Machinists,6,Detailed,51-4040,51-0000,51-4000,51-4040,51-4041
```

**Also available:**
- `soc2018_6digit.csv` — Just detailed (6-digit) codes: 867 rows, 2 columns (`soc2018_code`, `soc2018_title`)
- `soc2010_soc2018.csv` — 2010↔2018 crosswalk: 900 rows

### Secondary: BLS Official Downloads

**URL:** `https://www.bls.gov/soc/2018/`

BLS provides the authoritative source files, but they are in XLSX/PDF format and **BLS blocks all automated downloads** (returns 403 for curl, wget, Python requests, and WebFetch). Files must be manually downloaded via browser.

**Available files (all blocked for automated download):**
- `soc_structure_2018.xlsx` — Full hierarchy structure
- `soc_2018_definitions.xlsx` — Occupation definitions
- `soc_2018_direct_match_title_file.xlsx` — Maps ~32,000 job titles to SOC codes (critical for title matching)
- `soc_2018_manual.pdf` — Complete manual with definitions
- `soc_2010_to_2018_crosswalk.xlsx` — Version crosswalk

**Ingestion recommendation:** Use the GitHub CSV as the primary ingestion source. If the BLS Direct Match Title File is needed (for mapping messy job titles to SOC codes), it must be downloaded manually via browser and placed in this directory.

### Tertiary: O\*NET Taxonomy

**URL:** `https://www.onetcenter.org/taxonomy/2019/soc.html`

O\*NET provides an O\*NET-SOC → SOC crosswalk in both XLSX and CSV formats. This is useful for mapping O\*NET's extended codes back to standard SOC.

**Downloaded file:** `2019_to_SOC_Crosswalk.csv` (in `onet/` directory)
- 1,016 rows mapping O\*NET-SOC 2019 codes to 2018 SOC codes

---

## Update Cadence

- SOC is revised approximately every **10 years**
- **Current:** 2018 SOC (released 2017, implemented starting 2018)
- **Previous:** 2010 SOC, 2000 SOC
- **Next:** 2028 SOC — OMB published Federal Register notice in June 2024 requesting comments; final structure expected spring 2027, implementation beginning reference year 2028
- O\*NET updates its taxonomy more frequently to add/refine occupations within the SOC framework

---

## Relationship to O\*NET

O\*NET uses an extended version of SOC called **O\*NET-SOC**:

| System | Format | Example | Occupations |
|--------|--------|---------|-------------|
| SOC 2018 | `XX-XXXX` (6 digits) | `11-1011` Chief Executives | 867 |
| O\*NET-SOC 2019 | `XX-XXXX.XX` (8 digits) | `11-1011.00` Chief Executives | 1,016 |
| | | `11-1011.03` Chief Sustainability Officers | |

- When O\*NET does NOT subdivide a SOC code, it uses `.00` suffix
- When O\*NET DOES subdivide, it uses `.01`, `.02`, `.03`, etc.
- The first 6 digits (before the dot) always correspond to a valid SOC detailed occupation

---

## Source Files in This Directory

| File | Source | Description | Rows |
|------|--------|-------------|------|
| `soc2018_all.csv` | GitHub/danielruss | Complete SOC 2018 hierarchy (all levels) | 1,447 |
| `soc2018_6digit.csv` | GitHub/danielruss | Detailed (6-digit) codes only | 867 |
| `soc2010_soc2018.csv` | GitHub/danielruss | 2010↔2018 version crosswalk | 900 |

---

## Gotchas and Quirks

1. **The dash matters.** SOC codes are `XX-XXXX`, not `XXXXXX`. Some systems strip it; always normalize on ingestion.
2. **"All Other" residual codes** (ending in `9`) are catch-all categories. They're valid codes but represent "everything else not classified elsewhere" in that group.
3. **Level numbering is non-contiguous**: Levels are 2, 3, 5, 6 (there is no level 4). This is because the code digits used are positions 1-2 (major), 3 (minor), 4-5 (broad), 6 (detailed).
4. **Military codes (55-xxxx)** are included in the SOC structure but are not used by most civilian programs (OEWS, OES, etc.).
5. **BLS blocks automated downloads.** Any ingestion pipeline that needs official BLS files must download them manually or use the GitHub mirror.
6. **O\*NET has MORE occupations than SOC** because it subdivides some SOC codes. The mapping is many-to-one (multiple O\*NET codes → one SOC code).
