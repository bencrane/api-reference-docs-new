# Census ACS (American Community Survey) Overview | Geocodio API

**Field names:** `acs-demographics`, `acs-economics`, `acs-families`, `acs-housing`, `acs-social`

**Coverage:** US only

Geocodio retrieves statistics from the American Community Survey (ACS) for any US address or coordinate pair. Results are organized into five categories:

| Field | Category | Description |
|---|---|---|
| `acs-demographics` | Demographics | Population by age, sex, race, and ethnicity |
| `acs-economics` | Economics (Income) | Median income, household income, per capita income |
| `acs-families` | Families | Household types, marital status, family composition |
| `acs-housing` | Housing | Occupancy, tenure, units in structure, home values |
| `acs-social` | Social | Education attainment, veteran status |

## Pricing

Each ACS category counts as an additional lookup for billing purposes. The basic `census` field is included at no additional cost with any `acs-` field lookup.

## Geographic Levels

ACS data can be requested at specific geographic levels by appending the geography name:

| Geography | API Suffix | Example Field |
|---|---|---|
| Census Block Group | `block_group` | `acs-demographics-block_group` |
| Census Tract | `tract` | `acs-demographics-tract` |
| Census Place | `place` | `acs-demographics-place` |
| County Subdivision | `county_subdivision` | `acs-demographics-county_subdivision` |
| County | `county` | `acs-demographics-county` |
| Census MSA | `msa` | `acs-demographics-msa` |
| State | `state` | `acs-demographics-state` |

If no geography is specified, Geocodio selects the most appropriate level based on the geocoding accuracy:

| Accuracy Type | Default Geography |
|---|---|
| `rooftop`, `range_interpolation`, `nearest_street`, `point`, `nearest_rooftop_match`, `street_center`, `intersection` | Census Block Group |
| `nearest_place`, `place` | Census Place |
| `county` | County |
| `state` | State |

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=acs-demographics&api_key=YOUR_API_KEY"
```

```bash
# Request at a specific geography level
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=acs-demographics-county&api_key=YOUR_API_KEY"
```

## Metadata

All ACS responses include metadata at multiple levels:

**Overall ACS metadata:**

```json
{
  "acs": {
    "meta": {
      "source": "American Community Survey from the US Census Bureau",
      "survey_years": "2020-2024",
      "survey_duration_years": "5"
    }
  }
}
```

**Individual table metadata:**

```json
{
  "Median age": {
    "meta": {
      "table_id": "B01002",
      "universe": "Total population"
    }
  }
}
```

**Geography-level metadata (per ACS category):**

```json
{
  "demographics": {
    "meta": {
      "geography": "block_group"
    }
  }
}
```

## Data Format

Geocodio uses 5-year ACS estimates and always returns the most recent available data. Each data point includes:

- `value` -- the estimated count or amount
- `margin_of_error` -- the ACS-provided margin of error
- `percentage` -- a calculated percentage added by Geocodio for ease of use

```json
{
  "Male": {
    "value": 118902,
    "margin_of_error": 46,
    "percentage": 0.503
  }
}
```

The `census` field data (block, tract, FIPS codes) is automatically included with ACS responses at no extra charge.
