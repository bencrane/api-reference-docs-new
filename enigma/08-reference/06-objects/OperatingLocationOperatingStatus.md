# OperatingLocationOperatingStatus

## Overview

Indicates whether a location is actively functioning ("Open"), out of operation ("Temporarily Closed", "Closed"), or of uncertain status ("Unknown"). The system maintains this as a time series where each entry represents an unbroken period with the same operating status.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `operatingStatus` | `String` | None | Operational state of the brand at this address during the time period shown: Open, Closed, Temporarily Closed, or Unknown |
| `id` | `UUID!` | None | Unique identifier |
| `firstObservedDate` | `String` | None | Beginning of the observation period |
| `lastObservedDate` | `String` | None | End of the observation period |
| `internalId` | `String` | None | Internal identifier |
| `internalOperatingLocationId` | `String` | None | Internal operating location identifier |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count of records matching field and conditions |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Count of distinct values |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Checks if field exists under conditions |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum of field values |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum field value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum field value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average of field values |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collects field values into a string |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime value |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime value |
| `_fn` | `JSON` | None | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `OperatingLocationOperatingStatusEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `OperatingLocation`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-operating-status
