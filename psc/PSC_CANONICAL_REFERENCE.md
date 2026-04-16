# PSC Codes (Product Service Codes) — Canonical Reference

> **Produced:** 2026-04-15
> **Purpose:** Reference for building a PSC code ingestion pipeline into Postgres
> **Current version:** PSC April 2025 (GSA official)

---

## 1. What Is a PSC Code?

**Product Service Codes (PSC)** classify **what the federal government buys**. Every federal contract award in FPDS (Federal Procurement Data System) and USASpending is tagged with a PSC code describing the product or service being acquired.

PSC codes answer: _"What did the government procure?"_ — as opposed to NAICS codes, which answer _"What industry is the seller in?"_

PSC is maintained by the **General Services Administration (GSA)**.

---

## 2. Code Structure

PSC codes follow a **two-tier hierarchy**: group headers (1-2 characters) and leaf codes (4 characters).

### Product Codes (physical goods)
- **Group headers:** 2-digit numeric (e.g., `10` = WEAPONS, `58` = COMM/DETECT/COHERENT RADIATION)
- **Leaf codes:** 4-digit numeric (e.g., `1005` = GUNS, THROUGH 30MM; `5820` = RADIO AND TV COMMUNICATION EQUIPMENT)
- There are **75 product group headers** and **639 current product leaf codes**.

### Service Codes (services, R&D, construction, etc.)
- **Group headers:** 1-2 character alphabetic (e.g., `D` = IT AND TELECOM, `R` = SUPPORT SVCS)
- **Leaf codes:** 4-character alphanumeric, letter prefix (e.g., `D301` = IT AND TELECOM - FACILITY OPERATION AND MAINTENANCE, `R425` = SUPPORT - PROFESSIONAL: ENGINEERING/TECHNICAL)
- There are **96 service group headers** and **1,705 current service leaf codes** (including R&D sub-codes like `AA11`).

### Special Codes
- **Category 7 (IT):** Has a separate structure with `7A20`, `7B20`, etc. — product codes under IT that use alphanumeric format.
- **Group code `A`:** Research and Development, with sub-groups `AA` through `AS` covering different R&D domains.

### How to distinguish products from services
The GSA spreadsheet includes a `PSC Category: Service (S)/Product (P)` column. Alternatively:
- If the first character is a **digit** → **Product** code
- If the first character is a **letter** → **Service** code
- Exception: `7A`, `7B` prefix codes are products classified under IT

---

## 3. Sources Investigated

### 3a. GSA Official PSC Spreadsheet (XLSX) ⭐ RECOMMENDED

- **URL:** `https://www.acquisition.gov/sites/default/files/manual/PSC%20April%202025.xlsx`
- **Format:** XLSX, 2 sheets
- **Size:** 463 KB
- **Saved as:** `psc/PSC_April_2025.xlsx`

**Sheet 1: "PSC for 042025"** — the main data

| Column | Content |
|--------|---------|
| A | PSC CODE (numeric or alphanumeric) |
| B | PRODUCT AND SERVICE CODE NAME |
| C | START DATE (datetime) |
| D | END DATE (datetime, null = currently active) |
| E | PRODUCT AND SERVICE CODE FULL NAME (DESCRIPTION) |
| F | PRODUCT AND SERVICE CODE INCLUDES |
| G | PRODUCT AND SERVICE CODE EXCLUDES |
| H | PRODUCT AND SERVICE CODE NOTES |
| I | Parent PSC Code (e.g., "10 - WEAPONS") |
| J | PSC Category: Service (S)/Product (P) |
| K | Level 1 Category Code (numeric) |
| L | Level 1 Category (text) |
| M | Level 2 Category Code (numeric) |
| N | Level 2 Category (text) |

**Row counts:**
- Total rows: 6,108 (including historical/retired codes with end dates)
- Current codes (no end date): **2,540**
- Current codes with parent references: 2,449

**Key design detail:** The spreadsheet includes **both current and historical versions** of codes. A single PSC code (e.g., `1005`) may appear in multiple rows — one with an end date (historical) and one without (current). **Filter on `END DATE IS NULL`** to get only current codes.

