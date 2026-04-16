# WatchlistEntry

## Overview

Watchlist entities draw from OFAC publications including the Specially Designated Nationals and Blocked Persons List (SDN) and Consolidated Sanctions List (Non-SDN), which encompasses the Foreign Sanctions Evaders List, Sectoral Sanctions Identifications List, Palestinian Legislative Council List, and related sanctions lists.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `watchlistName` | `String` | — | Name of the watchlist, including SDN and Non-SDN |
| `firstObservedDate` | `String` | — | Date when entry was first observed |
| `lastObservedDate` | `String` | — | Date when entry was last observed |
| `internalId` | `String` | — | Internal identifier |
| `internalWatchlistEntryId` | `String` | — | Internal watchlist entry identifier |
| `legalEntitiesIsFlaggedBy` | `WatchlistEntryIsFlaggedByLegalEntityConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Legal entities flagged by this entry |
| `legalEntitiesAppearsOn` | `WatchlistEntryAppearsOnLegalEntityConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Legal entities this entry appears on |
| `addresses` | `WatchlistEntryAddressConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Associated addresses |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count aggregation |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation function |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum aggregation function |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum aggregation function |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average aggregation function |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect field values |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime aggregation |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime aggregation |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `AddressWatchlistEntryEdge`, `LegalEntityAppearsOnWatchlistEntryEdge`, `LegalEntityIsFlaggedByWatchlistEntryEdge`
- **Member of Connection(s):** None directly listed
- **Member of Union(s):** None
- **Referenced by Input(s):** None listed
- **Referenced by Object(s):** Multiple connection types

## Source

https://documentation.enigma.com/reference/graphql_api/objects/watchlist-entry
