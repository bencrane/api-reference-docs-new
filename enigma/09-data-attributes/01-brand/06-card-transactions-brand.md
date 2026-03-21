# Card Transactions (Brand)

## Description
Quantitative card transaction data from approximately 1/3 of all U.S. credit/debit card transactions.

## Tier
Plus

## Metrics

### Transaction Metrics
- `avg_transaction_size` - Average transaction amount
- `has_transactions` - Boolean indicating transaction presence
- `refunds_amount` - Total refund amount
- `card_transactions_count` - Number of transactions
- `card_revenue_amount` - Total revenue from card transactions
- `card_customers_average_daily_count` - Average daily customer count
- `card_revenue_yoy_growth` - Year-over-year revenue growth
- `card_revenue_prior_period_growth` - Prior period revenue growth

### Time Periods
- 1m (1 month)
- 3m (3 months)
- 12m (12 months)

## Fields

| Field | Type | Description |
|-------|------|-------------|
| period | String | Time period (1m, 3m, 12m) |
| periodStartDate | String | Start date of the period |
| periodEndDate | String | End date of the period |
| quantityType | String | Type of metric |
| projectedQuantity | Number | Projected quantity value |
| platformBrandId | String | Platform brand identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/brand-card-transaction
