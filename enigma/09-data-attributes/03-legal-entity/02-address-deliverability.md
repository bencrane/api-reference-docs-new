# Address Deliverability

## Description
The AddressDeliverability type represents USPS-compliant physical street address deliverability data for businesses, conforming to USPS Publication 28 standards.

## Tier
Plus

## Applies To
- Brand
- Operating Location
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier |
| rdi | String | Residential Delivery Indicator: "Residential" or "Commercial" |
| deliveryType | String | How mail reaches the address |
| deliverable | String | Deliverability status |
| virtual | String | Virtual address indicator |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Delivery Type Values
- Street address
- Multi-Tenant Building (apartment/unit subdivisions)
- Post Office Box
- Firm (internally redistributed mail)
- Rural Route or Highway Contract Route
- General Delivery (held at local post office)
- Null (insufficient information)

## Deliverable Status Values
- `deliverable` - Confirmed in USPS data, actively receiving mail
- `vacant` - In USPS records but unoccupied (typically 90+ days)
- `not_deliverable` - Temporarily marked undeliverable by USPS
- Null (insufficient data)

## Virtual Address Indicator
- `virtual_cmra` - Virtual address with valid Commercial Mail Receiving Agency
- `not_virtual` - Physical address without CMRA association
- Null (insufficient data)

## Source
https://documentation.enigma.com/reference/graphql_api/
