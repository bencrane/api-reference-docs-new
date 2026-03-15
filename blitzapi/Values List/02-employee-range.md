# Employee Range

# BlitzAPI - Values List - Employee Range

> **Case-sensitive.** Incorrect values silently return zero results.

This page contains all the possible values for the `employee_range` filter. These represent company size brackets based on LinkedIn employee count.

**Used in:**
- `POST /v2/search/companies` — `company.employee_range` parameter
- Response field `size` in company search and company enrichment results

| Value |
|-------|
| 1-10 |
| 11-50 |
| 51-200 |
| 201-500 |
| 501-1000 |
| 1001-5000 |
| 5001-10000 |
| 10001+ |

---

*Source: OpenAPI specification v2.1.0*

## JSON Array

```json
[
  "1-10",
  "11-50",
  "51-200",
  "201-500",
  "501-1000",
  "1001-5000",
  "5001-10000",
  "10001+"
]
```
