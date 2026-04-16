# ListMaterialization

## Overview
No description provided.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| id | `ID!` | — | — |
| listId | `ID!` | — | — |
| createdTimestamp | `DateTime!` | — | — |
| status | `String!` | — | — |
| updatedTimestamp | `DateTime!` | — | — |
| searchInput | `ListSearchInput` | — | — |
| metrics | `ListMaterializationMetricConnection` | `before: String`, `after: String`, `first: Int`, `last: Int` | — |
| billingEventDetails | `ListMaterializationBillingEventDetailConnection` | `before: String`, `after: String`, `first: Int`, `last: Int` | — |
| fieldAliases | `[FieldAlias]` | — | — |
| columnOrdering | `[String]` | — | — |
| columnCounts | `[ColumnCount]` | — | — |
| columnMapping | `[ColumnMapping]` | — | — |
| inputFileUri | `String` | — | — |
| listType | `ListType` | — | — |
| resourceUri | `String` | — | — |
| progressPercentComplete | `Int` | — | — |
| progressMessage | `String` | — | — |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** ListMaterializationEdge
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** CancelListMaterialization, CreateListMaterialization, UpdateListMaterialization

## Source
https://documentation.enigma.com/reference/graphql_api/objects/list-materialization
