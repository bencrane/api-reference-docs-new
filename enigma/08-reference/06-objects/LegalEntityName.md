# LegalEntityName

## Overview
Represents entities that U.S. law recognizes as having identity and rights, including natural persons and artificial entities such as businesses and governmental bodies.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `name` | `String` | — | The legal entity's name. |
| `nameFullTextSearchVector` | `String` | — | Full-text search vector for name. |
| `id` | `UUID!` | — | Unique identifier (non-null). |
| `firstObservedDate` | `String` | — | Date when entity was first observed. |
| `lastObservedDate` | `String` | — | Date when entity was last observed. |
| `legalEntityType` | `String` | — | Legal form: Person, Corporation, LLC, Partnership, etc. |
| `internalId` | `String` | — | Internal identifier. |
| `internalLegalEntityId` | `String` | — | Internal legal entity identifier. |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count of field values. |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Count of distinct field values. |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Check field existence. |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum of field values. |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum field value. |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum field value. |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average of field values. |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect field values. |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime value. |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime value. |
| `_fn` | `JSON` | — | Function metadata. |

## Interfaces Implemented
- `NodeFunctions`

## Type Membership
- **Member of Edge(s):** `LegalEntityNameEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-name
