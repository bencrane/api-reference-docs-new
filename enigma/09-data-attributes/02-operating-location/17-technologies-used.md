# Technologies Used

## Description
Third-party technologies being used at a particular operating location.

## Tier
Premium

## Applies To
- Operating Location

## Historical Tracking
- **Rank 0** = Most recent validated observation
- **Higher ranks** = Older usage periods

## Data Source
Parsing merchant identifiers from credit card transaction data via independently verified private vendors.

## Currently Identified Technologies
Payments-related only:
- Clover
- PayPal
- Shopify
- Square
- Stripe
- Toast

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| technology | String | Specific third-party tool used |
| category | String | Technology category (e.g., "payments") |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/operating-location-technologies-used
