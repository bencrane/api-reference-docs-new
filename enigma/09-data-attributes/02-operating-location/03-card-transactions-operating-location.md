# Card Transactions (Operating Location)

## Description
Contains quantitative information about the card transactions processed by the operating location.

## Tier
Plus

## Applies To
- Operating Location

## Data Source
Panel of around a third of all U.S. credit and debit card transactions.

## Quantity Types
- Transaction counts
- Revenue amounts
- Average transaction size
- Refunds
- Customer counts
- Year-over-year growth metrics

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| period | String | Time span indicator (1m, 3m, or 12m) |
| periodStartDate | String | Period start date |
| periodEndDate | String | Period end date |
| rawQuantity | Number | Unscaled measurement values |
| projectedQuantity | Number | Scaled estimates accounting for panel gaps |
| quantityType | String | Metric type (8 options available) |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Key Details
Projected quantity scales raw data by a multiplier based on features of the location (geography, industry, size) that are predictive of the proportion of transactions the panel includes.

## Source
https://documentation.enigma.com/reference/attributes/operating-location-card-transaction
