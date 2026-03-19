# Entity Interface

## Overview

The `Entity` interface represents a base type within the GraphQL API that defines common properties shared across multiple entity types.

## Definition

```graphql
interface Entity {
  id: ID!
  searchMetadata: Searchmetadata
}
```

## Fields

### `id`
- **Type:** `ID!` (non-null scalar)
- **Description:** A unique identifier for the entity

### `searchMetadata`
- **Type:** `Searchmetadata` (object)
- **Description:** Metadata related to search operations performed on or associated with the entity

## Implementing Types

The following types implement the `Entity` interface:

- `Brand`
- `LegalEntity`
- `OperatingLocation`
- `Person`

## Related Documentation

- [Previous: UpdateListMaterializationInput](/reference/graphql_api/inputs/update-list-materialization-input)
- [Next: NodeFunctions](/reference/graphql_api/interfaces/node-functions)

**Last Updated:** March 11, 2026
