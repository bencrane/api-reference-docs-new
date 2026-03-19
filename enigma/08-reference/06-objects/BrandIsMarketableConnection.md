# BrandIsMarketableConnection

## Overview

A GraphQL object type that represents a paginated collection of brand marketability records within the Enigma GraphQL API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null object)
- **Description:** Provides pagination metadata for navigating through the connection, including information about available pages and cursor positions.

### edges
- **Type:** `[BrandIsMarketableEdge]!` (non-null list of objects)
- **Description:** Contains the individual nodes (data items) in this paginated connection, each wrapped in an edge object.

## Related Types

This connection type is utilized by:
- **`Brand`** object - references this connection to provide marketability assessment data

## GraphQL Schema Location

- **Namespace:** `/reference/graphql_api/objects/`
- **Related Objects:**
  - [`BrandIsMarketableEdge`](/reference/graphql_api/objects/brand-is-marketable-edge)
  - [`PageInfo`](/reference/graphql_api/objects/page-info)

---

*Last updated: March 11, 2026*
