# BrandLegalEntityConnection

## Overview

A connection type used for paginating through relationships between Brand and LegalEntity objects within the Enigma GraphQL API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null)
- **Description:** Pagination metadata for navigating through the connection results.

### edges
- **Type:** `[BrandLegalEntityEdge]!` (non-null list)
- **Description:** The collection of edge nodes representing individual Brand-to-LegalEntity relationships.

## Usage Context

This connection type is returned when querying Brand objects to retrieve their associated legal entities. It implements the standard GraphQL cursor-based pagination pattern, allowing consumers to navigate large result sets efficiently.

## Related Types

- **Parent:** [`Brand`](/reference/graphql_api/objects/brand)
- **Edge Type:** [`BrandLegalEntityEdge`](/reference/graphql_api/objects/brand-legal-entity-edge)
- **Pagination Type:** [`PageInfo`](/reference/graphql_api/objects/page-info)
