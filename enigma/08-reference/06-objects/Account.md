# Account GraphQL Object Type

## Overview

The `Account` object represents user account information within the Enigma GraphQL API, including billing and subscription management details.

## Type Definition

```graphql
type Account {
  customerId: ID
  customerEmail: String
  billingAccountId: ID
  pricingPlan: String
  creditsAvailable: Boolean
  autoRenewEnabled: Boolean
  autoRechargeDesiredState: Boolean
  autoRechargeCurrentState: Boolean
  autoRechargeThresholdAmount: Int
  autoRechargeRechargeToAmount: Int
  autoRechargeLimitUsd: Int
  autoRechargeReenableAfterTimestamp: String
}
```

## Fields

| Field | Type | Purpose |
|-------|------|---------|
| `customerId` | `ID` | Unique identifier for the customer |
| `customerEmail` | `String` | Email address associated with the account |
| `billingAccountId` | `ID` | Identifier for the billing account |
| `pricingPlan` | `String` | Current pricing plan tier |
| `creditsAvailable` | `Boolean` | Indicates credit availability status |
| `autoRenewEnabled` | `Boolean` | Whether automatic renewal is active |
| `autoRechargeDesiredState` | `Boolean` | Target state for auto-recharge feature |
| `autoRechargeCurrentState` | `Boolean` | Current state of auto-recharge functionality |
| `autoRechargeThresholdAmount` | `Int` | Credit level triggering automatic recharge |
| `autoRechargeRechargeToAmount` | `Int` | Target credit amount after recharge |
| `autoRechargeLimitUsd` | `Int` | Maximum USD spend limit for auto-recharge |
| `autoRechargeReenableAfterTimestamp` | `String` | When auto-recharge can be re-enabled |

## Returned By

- [`account`](/reference/graphql_api/queries/account) query
