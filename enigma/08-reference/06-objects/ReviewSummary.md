# ReviewSummary

## Overview

Summary of publicly available customer reviews for this entity. This is a time series where rank 0 represents the most recent review summary, with higher ranks representing earlier periods. The data is sourced from actual customer reviews about business locations that are publicly available and updated at least monthly.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | Initial observation date |
| `lastObservedDate` | `String` | — | Most recent observation date |
| `reviewCount` | `String` | — | Number of reviews submitted for a location |
| `reviewScoreAvg` | `String` | — | Weighted average rating of all reviews for a location |
| `firstReviewDate` | `Date` | — | Date of earliest available review (from sample of 100) |
| `lastReviewDate` | `Date` | — | Date of latest available review; may lag up to 3 months |
| `internalId` | `String` | — | Internal identifier |
| `internalReviewSummaryId` | `String` | — | Internal review summary identifier |
| `operatingLocations` | `ReviewSummaryOperatingLocationConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Associated operating locations |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count aggregation |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect values with separator |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime |
| `_fn` | `JSON` | — | Internal function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `OperatingLocationReviewSummaryEdge`
- **Member of Connection(s):** `ReviewSummaryOperatingLocationConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `OperatingLocation`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/review-summary
