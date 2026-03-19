# BrandLocationDescriptionEdge

## Overview

`BrandLocationDescriptionEdge` is a GraphQL object type that implements the Relay edge pattern for paginating through brand location description data.

## Description

A Relay edge containing a `BrandLocationDescription` and its cursor for pagination purposes.

## Fields

### node
- **Type:** [`BrandLocationDescription`](/reference/graphql_api/objects/brand-location-description)
- **Description:** The item at the end of the edge

### cursor
- **Type:** `String!` (non-null)
- **Description:** A cursor for use in pagination

## Relationships

**Member of:**
- [`BrandLocationDescriptionConnection`](/reference/graphql_api/objects/brand-location-description-connection)

## Usage Context

This edge type is used within connection objects to provide pagination cursors alongside brand location description data, following the Relay cursor-based pagination specification.

---

*Last updated: March 11, 2026*
