# BrandActivityConnection

## Overview

`BrandActivityConnection` is a GraphQL object type used for paginated results of brand activity data within the Enigma API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null)
- **Description:** Contains pagination metadata for navigating through the connection results.

### edges
- **Type:** `[BrandActivityEdge]!` (non-null list)
- **Description:** An array of edge objects that wrap individual brand activity nodes and their cursor information.

## Usage Context

This connection type is returned as part of the [`Brand`](/reference/graphql_api/objects/brand) object when querying brand-related activities through the Enigma GraphQL API.

## Related Types

- **BrandActivityEdge** — Wraps individual activity nodes with pagination cursors
- **PageInfo** — Provides cursor-based pagination details

---

**Last Updated:** March 11, 2026
