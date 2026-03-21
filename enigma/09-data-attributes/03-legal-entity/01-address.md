# Address

## Description
The Addresses attribute represents the physical location(s) linked to a business or business location. Conforms to USPS Publication 28 standards.

## Tier
Core

## Applies To
- Brand
- Operating Location
- Legal Entity

## Address Types
- site
- registered
- mailing
- registered_agent_address
- registered_business_address

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| fullAddress | String | Complete address without punctuation |
| streetAddress1 | String | Primary street information (e.g., "245 5th Avenue") |
| streetAddress2 | String | Secondary details like suite, floor (e.g., "Fl 17") |
| city | String | Municipality |
| state | String | US state code |
| zip | String | ZIP code |
| county | String | County name |
| msa | String | Metropolitan/Micropolitan Statistical Area |
| csa | String | Combined Statistical Area |
| country | String | Three-digit ISO3 country code |
| type | String | Address classification |
| latitude | Float | Approximate decimal coordinates |
| longitude | Float | Approximate decimal coordinates |
| h3Index | String | H3 geohashing index at resolution 10 |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Coverage
- Businesses: 97%
- Business Locations: 100%

## Data Sources
- Credit/debit card transaction panel (40% of US transactions)
- Corporate registration records

## Key Notes
- Variations of the same address are resolved to the single, most granular address available
- Can be up to 10 addresses per registration
- Nine states (AL, DE, MS, NJ, NV, OH, OK, SC, WI) don't provide mailing addresses on registrations

## Sources
- https://developers.enigma.com/docs/addresses
- https://documentation.enigma.com/reference/graphql_api/objects/address
