# Census Block/Tract, FIPS Codes & MSA/CSA Codes | Geocodio API

**Field name:** `census`, `census2000`, `census2010`, `census2011`, `census2012`, `census2013`, `census2014`, `census2015`, `census2016`, `census2017`, `census2018`, `census2019`, `census2020`, `census2021`, `census2022`, `census2023`, `census2024`, `census2025`

**Coverage:** US only

Returns US Census-designated geographies including Census Tract, Census Block, FIPS codes, MSA/CSA codes, and more.

## Request

Request multiple vintage years simultaneously by comma-separating field names:

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=census2010,census&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=census2010,census&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "census": {
      "2010": {
        "census_year": 2010,
        "state_fips": "51",
        "county_fips": "51013",
        "tract_code": "101801",
        "block_code": "1004",
        "block_group": "1",
        "full_fips": "510131018011004",
        "place": {
          "name": "Arlington",
          "fips": "5103000"
        },
        "metro_micro_statistical_area": {
          "name": "Washington-Arlington-Alexandria, DC-VA-MD-WV",
          "area_code": "47900",
          "type": "metropolitan"
        },
        "combined_statistical_area": {
          "name": "Washington-Baltimore-Northern Virginia, DC-MD-VA-WV",
          "area_code": "51548"
        },
        "metropolitan_division": {
          "name": "Washington-Arlington-Alexandria, DC-VA-MD-WV",
          "area_code": "47894"
        },
        "county_subdivision": {
          "name": "Arlington",
          "fips": "90072",
          "fips_class": {
            "class_code": "Z7",
            "description": "A county subdivision that is coextensive with a county or equivalent feature or all or part of an incorporated place that the Census Bureau recognizes separately"
          }
        },
        "source": "US Census Bureau"
      },
      "2025": {
        "census_year": 2025,
        "state_fips": "51",
        "county_fips": "51013",
        "tract_code": "101801",
        "block_code": "2004",
        "block_group": "2",
        "full_fips": "510131018012004",
        "place": {
          "name": "Arlington",
          "fips": "5103000"
        },
        "metro_micro_statistical_area": {
          "name": "Washington-Arlington-Alexandria, DC-VA-MD-WV",
          "area_code": "47900",
          "type": "metropolitan"
        },
        "combined_statistical_area": {
          "name": "Washington-Baltimore-Arlington, DC-MD-VA-WV-PA",
          "area_code": "548"
        },
        "metropolitan_division": {
          "name": "Arlington-Alexandria-Reston, VA-WV",
          "area_code": "11694"
        },
        "county_subdivision": {
          "name": "Arlington",
          "fips": "90072",
          "fips_class": {
            "class_code": "Z7",
            "description": "A county subdivision that is coextensive with a county or equivalent feature or all or part of an incorporated place that the Census Bureau recognizes separately"
          }
        },
        "source": "US Census Bureau"
      }
    }
  }
}
```

## Core Census Fields

| Field | Description |
|---|---|
| `census_year` | The full year the Census data belongs to |
| `state_fips` | Two-digit state FIPS code |
| `county_fips` | Five-digit county FIPS code (first two digits are the state) |
| `tract_code` | Six-digit census tract code (subdivision of a county) |
| `block_code` | Four-digit census block code (smallest geographic unit with Census data) |
| `block_group` | Single-digit block group number |
| `full_fips` | Full 15-digit FIPS code (county FIPS + tract code + block code) |

## Place

Returned for locations within a Census-designated place. Returns `null` if the location is not in a Census-designated place.

| Field | Description |
|---|---|
| `name` | Official Census-designated name for the place |
| `fips` | Seven-digit place FIPS code |

## Metropolitan/Micropolitan Statistical Area (MSA)

Returned for locations within an MSA area. Returns `null` if no MSA is associated.

| Field | Description |
|---|---|
| `name` | Official Census-designated name |
| `area_code` | Unique area code (CBSA code) |
| `type` | `"metropolitan"` or `"micropolitan"` |

## Combined Statistical Area (CSA)

Returned for locations within a CSA. Returns `null` if no CSA is associated.

| Field | Description |
|---|---|
| `name` | Official Census-designated name |
| `area_code` | Unique census-defined code |

## Metropolitan Division (METDIV)

Returned for locations within a Metropolitan Division (introduced in 2003 to further split larger MSAs). Returns `null` if none is associated.

| Field | Description |
|---|---|
| `name` | Official Census-designated name |
| `area_code` | Unique census-defined code |

## County Subdivision

Depending on the state, this is either a Minor Civil Division (MCD) or Census County Division (CCD).

| Field | Description |
|---|---|
| `name` | Name of the county subdivision (city/town/township name or district number) |
| `fips` | Unique census-defined code |
| `fips_class` | Contains `class_code` and `description` for the given class code |

## Vintage Year Behavior

- `census` (no year) defaults to the most recent Census year. Currently returns **2025** data.
- Vintage geographies are available for every year back to 2010 (e.g., `census2015`).
- `census2000` provides County, Place, Tract, and Block FIPS codes only.
- Multiple years can be requested simultaneously (e.g., `fields=census2010,census`).

## Notes

Using Census tracts and blocks, you can match addresses with statistical data from the US Census Bureau, including the American Community Survey (ACS).

For Canadian Census data, see the `statcan` field append.
