# Timezone | Geocodio API

**Field name:** `timezone`

**Coverage:** US and Canada

Returns the timezone for an address or coordinate pair, including the standardized name, abbreviation, UTC offset, and whether the location observes Daylight Saving Time.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=timezone&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=timezone&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "timezone": {
      "name": "America/New_York",
      "utc_offset": -5,
      "observes_dst": true,
      "abbreviation": "EST",
      "source": "\u00a9 OpenStreetMap contributors"
    }
  }
}
```

## Response Fields

| Field | Description |
|---|---|
| `name` | Standardized timezone name in tzdb format (e.g., `America/New_York`) |
| `utc_offset` | UTC/GMT offset as an integer (e.g., `-5`) |
| `observes_dst` | Whether the location observes Daylight Saving Time (`true`/`false`) |
| `abbreviation` | Timezone abbreviation (see table below) |
| `source` | Data source attribution |

## Timezone Abbreviations

| Abbreviation | Description |
|---|---|
| `AKST` | Alaska Standard Time |
| `AST` | Atlantic Standard Time |
| `ChST` | Chamorro Standard Time |
| `CST` | Central Standard Time |
| `EST` | Eastern Standard Time |
| `HAST` | Hawaii-Aleutian Standard Time |
| `MST` | Mountain Standard Time |
| `PST` | Pacific Standard Time |
| `SST` | Samoa Standard Time |

## Skip Geocoding

You can extract timezone data from coordinates without performing a full geocode by using the `skipGeocoding` parameter:

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.9002898,-76.9990361&skipGeocoding&fields=timezone&api_key=YOUR_API_KEY"
```

```json
{
  "results": [
    {
      "location": {
        "lat": 38.9002898,
        "lng": -76.9990361
      },
      "accuracy_type": "coordinate",
      "fields": {
        "timezone": {
          "name": "America/New_York",
          "utc_offset": -5,
          "observes_dst": true,
          "abbreviation": "EST",
          "source": "\u00a9 OpenStreetMap contributors"
        }
      }
    }
  ]
}
```
