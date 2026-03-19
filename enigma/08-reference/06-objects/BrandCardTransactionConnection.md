# BrandCardTransactionConnection

## Overview

A GraphQL object type that represents a paginated collection of brand card transaction data within the Enigma API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null object)
- **Description:** Contains pagination metadata for navigating through the connection results.

### edges
- **Type:** `[BrandCardTransactionEdge]!` (non-null array of objects)
- **Description:** An array of edge objects that wrap individual card transaction nodes associated with brands.

## Usage Context

This connection type is utilized by the `Brand` object to provide paginated access to card transaction information. It follows the standard GraphQL cursor-based pagination pattern, allowing clients to traverse large datasets efficiently.

## Related Types

- **Parent:** `Brand` object
- **Edge Type:** `BrandCardTransactionEdge`
- **Node Type:** `BrandCardTransaction`

## Documentation Source

Enigma GraphQL API Reference - Last updated March 11, 2026
