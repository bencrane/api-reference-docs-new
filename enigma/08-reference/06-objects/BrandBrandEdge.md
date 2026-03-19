# BrandBrandEdge

## Overview

`BrandBrandEdge` is a Relay-compliant edge type that represents a connection between brands in the Enigma GraphQL API. It encapsulates a `Brand` node along with pagination information and relationship metadata.

## Description

"A Relay edge containing a `BrandBrand` and its cursor."

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `node` | [`Brand`](/reference/graphql_api/objects/brand) | The brand entity at the end of this edge |
| `cursor` | `String!` | Pagination cursor for use in relay-based pagination |
| `brandIsAffiliatedWithBrandId` | `UUID` | Identifier for the affiliated brand relationship |
| `rank` | `Int` | Ranking value for the brand affiliation |
| `id` | `ID` | Unique identifier for the edge |
| `datasetIds` | `JSON` | Collection of dataset identifiers associated with the relationship |
| `firstObservedDate` | `String` | Date when this affiliation was first detected |
| `lastObservedDate` | `String` | Date of the most recent observation of this affiliation |
| `affiliationType` | `String` | Classification of the relationship type between brands |
| `internalId` | `String` | Internal system identifier |
| `internalBrandIsAffiliatedWithBrandId` | `String` | Internal identifier for the affiliated brand relationship |

## Relationships

**Member of:** [`BrandBrandConnection`](/reference/graphql_api/objects/brand-brand-connection)

This edge type is used within connection objects to structure paginated responses containing brand affiliation data.
