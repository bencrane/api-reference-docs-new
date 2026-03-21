# Address

## Description
A physical street address for the business, adhering to USPS Publication 28 standards where applicable.

## Tier
Core

## Applies To
- Brand
- Operating Location
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| streetAddress1 | String | Primary street address line |
| streetAddress2 | String | Secondary address line (unit, suite, etc.) |
| fullAddress | String | Complete formatted address |
| city | String | City name |
| state | String | State abbreviation |
| zip | String | ZIP code |
| county | String | County name |
| country | String | Country (ISO3 code) |
| msa | String | Metropolitan/Micropolitan Statistical Area |
| csa | String | Combined Statistical Area |
| latitude | Float | Latitude coordinate |
| longitude | Float | Longitude coordinate |
| h3Index | String | Geo-hashing resolution 10 |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Key Details
Addresses can range from complete street addresses with unit numbers to postal codes or city/state combinations. Distinct units in the same building are listed separately when available.

## Source
https://documentation.enigma.com/reference/attributes/address
