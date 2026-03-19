# BrandNameEdge

## Overview

`BrandNameEdge` is a Relay-compliant edge type that encapsulates a `BrandName` object along with pagination metadata.

## Type Definition

```graphql
type BrandNameEdge {
  node: BrandName
  cursor: String!
}
```

## Fields

### node
- **Type:** [`BrandName`](/reference/graphql_api/objects/brand-name)
- **Description:** "The item at the end of the edge"

### cursor
- **Type:** `String!` (non-null)
- **Description:** "A cursor for use in pagination"

## Usage Context

This edge type appears as a member of the [`BrandNameConnection`](/reference/graphql_api/objects/brand-name-connection) object, which implements standard Relay pagination patterns for querying collections of brand names.

## Related Types

- **Parent:** [`BrandNameConnection`](/reference/graphql_api/objects/brand-name-connection)
- **Node Type:** [`BrandName`](/reference/graphql_api/objects/brand-name)

---

*Documentation last updated: March 11, 2026*
