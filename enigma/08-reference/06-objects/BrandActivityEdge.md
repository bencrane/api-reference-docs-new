# BrandActivityEdge

## Overview

`BrandActivityEdge` is a GraphQL object type that implements the Relay edge pattern for pagination purposes. It wraps a `BrandActivity` object alongside cursor information needed for cursor-based pagination.

## Type Definition

```graphql
type BrandActivityEdge {
  node: BrandActivity
  cursor: String!
}
```

## Fields

### node
- **Type:** [`BrandActivity`](/reference/graphql_api/objects/brand-activity)
- **Description:** The item at the end of the edge

### cursor
- **Type:** `String!` (non-null)
- **Description:** A cursor for use in pagination

## Relationships

**Member of:**
- [`BrandActivityConnection`](/reference/graphql_api/objects/brand-activity-connection) — Used within connection objects to provide paginated results

## Usage Context

This type is used when querying collections of brand activity data. It follows the Relay cursor connection specification, allowing clients to traverse paginated result sets efficiently.
