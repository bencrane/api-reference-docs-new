# List

## Overview
No description provided.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `ID!` | — | — |
| `listType` | `ListType` | — | — |
| `name` | `String` | — | — |
| `description` | `String` | — | — |
| `searchInput` | `ListSearchInput` | — | — |
| `createdTimestamp` | `DateTime!` | — | — |
| `updatedTimestamp` | `DateTime!` | — | — |
| `materializations` | `ListMaterializationConnection` | `before`, `after`, `first`, `last` (all `String`/`Int`) | — |
| `fileFormat` | `String` | — | — |
| `inputFileUri` | `String` | — | — |
| `columnCounts` | `[ColumnCount]` | — | — |
| `fieldAliases` | `[FieldAlias]` | — | — |
| `columnOrdering` | `[String]` | — | — |
| `columnMapping` | `[ColumnMapping]` | — | — |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** `ListEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `CreateList`, `UpdateList`

## Source
https://documentation.enigma.com/reference/graphql_api/objects/list
