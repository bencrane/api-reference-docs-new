# Data Appends (Fields) Overview | Geocodio API

Geocodio allows you to request additional data with forward and reverse geocoding requests. This additional data is called **fields** (also referred to as data appends).

## Requesting Fields

Add a `fields` query parameter to your geocoding request. Specify one or more field names separated by commas.

```
fields=cd,stateleg
```

Fields work with all geocoding endpoints:

- Forward geocoding (`/geocode`)
- Reverse geocoding (`/reverse`)
- Batch geocoding
- Lists API

When the `fields` parameter is specified, a `fields` key is added to each geocoding result containing the appended data.

> **Note:** Each field counts as an additional lookup for billing purposes. See the Geocodio pricing calculator.

## Example Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=cd,stateleg&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=cd,stateleg&api_key=YOUR_API_KEY"
```

## Available Fields

| Parameter Name | Description | Coverage |
|---|---|---|
| `cd`, `cd113`..`cd120` | Congressional District & Legislator information | US only |
| `stateleg`, `stateleg-next` | State Legislative District (House & Senate) & Legislator information | US only |
| `school` | School District (elementary/secondary or unified) | US only |
| `census`, `census2000`..`census2025` | Census Block/Tract, FIPS codes & MSA/CSA codes | US only |
| `acs-demographics` | Demographics (Census ACS) | US only |
| `acs-economics` | Economics: Income Data (Census ACS) | US only |
| `acs-families` | Families (Census ACS) | US only |
| `acs-housing` | Housing (Census ACS) | US only |
| `acs-social` | Social: Education & Veteran Status (Census ACS) | US only |
| `zip4` | USPS ZIP+4 code and delivery information | US only |
| `ffiec` | FFIEC CRA/HMDA Data (Beta) | US only |
| `riding` | Canadian Federal Electoral District | Canada only |
| `provriding`, `provriding-next` | Canadian Provincial/Territorial Electoral District | Canada only |
| `statcan` | Canadian statistical boundaries from Statistics Canada | Canada only |
| `timezone` | Timezone | US & Canada |

## Response Structure

When fields are requested, the response includes a `fields` object nested inside each result:

```json
{
  "results": [
    {
      "address_components": { ... },
      "formatted_address": "...",
      "location": { ... },
      "accuracy": 1,
      "accuracy_type": "rooftop",
      "fields": {
        "congressional_districts": [ ... ],
        "state_legislative_districts": { ... }
      }
    }
  ]
}
```

Some fields are specific to the US and cannot be queried for other countries. Canadian-specific fields (`riding`, `provriding`, `statcan`) only work with Canadian addresses.
