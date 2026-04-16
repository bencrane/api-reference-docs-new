# LegalEntity

## Overview
No description

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `ID!` | — | — |
| `internalId` | `String` | — | — |
| `enigmaId` | `String` | — | — |
| `tieBreakerMetadata` | `LegalEntityTieBreakerMetadata` | — | — |
| `searchMetadata` | `Searchmetadata` | — | — |
| `brands` | `LegalEntityBrandConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `names` | `LegalEntityNameConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `roles` | `LegalEntityRoleConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `persons` | `LegalEntityPersonConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `registeredEntities` | `LegalEntityRegisteredEntityConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `tins` | `LegalEntityTinConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `operatingLocations` | `LegalEntityOperatingLocationConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `isFlaggedByWatchlistEntries` | `LegalEntityIsFlaggedByWatchlistEntryConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `appearsOnWatchlistEntries` | `LegalEntityAppearsOnWatchlistEntryConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `addresses` | `LegalEntityAddressConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `legalEntities` | `LegalEntityLegalEntityConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `types` | `LegalEntityTypeConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `bankruptcies` | `LegalEntityBankruptcyConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | — |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | — |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | — |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | — |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | — |
| `_fn` | `JSON` | — | — |

## Interfaces Implemented
- `NodeFunctions`
- `Entity`

## Type Membership
- **Member of Edge(s):** `AddressLegalEntityEdge`, `BrandLegalEntityEdge`, `LegalEntityLegalEntityEdge`, `OperatingLocationLegalEntityEdge`, `PersonLegalEntityEdge`, `RegisteredEntityLegalEntityEdge`, `RoleLegalEntityEdge`, `TinLegalEntityEdge`, `WatchlistEntryAppearsOnLegalEntityEdge`, `WatchlistEntryIsFlaggedByLegalEntityEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** `SearchUnion`
- **Referenced by Input(s):** None
- **Referenced by Object(s):** Multiple connection objects

## Source
https://documentation.enigma.com/reference/graphql_api/objects/legal-entity
