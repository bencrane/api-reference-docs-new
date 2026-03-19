# BrandEdge

## Overview

`BrandEdge` is a Relay-compliant edge type within the Enigma GraphQL API that encapsulates a `Brand` object alongside pagination metadata.

## Type Definition

```graphql
type BrandEdge {
  node: Brand
  cursor: String!
}
```

## Fields

### `node`
- **Type:** [`Brand`](/reference/graphql_api/objects/brand)
- **Description:** Represents "the item at the end of the edge"

### `cursor`
- **Type:** `String!` (non-null)
- **Description:** A pagination token used in cursor-based navigation through result sets

## Usage Context

`BrandEdge` serves as a wrapper within connection types, enabling efficient pagination across collections of brand data. Each edge provides both the actual brand data and a cursor token for traversing subsequent pages of results.

## Related Types

**Member of:** [`BrandConnection`](/reference/graphql_api/objects/brand-connection)

---

**Last Updated:** March 11, 2026
