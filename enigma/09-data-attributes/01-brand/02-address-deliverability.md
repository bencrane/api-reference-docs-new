# Address Deliverability

## Description
Validation data indicating whether addresses are deliverable based on USPS delivery point validation data.

## Tier
Plus

## Fields

| Field | Type | Description |
|-------|------|-------------|
| deliverable | Boolean | Whether the address is deliverable |
| deliveryType | String | Type of delivery point |
| rdi | String | Residential Delivery Indicator |
| virtual | Boolean | CMRA (Commercial Mail Receiving Agency) indicator |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/address-deliverability
