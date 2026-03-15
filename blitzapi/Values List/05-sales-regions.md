# Sales Regions

# BlitzAPI - Values List - Sales Regions

> **Case-sensitive.** Incorrect values silently return zero results. Note: these are ALL CAPS.

This page contains all the possible values for the `sales_region` filter. These represent geographic sales territories.

**Used in:**
- `POST /v2/search/companies` — `company.hq.sales_region` parameter
- `POST /v2/search/employee-finder` — `sales_region` parameter

| Value | Description |
|-------|-------------|
| NORAM | North America |
| LATAM | Latin America |
| EMEA | Europe, Middle East, and Africa |
| APAC | Asia Pacific |

### Common Mistakes

- Using `"NA"` instead of `"NORAM"`
- Using lowercase like `"noram"` instead of `"NORAM"`

---

*Source: OpenAPI specification v2.1.0*

## JSON Array

```json
[
  "NORAM",
  "LATAM",
  "EMEA",
  "APAC"
]
```
