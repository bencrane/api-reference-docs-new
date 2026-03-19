# BrandIndustryConnection

## Overview

The `BrandIndustryConnection` is a GraphQL object type that facilitates pagination of brand-industry relationships within the Enigma API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null object)
- **Description:** "Pagination data for this connection."

### edges
- **Type:** `[BrandIndustryEdge]!` (non-null list)
- **Description:** "Contains the nodes in this connection."

## Usage Context

This connection type appears as a field within the `Brand` object, enabling developers to query industry associations related to specific brands while leveraging standard GraphQL pagination patterns.

## Related Types

- **Parent Type:** [`Brand`](/reference/graphql_api/objects/brand)
- **Edge Type:** [`BrandIndustryEdge`](/reference/graphql_api/objects/brand-industry-edge)
- **Page Info Type:** [`PageInfo`](/reference/graphql_api/objects/page-info)
