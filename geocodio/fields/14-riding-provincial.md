# Canadian Provincial Electoral District (Riding) | Geocodio API

**Field name:** `provriding` or `provriding-next`

**Coverage:** Canada only

Returns the provincial or territorial electoral district (riding) for a Canadian address or coordinate pair. Includes the OCD-ID and French/English names.

- `provriding` returns districts based on current boundaries.
- `provriding-next` returns districts based on upcoming redistricted boundaries.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=300+King+St%2C+Sturgeon+Falls%2C+ON+P2B+3A1%2C+Canada&fields=provriding&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=46.225866,-79.36316&fields=provriding&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "provincial_riding": {
      "ocd_id": "ocd-division/country:ca/province:on/ed:timiskaming-cochrane",
      "name_french": "Timiskaming - Cochrane",
      "name_english": "Timiskaming - Cochrane",
      "is_upcoming_district": false,
      "source": "Elections Ontario"
    }
  }
}
```

## Response Fields

| Field | Description |
|---|---|
| `ocd_id` | Open Civic Data Division Identifier for unique identification |
| `name_french` | French name of the riding |
| `name_english` | English name of the riding |
| `is_upcoming_district` | Whether this is a future redistricted district |
| `source` | Data source (e.g., "Elections Ontario", "Elections Saskatchewan") |

## Using provriding-next

`provriding-next` provides a preview of upcoming redistricted provincial ridings.

```bash
curl "https://api.geocod.io/v1.12/geocode?q=203+Laycoe+Crescent%2C+Saskatoon%2C+SK%2C+Canada&fields=provriding-next&api_key=YOUR_API_KEY"
```

Example response for `provriding-next`:

```json
{
  "fields": {
    "provincial_riding": {
      "ocd_id": "ocd-division/country:ca/province:sk/ed:49-2022",
      "name_french": "Saskatoon Silverspring",
      "name_english": "Saskatoon Silverspring",
      "is_upcoming_district": false,
      "source": "Elections Saskatchewan"
    }
  }
}
```

## Notes

- The OCD-ID can be used to uniquely identify the district using the Open Civic Data Division Identifiers project.
- In some cases, the French and English names will be the same.
