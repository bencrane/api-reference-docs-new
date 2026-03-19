# BrandLocationDescriptionConnection

## Overview

The `BrandLocationDescriptionConnection` is a GraphQL object type that implements standard connection pattern pagination for brand location description data.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null object)
- **Description:** "Pagination data for this connection."

### edges
- **Type:** `[BrandLocationDescriptionEdge]!` (non-null object array)
- **Description:** "Contains the nodes in this connection."

## Related Types

This object type is used as a field member of the `Brand` object type within the Enigma GraphQL API reference.

## Context

This connection object follows the standard GraphQL connection pattern, providing pagination capabilities and access to individual edge nodes containing brand location description information.
