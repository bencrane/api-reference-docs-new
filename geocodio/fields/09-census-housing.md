# Census: Housing (ACS) | Geocodio API

**Field name:** `acs-housing`

**Coverage:** US only

Returns housing data from the American Community Survey including occupancy status, ownership, units in structure, and home values.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=acs-housing&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=acs-housing&api_key=YOUR_API_KEY"
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
      "housing": {
        "Number of housing units": {
          "meta": { "table_id": "B25002", "universe": "Housing Units" },
          "Total": { "value": 1000, "margin_of_error": 135 }
        },
        "Occupancy status": {
          "meta": { "table_id": "B25002", "universe": "Housing Units" },
          "Occupied": { "value": 887, "margin_of_error": 124, "percentage": 0.887 },
          "Vacant": { "value": 113, "margin_of_error": 74, "percentage": 0.113 }
        },
        "Ownership of occupied units": {
          "meta": { "table_id": "B25003", "universe": "Occupied Housing Units" },
          "Owner occupied": { "value": 235, "margin_of_error": 79, "percentage": 0.265 },
          "Renter occupied": { "value": 652, "margin_of_error": 117, "percentage": 0.735 }
        },
        "Units in structure": {
          "meta": { "table_id": "B25024", "universe": "Housing Units" },
          "1, detached unit": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "1, attached unit": { "value": 142, "margin_of_error": 59, "percentage": 0.142 },
          "2 units": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "3 or 4 units": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "5 to 9 units": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "10 to 19 unit": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "20 to 49 units": { "value": 10, "margin_of_error": 16, "percentage": 0.01 },
          "50 or more units": { "value": 848, "margin_of_error": 139, "percentage": 0.848 },
          "Mobile home units": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "Boat, RV, van, etc. units": { "value": 0, "margin_of_error": 13, "percentage": 0 }
        },
        "Median value of owner-occupied housing units": {
          "meta": { "table_id": "B25077", "universe": "Owner-Occupied Housing Units" },
          "Total": { "value": 803600, "margin_of_error": 173895 }
        },
        "Value of owner-occupied housing units": {
          "meta": { "table_id": "B25075", "universe": "Owner-Occupied Housing Units" },
          "Less than $10,000": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$10,000 to $14,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$15,000 to $19,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$20,000 to $24,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$25,000 to $29,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$30,000 to $34,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$35,000 to $39,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$40,000 to $49,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$50,000 to $59,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$60,000 to $69,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$70,000 to $79,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$80,000 to $89,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$90,000 to $99,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$100,000 to $124,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$125,000 to $149,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$150,000 to $174,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$175,000 to $199,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$200,000 to $249,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$250,000 to $299,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$300,000 to $399,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$400,000 to $499,999": { "value": 0, "margin_of_error": 13, "percentage": 0 },
          "$500,000 to $749,999": { "value": 107, "margin_of_error": 59, "percentage": 0.455 },
          "$750,000 to $999,999": { "value": 49, "margin_of_error": 49, "percentage": 0.209 },
          "$1,000,000 to $1,499,999": { "value": 76, "margin_of_error": 43, "percentage": 0.323 },
          "$1,500,000 to $1,999,999": { "value": 3, "margin_of_error": 5, "percentage": 0.013 },
          "$2,000,000 or more": { "value": 0, "margin_of_error": 13, "percentage": 0 }
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

### Number of Housing Units (Table B25002)

Total count of housing units in the area.

### Occupancy Status (Table B25002)

- Occupied
- Vacant

### Ownership of Occupied Units (Table B25003)

- Owner occupied
- Renter occupied

### Units in Structure (Table B25024)

- 1, detached unit
- 1, attached unit
- 2 units
- 3 or 4 units
- 5 to 9 units
- 10 to 19 units
- 20 to 49 units
- 50 or more units
- Mobile home units
- Boat, RV, van, etc. units

### Median Value of Owner-Occupied Housing Units (Table B25077)

Single median value for owner-occupied housing.

### Value of Owner-Occupied Housing Units (Table B25075)

Distribution across 25 value brackets from less than $10,000 to $2,000,000 or more.

## Notes

The `census` field data is automatically included at no extra charge. All data is provided exactly as the Census Bureau packages it, with a `percentage` calculation added by Geocodio.
