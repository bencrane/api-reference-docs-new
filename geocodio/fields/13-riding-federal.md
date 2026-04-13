# Canadian Federal Electoral District (Riding) | Geocodio API

**Field name:** `riding`

**Coverage:** Canada only

Returns the Canadian federal electoral district (riding) for an address or coordinate pair. Includes the riding code, OCD-ID, and French/English names.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=300+King+St%2C+Sturgeon+Falls%2C+ON+P2B+3A1%2C+Canada&fields=riding&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=46.225866,-79.36316&fields=riding&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "riding": {
      "year": 2023,
      "code": "35104",
      "ocd_id": "ocd-division/country:ca/ed:35104-2023",
      "name_french": "Sudbury-Est\u2014Manitoulin\u2014Nickel Belt",
      "name_english": "Sudbury East\u2014Manitoulin\u2014Nickel Belt",
      "source": "Federal Redistribution"
    }
  }
}
```

## Response Fields

| Field | Description |
|---|---|
| `year` | The redistribution year for the riding boundaries |
| `code` | Federal electoral district code |
| `ocd_id` | Open Civic Data Division Identifier for unique identification |
| `name_french` | French name of the riding |
| `name_english` | English name of the riding |
| `source` | Data source (e.g., "Federal Redistribution") |

## Notes

- The OCD-ID can be used to uniquely identify the district using the Open Civic Data Division Identifiers project.
- In some cases, the French and English names will be the same.
