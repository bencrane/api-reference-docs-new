# Census: Families / Households (ACS) | Geocodio API

**Field name:** `acs-families`

**Coverage:** US only

Returns household and family data from the American Community Survey including household types, marital status, family composition by presence of children, and average household size.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=acs-families&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=acs-families&api_key=YOUR_API_KEY"
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
      "families": {
        "Household type by household": {
          "meta": { "table_id": "B11001", "universe": "Households" },
          "Total": { "value": 887, "margin_of_error": 124 },
          "Family households": { "value": 345, "margin_of_error": 100, "percentage": 0.389 },
          "Family households: Married-couple family": { "value": 338, "margin_of_error": 101, "percentage": 0.98 },
          "Family households: Other family": { "value": 7, "margin_of_error": 13, "percentage": 0.02 },
          "Family households: Other family: Male householder, no spouse present": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Family households: Other family: Female householder, no spouse present": { "value": 7, "margin_of_error": 13, "percentage": 1 },
          "Nonfamily households": { "value": 542, "margin_of_error": 127, "percentage": 0.611 },
          "Nonfamily households: Householder living alone": { "value": 349, "margin_of_error": 84, "percentage": 0.644 },
          "Nonfamily households: Householder not living alone": { "value": 193, "margin_of_error": 96, "percentage": 0.356 }
        },
        "Household type by population": {
          "meta": { "table_id": "B11002", "universe": "Population in Households" },
          "Total": { "value": 1554, "margin_of_error": 291 },
          "In family households": { "value": 762, "margin_of_error": 220, "percentage": 0.49 },
          "In family households: In married-couple family": { "value": 746, "margin_of_error": 221, "percentage": 0.979 },
          "In family households: In married-couple family: Relatives": { "value": 746, "margin_of_error": 221, "percentage": 1 },
          "In family households: In married-couple family: Nonrelatives": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "...": "...",
          "In nonfamily households": { "value": 792, "margin_of_error": 270, "percentage": 0.51 }
        },
        "Marital status": {
          "meta": { "table_id": "B12001", "universe": "Population 15 Years And Older" },
          "Male": { "value": 737, "margin_of_error": 165, "percentage": 0.504 },
          "Male: Never married": { "value": 354, "margin_of_error": 160, "percentage": 0.48 },
          "Male: Now married": { "value": 375, "margin_of_error": 108, "percentage": 0.509 },
          "Male: Now married: Married, spouse present": { "value": 340, "margin_of_error": 101, "percentage": 0.907 },
          "Male: Now married: Married, spouse absent": { "value": 35, "margin_of_error": 44, "percentage": 0.093 },
          "Male: Widowed": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: Divorced": { "value": 8, "margin_of_error": 9, "percentage": 0.011 },
          "Female": { "value": 725, "margin_of_error": 143, "percentage": 0.496 },
          "Female: Never married": { "value": 359, "margin_of_error": 134, "percentage": 0.495 },
          "Female: Now married": { "value": 317, "margin_of_error": 89, "percentage": 0.437 },
          "Female: Widowed": { "value": 8, "margin_of_error": 13, "percentage": 0.011 },
          "Female: Divorced": { "value": 41, "margin_of_error": 31, "percentage": 0.057 }
        },
        "Family Type by Presence and Age of Own Children Under 18 Years": {
          "meta": { "table_id": "B11003", "universe": "Families" },
          "Total": { "value": 345, "margin_of_error": 100 },
          "Married-couple family": { "value": 338, "margin_of_error": 101, "percentage": 0.98 },
          "Married-couple family: With own children of the householder under 18 years": { "value": 90, "margin_of_error": 60, "percentage": 0.266 },
          "...": "..."
        },
        "Average Household Size of Occupied Housing Units by Tenure": {
          "meta": { "table_id": "B25010", "universe": "Occupied housing units" },
          "Total": { "value": 1.75, "margin_of_error": 0.17 },
          "Owner occupied": { "value": 1.81, "margin_of_error": 0.24 },
          "Renter occupied": { "value": 1.73, "margin_of_error": 0.22 }
        },
        "Own Children Under 18 Years by Family Type and Age": {
          "meta": { "table_id": "B09002", "universe": "Own children under 18 years" },
          "Total": { "value": 92, "margin_of_error": 64 },
          "In married-couple families": { "value": 92, "margin_of_error": 64, "percentage": 1 },
          "In married-couple families: Under 3 years": { "value": 35, "margin_of_error": 31, "percentage": 0.38 },
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

### Household Type by Household (Table B11001)

- Total
- Family households: Married-couple family, Other family (Male householder no spouse, Female householder no spouse)
- Nonfamily households: Householder living alone, Householder not living alone

### Household Type by Population (Table B11002)

- Total
- In family households: In married-couple family (Relatives, Nonrelatives), In male householder no spouse (Relatives, Nonrelatives), In female householder no spouse (Relatives, Nonrelatives)
- In nonfamily households

### Marital Status (Table B12001)

Broken out by Male and Female:

- Never married, Now married (spouse present, spouse absent, separated, other), Widowed, Divorced

### Family Type by Presence and Age of Own Children Under 18 Years (Table B11003)

- Married-couple family (with/without own children under 18, by age groups)
- Other family: Male householder no spouse (with/without children, by age groups)
- Other family: Female householder no spouse (with/without children, by age groups)

### Average Household Size of Occupied Housing Units by Tenure (Table B25010)

- Total, Owner occupied, Renter occupied

### Own Children Under 18 Years by Family Type and Age (Table B09002)

- In married-couple families (by age: under 3, 3-4, 5, 6-11, 12-17)
- In other families: Male householder (by age)
- In other families: Female householder (by age)

## Notes

The `census` field data is automatically included at no extra charge. All data is provided exactly as the Census Bureau packages it, with a `percentage` calculation added by Geocodio for ease of use.
