# Census: Income / Economics (ACS) | Geocodio API

**Field name:** `acs-economics`

**Coverage:** US only

Returns economic and income data from the American Community Survey including median household income, household income distribution, and per capita income.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=acs-economics&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=acs-economics&api_key=YOUR_API_KEY"
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
      "economics": {
        "Number of households": {
          "meta": {
            "table_id": "B19001",
            "universe": "Households"
          },
          "Total": { "value": 887, "margin_of_error": 124 }
        },
        "Median household income": {
          "meta": {
            "table_id": "B19013",
            "universe": "Households"
          },
          "Total": { "value": 202344, "margin_of_error": 29891 }
        },
        "Household income": {
          "meta": {
            "table_id": "B19001",
            "universe": "Households"
          },
          "Less than $10,000": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$10,000 to $14,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$15,000 to $19,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$20,000 to $24,999": { "value": 7, "margin_of_error": 11, "percentage": 0.008 },
          "$25,000 to $29,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$30,000 to $34,999": { "value": 31, "margin_of_error": 51, "percentage": 0.035 },
          "$35,000 to $39,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$40,000 to $44,999": { "value": 8, "margin_of_error": 13, "percentage": 0.009 },
          "$45,000 to $49,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$50,000 to $59,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$60,000 to $74,999": { "value": 12, "margin_of_error": 16, "percentage": 0.014 },
          "$75,000 to $99,999": { "value": 59, "margin_of_error": 57, "percentage": 0.067 },
          "$100,000 to $124,999": { "value": 117, "margin_of_error": 63, "percentage": 0.132 },
          "$125,000 to $149,999": { "value": 56, "margin_of_error": 55, "percentage": 0.063 },
          "$150,000 to $199,999": { "value": 146, "margin_of_error": 83, "percentage": 0.165 },
          "$200,000 or more": { "value": 451, "margin_of_error": 98, "percentage": 0.508 }
        },
        "Per capita income": {
          "meta": {
            "table_id": "B19301",
            "universe": "Total population"
          },
          "Total": { "value": 153059, "margin_of_error": 34075 }
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

### Median Household Income (Table B19013)

Single value representing the median household income for the area.

### Household Income (Table B19001)

Distribution of households across income brackets:

- Less than $10,000
- $10,000 to $14,999
- $15,000 to $19,999
- $20,000 to $24,999
- $25,000 to $29,999
- $30,000 to $34,999
- $35,000 to $39,999
- $40,000 to $44,999
- $45,000 to $49,999
- $50,000 to $59,999
- $60,000 to $74,999
- $75,000 to $99,999
- $100,000 to $124,999
- $125,000 to $149,999
- $150,000 to $199,999
- $200,000 or more

### Per Capita Income (Table B19301)

Single value representing income per person.

## Data Format

Each data point includes `value`, `margin_of_error`, and `percentage` (where applicable). The percentage is calculated by Geocodio. All other data is provided exactly as packaged by the Census Bureau.

## Notes

The `census` field data (FIPS codes, block/tract info) is automatically included with ACS responses at no extra charge.
