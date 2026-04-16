# OperatingLocationName

## Overview

`OperatingLocationName` represents the name of an operating location, which is a place where business is conducted under a brand. These names are often distinct from brand names and may indicate something specific about that particular location.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `nameFullTextSearchVector` | `String` | — | Full-text search vector for the name |
| `name` | `String!` | — | "The name of the operating location" |
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | Date when the name was first observed |
| `lastObservedDate` | `String` | — | Date when the name was last observed |
| `internalId` | `String` | — | Internal identifier |
| `internalOperatingLocationId` | `String` | — | Internal operating location identifier |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count of records matching criteria |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Count of distinct values |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Check if field exists |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum of field values |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect values into string |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime value |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime value |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `OperatingLocationNameEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-name