**Sample current records:**

```
Code: 1005     Name: GUNS, THROUGH 30MM
  Parent: 10 - WEAPONS
  Category: (blank, but numeric = Product)
  Level 1: 12 - Weapons & Ammunition
  Level 2: 12.4 - Guns

Code: D301     Name: IT AND TELECOM- FACILITY OPERATION AND MAINTENANCE  
  Parent: D - IT AND TELECOM
  Category: S (Service)
  Level 1: 1 - IT
  Level 2: 1.3 - IT Professional Service (Labor)
```

**Sheet 2: "Category Managers"** — government category manager contact info (20 categories, names/emails). Not needed for code ingestion.

**Government-wide Category Management taxonomy (Level 1 categories, 20 total):**

| Code | Category |
|------|----------|
| 1 | IT |
| 2 | Professional Services |
| 3 | Security and Protection |
| 4 | Facilities & Construction |
| 5 | Industrial Products & Services |
| 6 | Office Management |
| 7 | Transportation and Logistics Services |
| 8 | Travel & Lodging |
| 9 | Human Capital |
| 10 | Medical |
| 11 | Aircraft, Ships/Submarines & Land Vehicles |
| 12 | Weapons & Ammunition |
| 13 | Electronic & Communication Equipment |
| 14 | Sustainment S&E |
| 15 | Clothing, Textiles & Subsistence S&E |
| 16 | Miscellaneous S&E |
| 17 | Research and Development |
| 18 | Equipment Related Services |
| 19 | Electronic & Communication Services |

There are **80 Level 2 sub-categories** within these.

### 3b. CSIS Defense Lookup Tables (CSV)

- **URL:** `https://github.com/CSISdefense/Lookup-Tables` → `ProductOrServiceCodes.csv`
- **Format:** CSV, 43 columns
- **Size:** 3,583 rows (3,582 unique codes)
- **Saved as:** `psc/ProductOrServiceCodes_CSIS.csv`

**Key columns:**

| Column | Content |
|--------|---------|
| ProductOrServiceCode | PSC code |
| ProductOrServiceCodeText | Description |
| IsService | TRUE/FALSE |
| Level1_Code | Level 1 category code |
| Level1_Category | Level 1 category name |
| Level2_Code | Level 2 category code |
| Level2_Category | Level 2 category name |
| DoDportfolioGroup | DoD-specific portfolio grouping |
| DoDportfolio | DoD portfolio name |

**43 columns total** including many CSIS/DoD-specific analytical fields: `ServicesCategory`, `HostNation3Category`, `PBLscore`, `OCOcrisisScore`, `GreenEnergy`, `BioRelated`, `IsPossibleC2`, `IsRemotelyOperated`, etc.

**Verdict:** Comprehensive and machine-readable CSV. However, it's maintained by a think tank (CSIS) for defense procurement analysis — **not the authoritative GSA source**. Includes many columns irrelevant to general PSC lookup. Contains more codes than the GSA "current" set because it includes historical codes. The analytical columns (DoD portfolio, crisis scores, etc.) may be valuable for defense-specific analysis but are not part of the official PSC standard.

### 3c. PSC Tool API (`psctool.us`)

- **URL:** `https://psctool.us/apidocs`
- **Status:** The API documentation page only renders in a browser (requires JavaScript). Direct API endpoint probing (`/api/psc`, `/api/psc?code=1005`) returns **404 errors**.
- **Verdict:** **Not usable as a data source.** The PSC Tool is a web-based GUI search tool, not a public API. No programmatic access available.

### 3d. AbilityOne PSC-NAICS File (XLSX)

- **URL:** `https://www.abilityone.gov/media_room/documents/Product_Services_NAICS_PSC_2021_06_28.xlsx`
- **Format:** XLSX, 4 sheets
- **Size:** 35 KB
- **Saved as:** `psc/AbilityOne_PSC_NAICS_Crosswalk.xlsx`

**Sheet structure:**

