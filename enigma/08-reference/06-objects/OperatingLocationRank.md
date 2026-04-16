# OperatingLocationRank

## Overview

Indicates how the card revenue of this operating location compares to other operating locations within the same Enigma industry and geographic area. For instance, a position of 5 out of 17 means four nearby pizza restaurants have higher card revenue and twelve have lower card revenue. The geographic area is determined by H3 index (resolution 4). An operating location may lack a rank if card revenue cannot be determined or fewer than ten nearby businesses in the same industry exist.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | First observation date |
| `lastObservedDate` | `String` | — | Most recent observation date |
| `quantityType` | `String` | — | Quantity metric used for ranking (currently card_revenue) |
| `period` | `String` | — | Period used for ranking (currently 12m) |
| `position` | `Int` | — | Absolute position relative to cohort |
| `cohortSize` | `Int` | — | Number of operating locations in cohort |
| `periodStartDate` | `Date` | — | Period commencement date |
| `periodEndDate` | `Date` | — | Period conclusion date |
| `internalId` | `String` | — | Internal identifier |
| `internalOperatingLocationId` | `String` | — | Internal operating location identifier |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count function |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Existence check function |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum function |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum function |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum function |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average function |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collection function |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime function |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime function |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `OperatingLocationRankEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `OperatingLocationRankConnection`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-rank
