# FFIEC (Fair Lending) | Geocodio API

**Field name:** `ffiec`

**Coverage:** US only (Beta)

Returns FFIEC (Federal Financial Institutions Examination Council) data commonly used by financial institutions, lenders, and organizations for Fair Lending compliance with HMDA and CRA regulations.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=ffiec&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=ffiec&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "ffiec": {
      "collection_year": 2025,
      "msa_md_code": "11694",
      "fips_state_code": "51",
      "fips_county_code": "013",
      "census_tract": "101801",
      "principal_city": true,
      "small_county": {
        "flag": "T",
        "description": "Tract record"
      },
      "split_tract": {
        "flag": "N",
        "description": "Tract number occurs within one MA"
      },
      "demographic_data": {
        "flag": "D",
        "description": "Total persons/population and median family income are not 0"
      },
      "urban_rural_flag": {
        "flag": "U",
        "description": "Urban"
      },
      "msa_md_median_family_income": 135790,
      "msa_md_median_household_income": 115805,
      "tract_median_family_income_percentage": 133.95,
      "ffiec_estimated_msa_md_median_family_income": 172700,
      "income_indicator": "Upper",
      "cra_poverty_criteria": false,
      "cra_unemployment_criteria": false,
      "cra_distressed_criteria": false,
      "cra_remote_rural_low_density_criteria": false,
      "previous_year_cra_distressed_criteria": false,
      "previous_year_cra_underserved_criterion": false,
      "meets_current_previous_criteria": false
    }
  }
}
```

## Response Fields

| Field | Description |
|---|---|
| `collection_year` | Data release year (currently 2025) |
| `msa_md_code` | MSA/MD (Metropolitan Statistical Area / Metropolitan Division) code |
| `fips_state_code` | Two-digit state FIPS code |
| `fips_county_code` | Three-digit county FIPS code |
| `census_tract` | Census tract code |
| `principal_city` | Whether the location is in a principal city |
| `small_county` | Small county flag and description |
| `split_tract` | Whether the tract number spans multiple metropolitan areas |
| `demographic_data` | Flag indicating availability of demographic data |
| `urban_rural_flag` | Urban or rural classification |
| `msa_md_median_family_income` | Median family income for the MSA/MD |
| `msa_md_median_household_income` | Median household income for the MSA/MD |
| `tract_median_family_income_percentage` | Tract median family income as a percentage of the MSA/MD median |
| `ffiec_estimated_msa_md_median_family_income` | FFIEC estimated MSA/MD median family income |
| `income_indicator` | Income level classification (e.g., "Upper", "Middle", "Moderate", "Low") |
| `cra_poverty_criteria` | Whether the tract meets CRA poverty criteria |
| `cra_unemployment_criteria` | Whether the tract meets CRA unemployment criteria |
| `cra_distressed_criteria` | Whether the tract meets CRA distressed criteria |
| `cra_remote_rural_low_density_criteria` | Whether the tract meets CRA remote rural/low density criteria |
| `previous_year_cra_distressed_criteria` | Whether the tract met CRA distressed criteria in the previous year |
| `previous_year_cra_underserved_criterion` | Whether the tract met CRA underserved criteria in the previous year |
| `meets_current_previous_criteria` | Whether the tract meets current or previous year criteria |

## Notes

This field is currently in **beta**. For detailed information about the individual values, refer to the FFIEC Documentation.