| Sheet | Rows | Columns | Content |
|-------|------|---------|---------|
| Product PSC Codes | 161 | PSC, PRODUCT_AND_SERVICE_CODE_NAME | Subset of product PSCs |
| Product NAICS | 348 | NAICS, NAICS Description | NAICS codes relevant to products |
| Services PSC | 156 | Product_or_Service_Code, PRODUCT_AND_SERVICE_CODE_NAME | Subset of service PSCs |
| Services NAICS | 24 | NAICS_Code, NAICS_Title | NAICS codes relevant to services |

**Critical finding:** Despite the filename suggesting a crosswalk, **this file does NOT contain a PSC-to-NAICS mapping.** It has 4 separate lists: product PSCs, product NAICS, service PSCs, and service NAICS. There is no column linking a specific PSC code to a specific NAICS code. It's a scope document for AbilityOne procurement categories, not a crosswalk.

**Verdict:** **Not useful as a PSC-NAICS crosswalk.** Only useful as a curated subset of ~300 PSC codes relevant to AbilityOne contracting.

---

## 4. PSC ↔ NAICS Mapping

### Does a reliable PSC-to-NAICS mapping exist?

**No single authoritative source provides a direct PSC-to-NAICS crosswalk.** The two classification systems are orthogonal by design:
- **NAICS** classifies the **seller** (what industry they're in)
- **PSC** classifies the **purchase** (what the government bought)

A company in NAICS `334111` (Electronic Computer Manufacturing) might sell products under dozens of different PSC codes.

**Indirect mapping via USASpending:** The most practical PSC-to-NAICS mapping comes from **actual contract data**. USASpending contract records contain both `product_or_service_code` (PSC) and `naics_code` (NAICS) columns. By aggregating historical awards, you can build a probabilistic mapping of which NAICS codes are most commonly associated with each PSC code. This is a derived relationship, not a canonical one.

**GSA PSC Category → NAICS rough alignment:** The 20 Level 1 PSC categories (IT, Professional Services, Medical, etc.) loosely correspond to NAICS sectors, but this is a conceptual alignment, not a code-level mapping.

---

## 5. Recommended Primary Source

### Use: **GSA Official PSC Spreadsheet** (`PSC_April_2025.xlsx`)

**Why:**

1. **Authoritative** — GSA is the official maintainer of PSC codes.
2. **Complete** — contains all current and historical codes with full metadata (descriptions, includes/excludes, parent hierarchy, category taxonomy).
3. **Rich metadata** — the `INCLUDES`, `EXCLUDES`, and `NOTES` columns provide disambiguation that no other source offers.
4. **Hierarchy built in** — the `Parent PSC Code` column and Level 1/Level 2 category columns encode the full hierarchy without needing to derive it.
5. **Versioned** — START/END dates let you reconstruct the PSC code set at any point in time.
6. **Current** — April 2025 release, the latest available.

**Ingestion notes for the follow-up agent:**

- Parse with openpyxl or pandas. Sheet name: `"PSC for 042025"` (will change with each release).
- **Filter on `END DATE IS NULL`** to get only current codes. Including historical codes is optional but useful for matching older contract data.
- PSC CODE column is mixed type: numeric for product codes (stored as float, e.g., `1005.0`), string for service codes (e.g., `D301`). Normalize all to text during ingestion. For numeric codes, strip `.0` and zero-pad to 4 digits if needed.
- Parent PSC Code column format: `"10 - WEAPONS"` — parse out the code prefix if you want a foreign key.
- Level 1/Level 2 category codes are numeric (floats). Cast to integer.
- Some rows are group headers (2-digit numeric or 1-2 char alpha) rather than leaf codes. These have no parent. Store them — they're useful as category reference.

---

## 6. Recommended Postgres Schema

```sql
CREATE TABLE lookup.psc_codes (
    psc_code             TEXT PRIMARY KEY,       -- e.g., '1005', 'D301', '10'
    name                 TEXT NOT NULL,           -- short name
    full_name            TEXT,                    -- longer description
    includes             TEXT,                    -- what this code includes
    excludes             TEXT,                    -- what this code excludes
    notes                TEXT,                    -- additional notes
    start_date           DATE,                   -- when this code became active
    end_date             DATE,                   -- null = currently active
    parent_psc_code      TEXT,                    -- parent group code (e.g., '10')
    is_product           BOOLEAN,                -- true = product, false = service
    level1_category_code SMALLINT,               -- government-wide category code
    level1_category      TEXT,                    -- e.g., 'Weapons & Ammunition'
    level2_category_code NUMERIC(4,1),           -- e.g., 12.4
    level2_category      TEXT,                    -- e.g., 'Guns'
    is_current           BOOLEAN DEFAULT TRUE,    -- derived from end_date IS NULL
    created_at           TIMESTAMPTZ DEFAULT NOW()
);

-- For historical codes, use a composite key instead:
-- PRIMARY KEY (psc_code, start_date)

CREATE INDEX idx_psc_parent ON lookup.psc_codes (parent_psc_code);
CREATE INDEX idx_psc_current ON lookup.psc_codes (is_current) WHERE is_current = TRUE;
CREATE INDEX idx_psc_level1 ON lookup.psc_codes (level1_category_code);
CREATE INDEX idx_psc_product ON lookup.psc_codes (is_product);
```

---

## 7. Relevance to USASpending

USASpending contract data (`usaspending_contracts` in our database, 14.6M+ rows) includes a `product_or_service_code` column.

**Mapping:** The `product_or_service_code` value in USASpending corresponds directly to the **4-character/digit leaf codes** in the PSC spreadsheet. Examples:
- `1005` → GUNS, THROUGH 30MM
- `D301` → IT AND TELECOM - FACILITY OPERATION AND MAINTENANCE
- `R425` → SUPPORT - PROFESSIONAL: ENGINEERING/TECHNICAL

**Format considerations:**
- USASpending stores PSC codes as text (already normalized)
- Product codes may appear with or without leading zeros (e.g., `1005` vs `1005`)
- Service codes are always alphanumeric (`D301`, `AA11`)

The PSC lookup table enables joining USASpending contract data to human-readable descriptions, category taxonomies, and parent hierarchies — answering questions like "How much did the government spend on IT services?" (filter Level 1 = IT) or "What specific weapons were procured?" (filter parent = `10`).

---

## 8. Update Cadence

The PSC code list is updated by GSA on an **as-needed basis** (not on a fixed cycle like NAICS). Updates typically happen 1-2 times per year. The most recent update is **April 2025**.

Changes are tracked via START/END dates in the spreadsheet. When a code is retired, its row gets an END DATE; when a new code is added or an existing code is revised, a new row is created with a new START DATE.

The PSC Manual (separate PDF/DOCX) provides detailed guidance on classification decisions and is updated alongside the spreadsheet.

---

## 9. Service Code Letter Groups

For reference, here are the top-level service code letter groups:

| Letter | Category |
|--------|----------|
| A | Research and Development |
| B | Special Studies/Analysis, Not R&D |
| C | Architect/Engineer Services |
| D | IT and Telecom |
| E | Purchase of Structures/Facilities |
| F | Natural Resources Management |
| G | Social Services |
| H | Quality Control, Test, Inspection |
| J | Maintenance, Repair, Rebuild Equipment |
| K | Modification of Equipment |
| L | Technical Representative Services |
| M | Operation of Government-Owned Facility |
| N | Installation of Equipment |
| P | Salvage Services |
| Q | Medical Services |
| R | Support Services (Professional, Admin, Mgmt) |
| S | Utilities and Housekeeping |
| T | Photo, Map, Print, Publication |
| U | Education and Training |
| V | Transport, Travel, Relocation |
| W | Lease/Rent Equipment |
| X | Lease/Rent Facilities |
| Y | Construction of Structures/Facilities |
| Z | Maintenance, Repair, Alter Real Property |

---

## 10. Source Files Saved

| File | Description |
|------|-------------|
| `psc/PSC_April_2025.xlsx` | GSA official PSC spreadsheet (recommended primary source) |
| `psc/ProductOrServiceCodes_CSIS.csv` | CSIS defense lookup table (3,582 codes, 43 analytical columns) |
| `psc/AbilityOne_PSC_NAICS_Crosswalk.xlsx` | AbilityOne scope document (NOT an actual PSC-NAICS crosswalk) |
