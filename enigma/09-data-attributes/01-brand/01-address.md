# Address

## Description
A physical street address for the business, conforming to USPS Publication 28 standards.

## Tier
Core

## Fields

| Field | Type | Description |
|-------|------|-------------|
| streetAddress1 | String | Primary street address line |
| streetAddress2 | String | Secondary street address line (apt, suite, etc.) |
| city | String | City name |
| county | String | County name |
| state | String | State abbreviation |
| zip | String | ZIP code |
| country | String | Country |
| csa | String | Combined Statistical Area |
| msa | String | Metropolitan Statistical Area |
| latitude | Float | Latitude coordinate |
| longitude | Float | Longitude coordinate |
| h3Index | String | H3 geospatial index |
| fullAddress | String | Complete formatted address |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/address
