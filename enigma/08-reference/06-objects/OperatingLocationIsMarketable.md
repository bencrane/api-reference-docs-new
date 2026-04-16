# OperatingLocationIsMarketable

## Overview

Represents a boolean value indicating whether an operating location qualifies as marketable. An operating location is considered marketable if it meets specific criteria, including maintaining an open status with recent data, demonstrating revenue activity within the last 12 months, or having received reviews within the last 12 months.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier for the record |
| `firstObservedDate` | `String` | — | Initial observation timestamp |
| `lastObservedDate` | `String` | — | Most recent observation timestamp |
| `isMarketable` | `Boolean` | — | Boolean indicator of marketability status |
| `internalId` | `String` | — | Internal identifier reference |
| `internalOperatingLocationId` | `String` | — | Operating location internal identifier |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregate function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Count distinct values |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregate function |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value function |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value function |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value function |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect values as string |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime value |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime value |
| `_fn` | `JSON` | — | Extended function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `OperatingLocationIsMarketableEdge`
- **Member of Connection(s):** `OperatingLocationIsMarketableConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-is-marketable
