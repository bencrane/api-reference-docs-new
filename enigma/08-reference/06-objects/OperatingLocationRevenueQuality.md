# OperatingLocationRevenueQuality

## Overview
Warnings and issues related to the revenue of an operating location.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | Initial observation date |
| `lastObservedDate` | `String` | — | Most recent observation date |
| `issueReason` | `String` | — | Cause of the revenue quality issue (e.g., extrapolation thresholds, revenue anomalies, location status mismatches) |
| `issueSeverity` | `String` | — | Level of concern (HIGH or MEDIUM) |
| `issueDescription` | `String` | — | Explanation of the revenue quality issue |
| `internalId` | `String` | — | Internal system identifier |
| `internalOperatingLocationId` | `String` | — | Associated operating location internal ID |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Aggregate count function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct value count |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average calculation |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect values with separator |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented
- `NodeFunctions`

## Type Membership
- **Member of Edge(s):** OperatingLocationRevenueQualityEdge
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** OperatingLocation

## Source
https://documentation.enigma.com/reference/graphql_api/objects/operating-location-revenue-quality
