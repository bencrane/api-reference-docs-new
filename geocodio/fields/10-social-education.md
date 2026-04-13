# Census: Social -- Education & Veteran Status (ACS) | Geocodio API

**Field name:** `acs-social`

**Coverage:** US only

Returns education attainment and veteran status data from the American Community Survey.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=acs-social&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=acs-social&api_key=YOUR_API_KEY"
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
      "social": {
        "Population by minimum level of education": {
          "meta": { "table_id": "B15002", "universe": "Population 25 Years And Over" },
          "Total": { "value": 1315, "margin_of_error": 178 },
          "Male": { "value": 675, "margin_of_error": 125, "percentage": 0.513 },
          "Male: No schooling completed": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: Nursery to 4th grade": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: 5th and 6th grade": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: 7th and 8th grade": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: 9th grade": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: 10th grade": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: 11th grade": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: 12th grade, no diploma": { "value": 6, "margin_of_error": 10, "percentage": 0.009 },
          "Male: High school graduate (includes equivalency)": { "value": 8, "margin_of_error": 15, "percentage": 0.012 },
          "Male: Some college, less than 1 year": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: Some college, 1 or more years, no degree": { "value": 24, "margin_of_error": 28, "percentage": 0.036 },
          "Male: Associate's degree": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Male: Bachelor's degree": { "value": 277, "margin_of_error": 87, "percentage": 0.41 },
          "Male: Master's degree": { "value": 254, "margin_of_error": 101, "percentage": 0.376 },
          "Male: Professional school degree": { "value": 69, "margin_of_error": 55, "percentage": 0.102 },
          "Male: Doctorate degree": { "value": 37, "margin_of_error": 46, "percentage": 0.055 },
          "Female": { "value": 640, "margin_of_error": 102, "percentage": 0.487 },
          "Female: No schooling completed": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "...": "..."
        },
        "Population with veteran status": {
          "meta": { "table_id": "B21001", "universe": "Civilian Population 18 Years And Over" },
          "Total": { "value": 1400, "margin_of_error": 288 },
          "Veteran": { "value": 74, "margin_of_error": 50, "percentage": 0.053 },
          "Nonveteran": { "value": 1326, "margin_of_error": 291, "percentage": 0.947 },
          "Male": { "value": 682, "margin_of_error": 175, "percentage": 0.487 },
          "Male: Veteran": { "value": 74, "margin_of_error": 50, "percentage": 0.109 },
          "Male: Nonveteran": { "value": 608, "margin_of_error": 179, "percentage": 0.891 },
          "Male: 18 to 34 years": { "value": 303, "margin_of_error": 154, "percentage": 0.444 },
          "Male: 18 to 34 years: Veteran": { "value": 26, "margin_of_error": 30, "percentage": 0.086 },
          "Male: 18 to 34 years: Nonveteran": { "value": 277, "margin_of_error": 157, "percentage": 0.914 },
          "...": "...",
          "Female": { "value": 718, "margin_of_error": 143, "percentage": 0.513 },
          "Female: Veteran": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Female: Nonveteran": { "value": 718, "margin_of_error": 143, "percentage": 1 },
          "...": "..."
        },
        "Period of military service for veterans": {
          "meta": { "table_id": "B21002", "universe": "Civilian Veterans 18 Years And Over" },
          "Total": { "value": 74, "margin_of_error": 50 },
          "Gulf War (9/2001 or later), no Gulf War (8/1990 to 8/2001), no Vietnam War": { "value": 57, "margin_of_error": 45, "percentage": 0.77 },
          "Gulf War (9/2001 or later) and Gulf War (8/1990 to 8/2001), no Vietnam War": { "value": 14, "margin_of_error": 23, "percentage": 0.189 },
          "Gulf War (8/1990 to 8/2001), no Vietnam War": { "value": 3, "margin_of_error": 5, "percentage": 0.041 },
          "Gulf War (8/1990 to 8/2001) and Vietnam War": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Vietnam War, no Korean War, no World War II": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Vietnam War and Korean War, no World War II": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Vietnam War and Korean War and World War II": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Korean War, no Vietnam War, no World War II": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Korean War and World War II, no Vietnam War": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "World War II, no Korean War, no Vietnam War": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Between Gulf War and Vietnam War only": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Between Vietnam War and Korean War only": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Between Korean War and World War II only": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Pre-World War II only": { "value": 0, "margin_of_error": 13, "percentage": 0 }
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

### Population by Minimum Level of Education (Table B15002)

Broken out by Male and Female:

- No schooling completed
- Nursery to 4th grade
- 5th and 6th grade
- 7th and 8th grade
- 9th grade
- 10th grade
- 11th grade
- 12th grade, no diploma
- High school graduate (includes equivalency)
- Some college, less than 1 year
- Some college, 1 or more years, no degree
- Associate's degree
- Bachelor's degree
- Master's degree
- Professional school degree
- Doctorate degree

### Population with Veteran Status (Table B21001)

Broken out by Male and Female, and by age groups (18-34, 35-54, 55-64, 65-74, 75+):

- Veteran
- Nonveteran

### Period of Military Service for Veterans (Table B21002)

- Gulf War (9/2001 or later), no Gulf War (8/1990 to 8/2001), no Vietnam War
- Gulf War (9/2001 or later) and Gulf War (8/1990 to 8/2001), no Vietnam War
- Gulf War (9/2001 or later), and Gulf War (8/1990 to 8/2001), and Vietnam War
- Gulf War (8/1990 to 8/2001), no Vietnam War
- Gulf War (8/1990 to 8/2001) and Vietnam War
- Vietnam War, no Korean War, no World War II
- Vietnam War and Korean War, no World War II
- Vietnam War and Korean War and World War II
- Korean War, no Vietnam War, no World War II
- Korean War and World War II, no Vietnam War
- World War II, no Korean War, no Vietnam War
- Between Gulf War and Vietnam War only
- Between Korean War and World War II only
- Pre-World War II only

## Notes

The `census` field data is automatically included at no extra charge. All data is provided exactly as the Census Bureau packages it, with a `percentage` calculation added by Geocodio.
