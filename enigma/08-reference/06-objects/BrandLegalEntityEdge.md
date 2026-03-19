# BrandLegalEntityEdge

## Overview

The `BrandLegalEntityEdge` is a Relay-compliant edge type within the Enigma GraphQL API that encapsulates a `LegalEntity` node along with pagination metadata, representing a connection between a brand and a legal entity.

## Type Definition

```graphql
type BrandLegalEntityEdge {
  node: LegalEntity
  cursor: String!
  id: ID
  legalEntityDoesBusinessAsBrandId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityDoesBusinessAsBrandId: String
}
```

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `node` | `LegalEntity` | — | "The item at the end of the edge" |
| `cursor` | `String` | Yes | Pagination cursor for use in relay-based pagination |
| `id` | `ID` | — | Unique identifier for the edge |
| `legalEntityDoesBusinessAsBrandId` | `UUID` | — | UUID identifier linking the legal entity to the brand relationship |
| `datasetIds` | `JSON` | — | Collection of dataset identifiers associated with this edge |
| `firstObservedDate` | `String` | — | Initial observation date of this relationship |
| `lastObservedDate` | `String` | — | Most recent observation date of this relationship |
| `rank` | `Int` | — | Ranking value for this edge |
| `internalId` | `String` | — | Internal system identifier |
| `internalLegalEntityDoesBusinessAsBrandId` | `String` | — | Internal identifier for the legal entity-brand relationship |

## Relationships

**Member of:** `BrandLegalEntityConnection` object

This edge serves as a component within connection objects that facilitate paginated retrieval of legal entities associated with brands.
