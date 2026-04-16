# Person

## Overview
No description provided in documentation.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `ID!` | None | Non-null identifier |
| `internalId` | `String` | None | Internal identifier string |
| `enigmaId` | `String` | None | Enigma identifier string |
| `tieBreakerMetadata` | `String` | None | Metadata for tie-breaking scenarios |
| `searchMetadata` | `Searchmetadata` | None | Search metadata object |
| `names` | `PersonNameConnection` | `first: Int = 3, last: Int, after: String, before: String, conditions: ConnectionConditions` | Connection to person names |
| `legalEntities` | `PersonLegalEntityConnection` | `first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions` | Connection to legal entities |
| `count` | `Int` | `field: String!, conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!, conditions: Conditions` | Distinct count aggregation |
| `has` | `Boolean` | `field: String!, conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!, conditions: Conditions` | Sum aggregation function |
| `min` | `Int` | `field: String!, conditions: Conditions` | Minimum value aggregation |
| `max` | `Int` | `field: String!, conditions: Conditions` | Maximum value aggregation |
| `avg` | `Float` | `field: String!, conditions: Conditions` | Average value aggregation |
| `collect` | `String` | `field: String!, separator: String, conditions: Conditions` | Collect values with separator |
| `minDateTime` | `DateTime` | `field: String!, conditions: Conditions` | Minimum datetime aggregation |
| `maxDateTime` | `DateTime` | `field: String!, conditions: Conditions` | Maximum datetime aggregation |
| `_fn` | `JSON` | None | Function metadata |

## Interfaces Implemented
- `NodeFunctions`
- `Entity`

## Type Membership
- **Member of Edge(s):** `LegalEntityPersonEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** `SearchUnion`
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/person
