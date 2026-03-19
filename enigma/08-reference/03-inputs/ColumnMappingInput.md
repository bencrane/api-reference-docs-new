# ColumnMappingInput

## Overview

The `ColumnMappingInput` is a GraphQL input type used to map columns to search fields within list operations.

## Definition

```graphql
input ColumnMappingInput {
  columnName: String!
  searchField: ListSearchField!
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `columnName` | `String!` | The name of the column being mapped (required) |
| `searchField` | `ListSearchField!` | The search field enum value to associate with the column (required) |

## Usage Context

This input type is utilized as a component within:
- **`CreateListInput`** — for establishing column mappings when creating new lists
- **`UpdateListInput`** — for modifying column mappings in existing lists

## Related References

- [ListSearchField Enum](/reference/graphql_api/enums/list-search-field)
- [CreateListInput](/reference/graphql_api/inputs/create-list-input)
- [UpdateListInput](/reference/graphql_api/inputs/update-list-input)
