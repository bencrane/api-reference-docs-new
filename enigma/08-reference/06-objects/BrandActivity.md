# BrandActivity GraphQL Object Documentation

## Overview

The `BrandActivity` object identifies businesses engaged in high-compliance-risk activities within Enigma's KYB system.

## Description

"Identifies businesses that engage in activities with a high compliance risk."

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | `UUID!` | Unique identifier for the activity record |
| `firstObservedDate` | `String` | Initial detection date of the high-risk activity |
| `lastObservedDate` | `String` | Most recent observation date |
| `activityType` | `String` | Classification category (see High-Risk Categories below) |
| `internalId` | `String` | Internal system identifier |
| `internalBrandId` | `String` | Internal brand reference identifier |

## Aggregation Functions

The object implements `NodeFunctions` interface, providing:
- `count(field, conditions)` - Count matching records
- `countDistinct(field, conditions)` - Count unique values
- `has(field, conditions)` - Boolean field existence check
- `sum(field, conditions)` - Sum numeric values
- `min/max(field, conditions)` - Minimum/maximum values
- `avg(field, conditions)` - Calculate averages
- `collect(field, separator, conditions)` - Aggregate values
- `minDateTime/maxDateTime(field, conditions)` - Temporal aggregations

## High-Risk Activity Categories

The system classifies businesses into 13 risk categories:

1. **Cannabis** - Retailers, growers, distributors, and software providers
2. **Tobacco and Vaping** - Cigarettes, cigars, e-cigarette retailers
3. **Firearms, Weapons and Ammunition** - Gun retailers and shooting ranges
4. **Adult Entertainment and Dating** - Dating platforms, entertainment clubs, retail
5. **Gambling and Sports Betting** - Casinos, online betting, fantasy sports
6. **Payments and Money Transfer** - Payment processors, crowdfunding, lending services
7. **Multi-level Marketing** - MLM and pyramid schemes
8. **Pawn Shops, Check Cashing and Payday Loans**
9. **Cryptocurrencies and Digital Assets** - Wallets, exchanges, blockchain infrastructure
10. **Investments and Financing** - Brokers and lending instruments
11. **Legal Finance** - Collections and bail bonds
12. **Gift Cards** - Gift card retailers and resellers
13. **Health and Lifestyle** - Diet centers, supplements, non-FDA-regulated products
14. **Prescription Drugs** - Pharmacy operations

## Coverage & Data Sources

- **Scope**: Approximately 130K classified brands, including online-only businesses
- **Sources**: Derived from card transaction data, legal entity registrations, business names, and websites
- **Methodology**: Keyword analysis in industry descriptions, business names, and domain URLs (not website content analysis)

## Use Cases

The classification enhances automated customer onboarding by flagging businesses for manual review or additional risk assessment, ensuring compliance standards during onboarding workflows.
