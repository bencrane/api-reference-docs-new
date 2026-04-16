# SOC ↔ NAICS Crosswalk — Canonical Reference

> **Last updated:** 2026-04-16
> **Purpose:** Map from NAICS industry codes to the SOC occupations typically employed in that industry

---

## Why This Matters

We have USASpending contract data telling us which companies won federal contracts in which NAICS industry. The SOC↔NAICS crosswalk lets us go from:

> "Company X just won a $5M manufacturing contract in **NAICS 332710** (Machine Shops)"

to:

> "They will likely need **Machinists (SOC 51-4041)**, **CNC Operators (SOC 51-4011)**, and **Quality Inspectors (SOC 51-9061)**"

That's the intelligence layer that makes staffing outreach proactive instead of reactive.

---

## Does a Direct SOC ↔ NAICS Crosswalk Exist?

**Yes, but it's not a simple lookup table.** There is no single file that says "NAICS 332710 → SOC 51-4041." Instead, the crosswalk exists as **employment data** — the BLS publishes how many workers in each occupation are employed in each industry. This employment data IS the crosswalk.

There are **two main sources**, both from BLS:

| Source | What It Is | Granularity | Best For |
|--------|-----------|-------------|----------|
| **BLS Employment Projections (EP) Matrix** | Projected employment by industry × occupation | 423 industries × ~800 occupations | Complete crosswalk with employment counts + percentages |
| **BLS OEWS Industry-Specific Data** | Survey-based employment + wages by industry × occupation | 4-digit NAICS × ~830 occupations | Current employment + wage data |

---

## Source 1: BLS Employment Projections Industry-Occupation Matrix

### Overview

The **National Employment Matrix** is the most comprehensive industry-occupation crosswalk. It combines data from CES, OEWS, and CPS to show employment for 423 industries × ~800 detailed occupations.

### Key Details

- **Classification systems:** 2022 NAICS (industries) × 2018 SOC (occupations)
- **Coverage:** 423 industries (2-digit through 6-digit NAICS) × all SOC codes at all hierarchy levels
- **Data type:** Employment counts (thousands), **percentage of industry**, **percentage of occupation**, base year (2024) and projected year (2034)
- **Update cadence:** Projections updated every 2 years; wages updated annually in April
- **Estimated size:** 50,000–90,000 NAICS-SOC pairs across all industries

### Download URLs

**BLS blocks automated downloads (403 for curl/wget/python).** Must be downloaded manually via browser.

| File | URL | Description |
|------|-----|-------------|
| Combined by Occupation | `https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx` | Full matrix (all industries for each occupation) |
| Per-Industry Files | `https://www.bls.gov/emp/ind-occ-matrix/ind-xlsx/ind-{NAICS}.xlsx` | One XLSX per NAICS code (e.g., `ind-332710.xlsx`) |
| Per-Occupation Files | `https://www.bls.gov/emp/ind-occ-matrix/occ-xlsx/occ-{SOC}.xlsx` | One XLSX per SOC code (e.g., `occ-51-4041.xlsx`) |
| Time Series Flat Files | `https://download.bls.gov/pub/time.series/ep/` | Flat files with series IDs |
| **Interactive Query API** | `https://data.bls.gov/projections/nationalMatrix?queryParams={NAICS}&ioType=i` | **Works from browser** (not blocked) |
| Browse by Industry | `https://www.bls.gov/emp/tables/industry-occupation-matrix-industry.htm` | HTML tables, one per industry |
| Browse by Occupation | `https://www.bls.gov/emp/tables/industry-occupation-matrix-occupation.htm` | HTML tables, one per occupation |

**Note:** `www.bls.gov` URLs return 403 for automated requests, but the `data.bls.gov` interactive query API works from browsers and may work from headless browsers.

### Schema (Confirmed via live query of `data.bls.gov`)

The industry-occupation matrix contains 13 columns per row:

| Column | Description |
|--------|-------------|
| `Occupation Title` | Occupation name (e.g., "Machinists") |
| `Occupation Code` | 6-digit SOC code (e.g., "51-4041") |
| `Occupation Type` | `Line Item` (detailed 6-digit) or `Summary` (rollup) |
| `2024 Employment` | Employment count in thousands |
| `2024 Percent of Industry` | What % of this industry's workforce is this occupation |
| `2024 Percent of Occupation` | What % of this occupation nationally works in this industry |
| `Projected 2034 Employment` | Projected employment in thousands |
| `Projected 2034 Percent of Industry` | Projected % of industry |
| `Projected 2034 Percent of Occupation` | Projected % of occupation |
| `Employment Change, 2024-2034` | Numeric change |
| `Employment Percent Change, 2024-2034` | Percentage change |
| `Occupation Sort` | Internal sort key |
| `Display Level` | Hierarchy depth (0-4) |

**Key insight:** The matrix already includes **both percentage columns** — you don't need to compute employment shares yourself.

### How It Maps Industry to Occupations

For a given NAICS industry, the matrix shows:
1. **Which occupations** are employed in that industry
2. **How many workers** in each occupation
3. **Employment share** (computable from the counts)

