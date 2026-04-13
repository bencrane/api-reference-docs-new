# School Districts | Geocodio API

**Field name:** `school`

**Coverage:** US only

Returns the school district for an address or coordinate pair. Depending on the area, the response contains either a **unified** school district or separate **elementary** and **secondary** districts.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=school&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=school&api_key=YOUR_API_KEY"
```

## Response -- Unified School District

```json
{
  "fields": {
    "school_districts": {
      "unified": {
        "name": "Desert Sands Unified School District",
        "lea_code": "11110",
        "grade_low": "KG",
        "grade_high": "12"
      }
    }
  }
}
```

## Response -- Elementary/Secondary School Districts

```json
{
  "fields": {
    "school_districts": {
      "elementary": {
        "name": "Topsfield School District",
        "lea_code": "11670",
        "grade_low": "PK",
        "grade_high": "06"
      },
      "secondary": {
        "name": "Masconomet School District",
        "lea_code": "07410",
        "grade_low": "07",
        "grade_high": "12"
      }
    }
  }
}
```

## Response Fields

| Field | Description |
|---|---|
| `name` | Full name of the school district |
| `lea_code` | Local Education Agency (LEA) code |
| `grade_low` | Lowest grade served. `KG` = Kindergarten, `PK` = Pre-Kindergarten |
| `grade_high` | Highest grade served |

## Notes

- The response contains either a `unified` key or both `elementary` and `secondary` keys, depending on how the area's school districts are organized.
- The LEA code is the standard identifier used by the National Center for Education Statistics (NCES).
