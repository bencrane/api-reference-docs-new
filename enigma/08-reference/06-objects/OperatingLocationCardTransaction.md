# OperatingLocationCardTransaction

## Overview

Contains quantitative information about the card transactions processed by an operating location. The card transaction data derives from a panel representing approximately one-third of all U.S. credit and debit card transactions.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `quantityType` | `String` | — | Indicates the type of quantity represented (e.g., `avg_transaction_size`, `card_revenue_amount`, `card_transactions_count`, `card_customers_average_daily_count`, `card_revenue_yoy_growth`, `card_revenue_prior_period_growth`, `refunds_amount`, `has_transactions`) |
| `period` | `String` | — | Indicates the length of the time period: `1m` (one month), `3m` (three months), or `12m` (twelve months) |
| `id` | `UUID!` | — | Unique identifier for the card transaction record |
| `firstObservedDate` | `String` | — | Initial observation date of the card transaction data |
| `lastObservedDate` | `String` | — | Most recent observation date of the card transaction data |
| `rawQuantity` | `Float` | — | Raw value of the specified quantity type; may be null if underlying data falls below compliance thresholds |
| `projectedQuantity` | `Float` | — | Projected value scaled to estimate total card transactions; null under compliance thresholds |
| `periodStartDate` | `Date` | — | Beginning date of the reporting period |
| `periodEndDate` | `Date` | — | Ending date of the reporting period |
| `internalId` | `String` | — | Internal identifier |
| `internalOperatingLocationId` | `String` | — | Internal operating location identifier |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count aggregation function |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Existence check function |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation function |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value function |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value function |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average calculation function |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | String collection function |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime function |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime function |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `OperatingLocationCardTransactionEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-card-transaction
