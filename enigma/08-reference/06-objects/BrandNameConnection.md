# BrandNameConnection

## Overview

`BrandNameConnection` is a GraphQL object type that implements pagination functionality for brand name data within the Enigma GraphQL API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null object)
- **Description:** "Pagination data for this connection."

### edges
- **Type:** `[BrandNameEdge]!` (non-null object array)
- **Description:** "Contains the nodes in this connection."

## Type Details

This object serves as a connection wrapper, following the standard GraphQL cursor-based pagination pattern. It provides two essential components:

1. **pageInfo** - Supplies metadata about the current page state, including cursors and whether additional pages exist
2. **edges** - Returns an array of `BrandNameEdge` objects that wrap individual brand name records with their associated cursor information

## Related Types

- **Associated With:** [`Brand`](/reference/graphql_api/objects/brand) object
- **Edge Type:** [`BrandNameEdge`](/reference/graphql_api/objects/brand-name-edge)
- **Page Info Type:** [`PageInfo`](/reference/graphql_api/objects/page-info)

## Usage Context

`BrandNameConnection` is typically returned when querying brand name relationships from the `Brand` object, enabling efficient pagination through potentially large result sets of brand names associated with a particular brand entity.
