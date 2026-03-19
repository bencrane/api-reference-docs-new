# BrandIsMarketableEdge

## Overview

`BrandIsMarketableEdge` is a GraphQL object type that implements the Relay edge pattern for pagination. It encapsulates a `BrandIsMarketable` node along with cursor information necessary for traversing paginated result sets.

## Type Definition

```graphql
type BrandIsMarketableEdge {
  node: BrandIsMarketable
  cursor: String!
}
```

## Fields

### node
- **Type:** [`BrandIsMarketable`](/reference/graphql_api/objects/brand-is-marketable) object
- **Description:** The data item positioned at the end of this edge

### cursor
- **Type:** [`String!`](/reference/graphql_api/scalars/string) (non-null scalar)
- **Description:** A pagination cursor for use in subsequent queries to navigate through result sets

## Usage Context

`BrandIsMarketableEdge` is utilized as a member of the [`BrandIsMarketableConnection`](/reference/graphql_api/objects/brand-is-marketable-connection) object, which follows Relay's cursor-based pagination specification. Each edge within a connection represents a single result item paired with its corresponding pagination marker.

## Related Types

- **Parent Connection:** [`BrandIsMarketableConnection`](/reference/graphql_api/objects/brand-is-marketable-connection)
- **Node Type:** [`BrandIsMarketable`](/reference/graphql_api/objects/brand-is-marketable)
