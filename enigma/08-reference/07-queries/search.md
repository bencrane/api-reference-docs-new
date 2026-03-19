# Search Query Documentation

## Overview

The `search` query is a GraphQL operation that enables searching within the Enigma database without additional description provided in the reference material.

## Signature

```graphql
search(searchInput: SearchInput!): [SearchUnion]
```

## Parameters

**searchInput** (`SearchInput!` - required)
- The input object containing search criteria and filters for querying business data

## Return Type

**SearchUnion** (array)
- Returns an array of union type results matching the search criteria

## Usage

This query accepts a required `SearchInput` parameter and returns matching results as a union type, allowing for flexible response structures based on the entity types found.

## Related Resources

- [SearchInput Reference](/reference/graphql_api/inputs/search-input)
- [SearchUnion Reference](/reference/graphql_api/unions/search-union)
- [GraphQL API Overview](/reference/graphql_api)

---

**Last Updated:** March 11, 2026
