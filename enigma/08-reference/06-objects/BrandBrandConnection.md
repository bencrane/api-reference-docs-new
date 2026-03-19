# BrandBrandConnection

## Overview

`BrandBrandConnection` is a GraphQL object type used for pagination of Brand-to-Brand relationships within the Enigma GraphQL API.

## Fields

### pageInfo
- **Type:** [`PageInfo!`](/reference/graphql_api/objects/page-info) (non-null)
- **Description:** "Pagination data for this connection."

### edges
- **Type:** [`[BrandBrandEdge]!`](/reference/graphql_api/objects/brand-brand-edge) (non-null list)
- **Description:** "Contains the nodes in this connection."

## Usage Context

This connection type appears as a member of the [`Brand`](/reference/graphql_api/objects/brand) object, enabling traversal of related Brand entities through a paginated interface.

## Related Types

- **Previous:** BrandActivity
- **Next:** BrandBrandEdge

---

*Last updated: Mar 11, 2026*