**Confirmed real data** — NAICS 332710 (Machine Shops), queried from `data.bls.gov`:

| Occupation | SOC Code | Employment (K) | % of Industry | % of Occupation |
|------------|----------|----------------|---------------|-----------------|
| Machinists | 51-4041 | 62.8 | 24.2% | 21.0% |
| CNC Tool Operators | 51-9161 | 28.7 | 11.1% | 16.2% |
| Welders, Cutters, Solderers | 51-4121 | 14.1 | 5.5% | 3.1% |
| First-Line Supervisors, Production | 51-1011 | 12.9 | 5.0% | 1.8% |
| General and Operations Managers | 11-1021 | 10.2 | 3.9% | 0.3% |
| Inspectors, Testers, Sorters | 51-9061 | 8.6 | 3.3% | 1.4% |
| CNC Tool Programmers | 51-9162 | 4.9 | 1.9% | 17.2% |

NAICS 332710 has **215 rows total** (124 detailed line-item occupations + 91 summary rollups). This lets you rank occupations by employment share within any NAICS industry.

---

## Source 2: BLS OEWS Industry-Specific Data

### Overview

The **Occupational Employment and Wage Statistics (OEWS)** program publishes employment and wage estimates by occupation for specific industries. This is based on actual survey data (not projections).

### Key Details

- **Classification systems:** 2022 NAICS × 2018 SOC
- **Industry granularity:** Sector (2-digit), subsector (3-digit), most 4-digit industry groups, and selected 5- and 6-digit industries
- **Occupation granularity:** Detailed and major occupation groups (~830 occupations)
- **Data type:** Employment counts, mean/median wages, percentile wages
- **Update cadence:** Annual (May reference period)
- **Current data:** May 2024 estimates

### Download URLs

**`www.bls.gov` blocks automated downloads (403).** Must be downloaded manually via browser.

| Resource | URL | Description |
|----------|-----|-------------|
| **All Data (bulk zip)** | `https://www.bls.gov/oes/special-requests/oesm24all.zip` | ALL geographies + industries combined |
| National Data | `https://www.bls.gov/oes/special-requests/oesm24nat.zip` | National cross-industry only |
| State Data | `https://www.bls.gov/oes/special-requests/oesm24st.zip` | State-level data |
| Metro Area Data | `https://www.bls.gov/oes/special-requests/oesm24ma.zip` | Metro area data |
| Industry Titles | `https://www.bls.gov/oes/2024/may/industry_titles_m2024.xlsx` | NAICS code → title lookup |
| Occupation Definitions | `https://www.bls.gov/oes/2024/may/occupation_definitions_m2024.xlsx` | SOC code definitions |
| Per-Industry Pages | `https://www.bls.gov/oes/2024/may/naics4_{NAICS}.htm` | One HTML page per NAICS code |

### Schema (Confirmed from OES bulk data)

The `oesm24all.zip` contains files with ~25 columns:

| Column | Description |
|--------|-------------|
| `AREA` / `AREA_TITLE` | Geographic area code and name |
| `NAICS` / `NAICS_TITLE` | NAICS industry code and name |
| `I_GROUP` | Industry group level |
| `OCC_CODE` / `OCC_TITLE` | SOC occupation code and name |
| `O_GROUP` | Occupation group level |
| `TOT_EMP` | Total employment |
| `EMP_PRSE` | Employment percent relative standard error |
| `H_MEAN` / `A_MEAN` | Mean hourly / annual wage |
| `H_MEDIAN` / `A_MEDIAN` | Median hourly / annual wage |
| `H_PCT10` / `H_PCT25` / `H_PCT75` / `H_PCT90` | Hourly wage percentiles |
| `A_PCT10` / `A_PCT25` / `A_PCT75` / `A_PCT90` | Annual wage percentiles |

### Advantages Over EP Matrix

- **Includes wage data** — know not just which occupations, but how much they earn in that industry
- **Based on actual survey data** (not projections)
- **Updated annually** (EP matrix is every 2 years)

### Limitations

- Industry granularity is mainly at 4-digit NAICS (not always 6-digit)
- Some occupation × industry cells are suppressed for confidentiality
- Not all NAICS codes have published data

---

## Source 3: O\*NET Related Occupations (Supplementary)

While not a direct NAICS→SOC crosswalk, O\*NET provides:

- **Related Occupations.txt** — maps similar occupations (useful for expanding from known occupations to related ones)
- **Technology Skills.txt** — shared technology platforms across occupations can indicate industry overlap
- **Task Statements.txt** — shared tasks can identify occupations in similar industries

These are not substitutes for the BLS data but can supplement it.

---

## Recommended Ingestion Strategy

### For the Initial Crosswalk Table

**Primary source: BLS Employment Projections Matrix (manually downloaded)**

1. Manually download `occupation.xlsx` from `https://www.bls.gov/emp/ind-occ-matrix/occupation.xlsx`
2. Also download individual industry files from `https://www.bls.gov/emp/ind-occ-matrix/ind-xlsx/ind-{NAICS}.xlsx` for key NAICS codes
3. Parse into a `naics_soc_crosswalk` table:

