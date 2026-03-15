# Industry

# BlitzAPI - Values List - Industry

> **Case-sensitive.** Incorrect values silently return zero results.

This page contains the known industry values for the `industry` filter. BlitzAPI uses LinkedIn's industry taxonomy, which contains approximately **700 accepted values** according to the OpenAPI specification.

**Used in:**
- `POST /v2/search/companies` — `company.industry.include` / `company.industry.exclude` parameters
- Response field `industry` in company search and company enrichment results

### Common Mistakes

- Using generic terms like `"Tech"` instead of specific values like `"Computer Software"`
- Values must match the exact LinkedIn industry taxonomy string

## Industry Values Referenced in Documentation

The following industry values appear explicitly in BlitzAPI documentation and examples:

| Value |
|-------|
| Computer Software |
| Financial Services |
| Healthcare |
| Information Technology |
| Software Development |
| Technology, Information and Internet |

> **Note:** The canonical format is `"Technology, Information and Internet"` (with comma). An OpenAPI example contained a semicolon variant — disregard that; use the comma version.

---

*Source: BlitzAPI field normalization reference, OpenAPI specification v2.1.0, and endpoint documentation*

## JSON Array

The array below contains only the industry values explicitly referenced in BlitzAPI documentation. This is **not** the complete list.

```json
[
  "Computer Software",
  "Financial Services",
  "Healthcare",
  "Information Technology",
  "Software Development",
  "Technology, Information and Internet"
]
```

## Gaps

The BlitzAPI OpenAPI specification states there are **~700 accepted industry values** sourced from LinkedIn's industry taxonomy. Only 6 values are explicitly referenced in the current documentation. The full list should be sourced from:
- The BlitzAPI dashboard's industry filter dropdown
- API response inspection (the `industry` field in company search/enrichment results)
- LinkedIn's published industry taxonomy
- BlitzAPI support team

Until the complete list is obtained, downstream systems should validate industry values against actual API responses rather than relying solely on this partial list.
