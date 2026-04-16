# OperatingLocationTechnologiesUsed

## Overview

This type indicates third-party technologies being used at a particular operating location. Technologies are determined by parsing merchant identifiers from credit card transaction data. The data is sourced from private vendors and independently verified for accuracy, currently covering payments-related technologies like Clover, PayPal, Shopify, Square, Stripe, and Toast.

The type maintains historical information through a rank property: Rank 0 reflects the most recent validated observation, while higher ranks represent older recorded usage periods, enabling visibility into technology changes over time.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| id | UUID! | — | Unique identifier |
| firstObservedDate | String | — | Date of first observation |
| lastObservedDate | String | — | Date of most recent observation |
| technology | String | — | "The specific third-party technology being used by the location" |
| category | String | — | "The category of the third-party technology being used by the location. An example would be payments" |
| internalId | String | — | Internal identifier |
| internalOperatingLocationId | String | — | Internal operating location identifier |
| count | Int | field: String!, conditions: Conditions | Aggregation function |
| countDistinct | Int | field: String!, conditions: Conditions | Aggregation function |
| has | Boolean | field: String!, conditions: Conditions | Check existence |
| sum | Int | field: String!, conditions: Conditions | Aggregation function |
| min | Int | field: String!, conditions: Conditions | Aggregation function |
| max | Int | field: String!, conditions: Conditions | Aggregation function |
| avg | Float | field: String!, conditions: Conditions | Aggregation function |
| collect | String | field: String!, separator: String, conditions: Conditions | Aggregation function |
| minDateTime | DateTime | field: String!, conditions: Conditions | Aggregation function |
| maxDateTime | DateTime | field: String!, conditions: Conditions | Aggregation function |
| _fn | JSON | — | Function metadata |

## Interfaces Implemented

- NodeFunctions

## Type Membership

- **Member of Edge(s):** OperatingLocationTechnologiesUsedEdge
- **Member of Connection(s):** None explicitly listed
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** OperatingLocationTechnologiesUsedConnection

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-technologies-used