```sql
CREATE TABLE naics_soc_crosswalk (
    naics_code VARCHAR(6),              -- NAICS industry code
    naics_title TEXT,                    -- Industry name
    soc_code VARCHAR(7),                -- SOC occupation code (XX-XXXX)
    soc_title TEXT,                      -- Occupation name
    occupation_type VARCHAR(10),         -- 'Line Item' (detailed) or 'Summary' (rollup)
    employment_2024 DECIMAL,            -- Base year employment (thousands)
    pct_of_industry DECIMAL,            -- % of this industry's workforce
    pct_of_occupation DECIMAL,          -- % of this occupation nationally in this industry
    employment_2034 DECIMAL,            -- Projected employment (thousands)
    employment_pct_change DECIMAL,      -- Projected % change
    source VARCHAR(20) DEFAULT 'BLS_EP'
);
```

### For Wage-Enriched Data

**Secondary source: BLS OEWS data (manually downloaded)**

1. Download OEWS industry-specific files from `https://www.bls.gov/oes/tables.htm`
2. Parse to add wage columns:

```sql
ALTER TABLE naics_soc_crosswalk ADD COLUMN mean_annual_wage DECIMAL;
ALTER TABLE naics_soc_crosswalk ADD COLUMN median_annual_wage DECIMAL;
```

### Querying the Crosswalk

The EP matrix already includes percentage columns, so queries are straightforward:

```sql
-- Top occupations in Machine Shops by % of industry workforce
SELECT soc_code, soc_title, employment_2024, pct_of_industry
FROM naics_soc_crosswalk
WHERE naics_code = '332710'
  AND occupation_type = 'Line Item'
ORDER BY pct_of_industry DESC
LIMIT 10;
```

---

## Concrete Usage Example

**Starting point:** A company won a contract in NAICS 332710 (Machine Shops).

**Step 1:** Look up NAICS 332710 in the crosswalk:
```sql
SELECT soc_code, soc_title, employment_2024
FROM naics_soc_crosswalk
WHERE naics_code = '332710'
ORDER BY employment_2024 DESC
LIMIT 10;
```

**Step 2:** For each SOC code, look up skills and alternate titles in O\*NET:
```sql
-- Get alternate titles for matching
SELECT alternate_title
FROM onet_alternate_titles
WHERE onet_soc_code LIKE '51-4041%';  -- Machinists

-- Get required skills
SELECT element_name, data_value
FROM onet_skills
WHERE onet_soc_code = '51-4041.00'
AND scale_id = 'IM'
ORDER BY data_value DESC;
```

**Step 3:** Use alternate titles to search resumes, job boards, or candidate databases for people with matching job titles.

---

## Known Gaps and Flags

1. **BLS blocks all automated downloads.** Both EP matrix and OEWS data must be manually downloaded via browser. This is the biggest operational friction.

2. **No single flat-file crosswalk.** The data exists as Excel files organized by industry or occupation, not as a single `NAICS_code, SOC_code, employment` CSV. Parsing required.

3. **Industry granularity varies.** The EP matrix has 423 industries ranging from 2-digit sectors to 6-digit NAICS codes. Machine Shops (332710) IS available at the 6-digit level, but not every 6-digit NAICS code has its own entry — some are only available at 4- or 5-digit rollup.

4. **NAICS version alignment.** The EP matrix uses 2022 NAICS. Our USASpending data may use earlier NAICS versions. Cross-referencing may require a NAICS version crosswalk (see `naics/` directory).

5. **SOC version alignment.** Both sources use 2018 SOC. O\*NET uses O\*NET-SOC 2019. Minor differences exist — use the `2019_to_SOC_Crosswalk.csv` to bridge.

6. **Some industries have suppressed data.** Small industries or rare occupation × industry combinations may have data suppressed for confidentiality.

7. **The crosswalk is probabilistic, not deterministic.** NAICS 332710 doesn't ONLY employ Machinists — it also employs office staff, managers, etc. The employment shares tell you which occupations are most likely, not which are guaranteed.

---

## Alternative Approaches (If BLS Data Is Inaccessible)

If the BLS download blockade proves insurmountable:

1. **BLS Public Data API** (`https://api.bls.gov/publicAPI/v2/`) — Supports OEWS series queries. Series IDs follow a pattern encoding area, industry, and occupation codes. Requires registration for v2 (higher rate limits). Could programmatically pull industry × occupation employment data.

2. **Data.gov catalog** — `https://catalog.data.gov/dataset/standard-occupational-classification-da7d9` — May have archived SOC datasets.

3. **Build from O\*NET + domain knowledge** — For the most common NAICS codes in federal contracting, manually map typical occupations. Not scalable but works for initial MVP.

4. **Census Bureau microdata** — American Community Survey (ACS) PUMS data includes both industry and occupation codes for individual workers. Could build a crosswalk from microdata (heavy lift).
