# BrandCardTransaction

## Overview

The `BrandCardTransaction` object provides quantitative information about card transactions processed by a brand, derived from a panel representing approximately one-third of all U.S. credit and debit card transactions.

## Fields

### quantityType: String
Indicates the category of quantity represented in the record. Valid values include:
- `avg_transaction_size`: Average transaction value in dollars
- `has_transactions`: Binary indicator (1 if transactions occurred, 0 otherwise)
- `refunds_amount`: Total refund dollars for the period
- `card_transactions_count`: Total number of card transactions
- `card_revenue_amount`: Total sales amount in dollars
- `card_customers_average_daily_count`: Mean unique daily customer count
- `card_revenue_yoy_growth`: Year-over-year revenue ratio
- `card_revenue_prior_period_growth`: Sequential period revenue ratio

### period: String
Specifies the time period duration. Options are:
- `1m`: One month
- `3m`: Three months
- `12m`: Twelve months

### projectedQuantity: Float
The numerical value for the specified quantity type. May be null when underlying transaction volumes fall below compliance thresholds (except for "has_transactions").

### platformBrandId: UUID
The brand identifier for the payment platform that processed the transaction. Null indicates the quantity is not attributed to a specific platform.

### id: UUID! (non-null)
Unique identifier for the record.

### periodStartDate: Date
The beginning date of the reported time period.

### periodEndDate: Date
The ending date of the reported time period.

### firstObservedDate: String
Date when the record was first detected.

### lastObservedDate: String
Date of the most recent observation.

### internalId: String
Internal system identifier.

### internalBrandId: String
Internal brand reference number.

### internalPlatformBrandId: String
Internal platform brand reference number.

## Aggregate Functions

The object implements `NodeFunctions` interface, providing:
- `count(field, conditions)`: Record count
- `countDistinct(field, conditions)`: Unique value count
- `has(field, conditions)`: Field presence check
- `sum(field, conditions)`: Numeric summation
- `min(field, conditions)` / `max(field, conditions)`: Extrema
- `avg(field, conditions)`: Numeric average
- `collect(field, separator, conditions)`: Value concatenation
- `minDateTime(field, conditions)` / `maxDateTime(field, conditions)`: Temporal extrema
