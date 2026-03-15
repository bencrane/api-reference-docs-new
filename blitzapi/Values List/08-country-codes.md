# Country Codes

# BlitzAPI - Values List - Country Codes

> **Case-sensitive.** Incorrect values silently return zero results. All codes are UPPERCASE two-letter.

BlitzAPI uses **ISO 3166-1 alpha-2** country codes consistent with LinkedIn. Additionally, the Waterfall ICP Search endpoint accepts the special value `"WORLD"` for unrestricted global searches.

**Used in:**
- `POST /v2/search/companies` — `company.hq.country_code` parameter
- `POST /v2/search/employee-finder` — `country_code` parameter
- `POST /v2/search/waterfall-icp-keyword` — `cascade[].location` parameter (also accepts `"WORLD"`)
- Response fields `country_code` in location/HQ objects

### Common Mistakes

- Using `"USA"` instead of `"US"`
- Using lowercase like `"us"` instead of `"US"`
- Using `"UK"` instead of `"GB"` for United Kingdom

## Country Codes Referenced in Documentation

The following country codes appear explicitly in BlitzAPI documentation and examples:

| Code | Country |
|------|---------|
| AU | Australia |
| BR | Brazil |
| CA | Canada |
| DE | Germany |
| FR | France |
| GB | United Kingdom |
| IN | India |
| SG | Singapore |
| US | United States |

### Special Values

| Value | Description | Endpoint |
|-------|-------------|----------|
| WORLD | Global / unrestricted search | Waterfall ICP Search only (`cascade[].location`) |

---

*Source: ISO 3166-1 alpha-2 standard; BlitzAPI appendix and endpoint documentation*

## JSON Array

The array below contains country codes explicitly referenced in BlitzAPI documentation, plus the special `WORLD` value. For the complete list of 249 ISO 3166-1 alpha-2 codes, refer to the ISO 3166-1 standard.

```json
[
  "AU",
  "BR",
  "CA",
  "DE",
  "FR",
  "GB",
  "IN",
  "SG",
  "US",
  "WORLD"
]
```

## Gaps

The full set of accepted country codes is the ISO 3166-1 alpha-2 standard (249 codes). Only 9 specific codes are explicitly referenced in the current BlitzAPI documentation. Any valid ISO 3166-1 alpha-2 code should be accepted by the API. The complete list can be sourced from:
- ISO 3166-1 alpha-2 specification
- BlitzAPI dashboard / API response inspection
