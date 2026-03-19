# BrandCardTransactionEdge

## Overview

`BrandCardTransactionEdge` is a Relay-compliant edge type that wraps a `BrandCardTransaction` object along with pagination metadata, following standard GraphQL connection patterns.

## Type Definition

```graphql
type BrandCardTransactionEdge {
  node: BrandCardTransaction
  cursor: String!
}
```

## Fields

### node
- **Type:** [`BrandCardTransaction`](/reference/graphql_api/objects/brand-card-transaction)
- **Description:** The data object representing the brand's card transaction at this edge position

### cursor
- **Type:** `String!` (non-null)
- **Description:** An opaque pagination token for cursor-based traversal through result sets

## Related Types

This edge type is a member of:
- [`BrandCardTransactionConnection`](/reference/graphql_api/objects/brand-card-transaction-connection) — the parent connection type that aggregates multiple edges

## Usage Context

`BrandCardTransactionEdge` enables paginated queries over brand card transaction data by combining the transaction details with a cursor reference, allowing clients to efficiently navigate through large result sets using cursor-based pagination patterns.

---

**Last Updated:** Mar 11, 2026
