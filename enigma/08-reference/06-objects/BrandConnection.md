# BrandConnection

## Overview

`BrandConnection` is a GraphQL object type that represents a paginated collection of brand entities within the Enigma API schema.

## Type Definition

```graphql
type BrandConnection {
  pageInfo: PageInfo!
  edges: [BrandEdge]!
}
```

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null object)
- **Description:** Provides pagination metadata for navigating through the connection results, including information about cursor positions and whether additional pages exist.

### edges
- **Type:** `[BrandEdge]!` (non-null list of BrandEdge objects)
- **Description:** An array containing the actual brand nodes within this connection, with each wrapped in edge metadata.

## Purpose

This connection type follows the GraphQL relay cursor-based pagination pattern, enabling efficient retrieval and navigation of brand data sets. It pairs pagination controls with the actual result set to support scalable queries across large datasets.

## Related Types

- **[PageInfo](/reference/graphql_api/objects/page-info)** – Cursor and page navigation details
- **[BrandEdge](/reference/graphql_api/objects/brand-edge)** – Individual brand records with metadata
- **[Brand](/reference/graphql_api/objects/brand)** – The underlying brand entity structure
