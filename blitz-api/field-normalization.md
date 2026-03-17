# BlitzAPI Field Normalization

## Overview
BlitzAPI Search endpoints require **case-sensitive normalized values** for categorical filters. Incorrect values silently return zero results, so precision is critical.

## Key Field Categories

### Employee Range (8 tiers)
Ranges from `"1-10"` through `"10001+"` employees for company sizing in searches.

### Job Levels (6 categories)
- `"C-Team"`
- `"VP"`
- `"Director"`
- `"Manager"`
- `"Staff"`
- `"Other"`

### Job Functions (22 options)
Spans roles including:
- `"Advertising & Marketing"`
- `"Engineering"`
- `"Sales & Business Development"`
- `"Human Resources"`
- `"Writing/Editing"`
- And more...

### Sales Regions (4 areas)
- `"NORAM"` (North America)
- `"LATAM"` (Latin America)
- `"EMEA"` (Europe, Middle East, Africa)
- `"APAC"` (Asia Pacific)

### Continents (7 options)
- Africa
- Antarctica
- Asia
- Europe
- North America
- Oceania
- South America

### Company Types (10 classifications)
- `"Public Company"`
- `"Privately Held"`
- `"Nonprofit"`
- `"Government Agency"`
- And more...

### Industry (150+ categories)
Comprehensive taxonomy including:
- `"Computer Software"`
- `"Healthcare"`
- `"Financial Services"`
- And many more...

### Country Codes
Uses ISO 3166-1 alpha-2 standard (e.g., `"US"`, `"GB"`, `"FR"`). Waterfall ICP accepts `"WORLD"` for global searches.

## Common Mistakes
- Using `"Tech"` instead of specific values like `"Computer Software"`
- Entering `"USA"` instead of `"US"`
- Writing `"vp"` instead of `"VP"` (case-sensitive!)
- Applying `"NA"` instead of `"NORAM"`

All values require exact case matching and copy-paste verification to avoid failures.
