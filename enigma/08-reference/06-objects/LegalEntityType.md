# LegalEntityType

## Overview

These are entities which U.S. law recognizes as having an identity and rights. They can be either natural persons, or artificial entities such as businesses and governmental bodies.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | None | Unique identifier |
| `firstObservedDate` | `String` | None | Date entity was first observed |
| `lastObservedDate` | `String` | None | Date entity was last observed |
| `legalEntityType` | `String` | None | The legal form of the entity (Person, Corporation, LLC, Partnership, etc.) |
| `internalId` | `String` | None | Internal identifier |
| `internalLegalEntityId` | `String` | None | Internal legal entity identifier |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count of records matching field and conditions |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Count of distinct records |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Whether field exists under conditions |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum of field values |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum field value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum field value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average field value |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect field values joined by separator |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime value |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime value |
| `_fn` | `JSON` | None | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `LegalEntityTypeEdge`
- **Member of Connection(s):** `LegalEntityTypeConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `LegalEntity`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-type
