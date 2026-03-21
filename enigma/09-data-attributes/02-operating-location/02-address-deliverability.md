# Address Deliverability

## Description
Validates physical business addresses using USPS standards (Publication 28).

## Tier
Plus

## Applies To
- Brand
- Operating Location
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| deliverable | Boolean | Whether the address is deliverable based on USPS data |
| deliveryType | String | Mail delivery method for the address |
| rdi | String | Residential Delivery Indicator (Residential/Commercial) |
| virtual | Boolean | CMRA (Commercial Mail Receiving Agency) indicator |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Key Details
Distinguishes between complete street addresses with units and broader geographic identifiers like postal codes or city/state combinations.

## Source
https://documentation.enigma.com/reference/attributes/address-deliverability
