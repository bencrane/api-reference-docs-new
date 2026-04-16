# RegisteredEntity

## Overview

Represents businesses which have become legal entities by registering with a U.S. Secretary of State (SoS). Each state's SoS serves as the ultimate source of truth for these records. The system joins domestic and foreign registrations together to represent single entities.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `name` | `String` | — | Standardized name derived from the entity's registration |
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | Date entity was first observed |
| `lastObservedDate` | `String` | — | Date entity was last observed |
| `registeredEntityType` | `String` | — | Standardized legal form (e.g., "Corporation", "LLC") |
| `formationDate` | `Date` | — | Earliest issue date from registrations, formatted YYYY-MM-DD |
| `formationYear` | `Int` | — | Year (YYYY) of earliest issue date from registrations |
| `internalId` | `String` | — | Internal identifier |
| `internalRegisteredEntityId` | `String` | — | Internal registered entity identifier |
| `nameFullTextSearchVector` | `String` | — | Full text search vector for name |
| `registrations` | `RegisteredEntityRegistrationConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Connection to registrations |
| `legalEntities` | `RegisteredEntityLegalEntityConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Connection to legal entities |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count aggregation function |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation function |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value function |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value function |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value function |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collection aggregation function |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime function |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime function |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `LegalEntityRegisteredEntityEdge`, `RegistrationRegisteredEntityEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `RegisteredEntityRegistrationConnection`, `RegisteredEntityLegalEntityConnection`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/registered-entity
