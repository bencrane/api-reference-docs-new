# OperatingLocation

## Overview
No description provided.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `internalId` | `String` | None | — |
| `enigmaId` | `String` | None | — |
| `id` | `ID!` | None | — |
| `tieBreakerMetadata` | `OperatingLocationTieBreakerMetadata` | None | — |
| `searchMetadata` | `Searchmetadata` | None | — |
| `names` | `OperatingLocationNameConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `addresses` | `OperatingLocationAddressConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `phoneNumbers` | `OperatingLocationPhoneNumberConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `brands` | `OperatingLocationBrandConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `roles` | `OperatingLocationRoleConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `legalEntities` | `OperatingLocationLegalEntityConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `operatingStatuses` | `OperatingLocationOperatingStatusConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `technologiesUseds` | `OperatingLocationTechnologiesUsedConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `websites` | `OperatingLocationWebsiteConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `reviewSummaries` | `OperatingLocationReviewSummaryConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `cardTransactions` | `OperatingLocationCardTransactionConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `ranks` | `OperatingLocationRankConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `revenueQualities` | `OperatingLocationRevenueQualityConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `locationTypes` | `OperatingLocationLocationTypeConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `isMarketables` | `OperatingLocationIsMarketableConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
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
| `_fn` | `JSON` | None | — |

## Interfaces Implemented
- `NodeFunctions`
- `Entity`

## Type Membership
- **Member of Edge(s):** AddressOperatingLocationEdge, BrandOperatingLocationEdge, LegalEntityOperatingLocationEdge, PhoneNumberOperatingLocationEdge, ReviewSummaryOperatingLocationEdge, RoleOperatingLocationEdge, WebsiteOperatingLocationEdge
- **Member of Connection(s):** None
- **Member of Union(s):** SearchUnion
- **Referenced by Input(s):** None
- **Referenced by Object(s):** Multiple connection types

## Source
https://documentation.enigma.com/reference/graphql_api/objects/operating-location
