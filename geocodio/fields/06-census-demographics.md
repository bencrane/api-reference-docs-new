# Census: Demographics (ACS) | Geocodio API

**Field name:** `acs-demographics`

**Coverage:** US only

Returns demographic data from the American Community Survey including population by age, sex, race, and ethnicity.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=acs-demographics&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=acs-demographics&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "census": { ... },
    "acs": {
      "meta": {
        "source": "American Community Survey from the US Census Bureau",
        "survey_years": "2020-2024",
        "survey_duration_years": "5"
      },
      "demographics": {
        "Median age": {
          "meta": {
            "table_id": "B01002",
            "universe": "Total population"
          },
          "Total": { "value": 34, "margin_of_error": 2.6 },
          "Male": { "value": 36.2, "margin_of_error": 4.3 },
          "Female": { "value": 33.3, "margin_of_error": 1.3 }
        },
        "Population by age range": {
          "meta": {
            "table_id": "B01001",
            "universe": "Total population"
          },
          "Total": { "value": 1554, "margin_of_error": 291 },
          "Male": { "value": 775, "margin_of_error": 170, "percentage": 0.499 },
          "Male: Under 5 years": { "value": 35, "margin_of_error": 31, "percentage": 0.045 },
          "Male: 5 to 9 years": { "value": 3, "margin_of_error": 6, "percentage": 0.004 },
          "Male: 10 to 14 years": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "...": "...",
          "Female": { "value": 779, "margin_of_error": 161, "percentage": 0.501 },
          "Female: Under 5 years": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "...": "..."
        },
        "Sex": {
          "meta": {
            "table_id": "B01001",
            "universe": "Total population"
          },
          "Total": { "value": 1554, "margin_of_error": 291 },
          "Male": { "value": 775, "margin_of_error": 170, "percentage": 0.499 },
          "Female": { "value": 779, "margin_of_error": 161, "percentage": 0.501 }
        },
        "Race and ethnicity": {
          "meta": {
            "table_id": "B03002",
            "universe": "Total population"
          },
          "Total": { "value": 1554, "margin_of_error": 291 },
          "Not Hispanic or Latino": { "value": 1478, "margin_of_error": 295, "percentage": 0.951 },
          "Not Hispanic or Latino: White alone": { "value": 1116, "margin_of_error": 225, "percentage": 0.755 },
          "Not Hispanic or Latino: Black or African American alone": { "value": 44, "margin_of_error": 54, "percentage": 0.03 },
          "Not Hispanic or Latino: Asian alone": { "value": 130, "margin_of_error": 95, "percentage": 0.088 },
          "...": "...",
          "Hispanic or Latino": { "value": 76, "margin_of_error": 45, "percentage": 0.049 },
          "Hispanic or Latino: White alone": { "value": 21, "margin_of_error": 23, "percentage": 0.276 },
          "...": "..."
        },
        "meta": {
          "geography": "block_group"
        }
      }
    }
  }
}
```

## Data Points Returned

### Median Age (Table B01002)

- Total, Male, Female

### Population by Age Range (Table B01001)

Broken out by Male and Female:

- Under 5 years, 5-9 years, 10-14 years, 15-17 years, 18-19 years, 20 years, 21 years, 22-24 years, 25-29 years, 30-34 years, 35-39 years, 40-44 years, 45-49 years, 50-54 years, 55-59 years, 60-64 years, 65-69 years, 70-74 years, 75-79 years, 80-84 years, 85 years and over

### Sex (Table B01001)

- Total, Male, Female

### Race and Ethnicity (Table B03002)

Broken out by Not Hispanic or Latino and Hispanic or Latino:

- White alone
- Black or African American alone
- American Indian and Alaska Native alone
- Asian alone
- Native Hawaiian and Other Pacific Islander alone
- Some other race alone
- Two or more races
- Two or more races: Two races including Some other race
- Two or more races: Two races excluding Some other race, and three or more races

## Data Format

Each data point includes `value`, `margin_of_error`, and `percentage` (where applicable). The percentage is calculated by Geocodio to aid ease of use. All other data is provided exactly as packaged by the Census Bureau.

## Notes

The `census` field data (FIPS codes, block/tract info) is automatically included with ACS responses at no extra charge. The categories for age, sex, gender, race, and ethnicity are returned exactly as the Census Bureau provides them.
