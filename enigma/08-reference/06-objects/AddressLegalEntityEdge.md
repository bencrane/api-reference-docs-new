# AddressLegalEntityEdge

## Overview

The `AddressLegalEntityEdge` represents a Relay-compliant edge in the Enigma GraphQL API. It wraps a `LegalEntity` object along with pagination metadata, enabling cursor-based traversal through collections of legal entities associated with specific addresses.

## Type Definition

```graphql
type AddressLegalEntityEdge {
  node: LegalEntity
  cursor: String!
  id: ID
  legalEntityReceivesMailAtAddressId: UUID
  datasetIds: JSON
  firstObservedDate: String
  lastObservedDate: String
  rank: Int
  internalId: String
  internalLegalEntityReceivesMailAtAddressId: String
}
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| **node** | `LegalEntity` | The legal entity object at the end of this edge |
| **cursor** | `String!` | Required pagination cursor for use in subsequent queries |
| **id** | `ID` | Identifier for the edge instance |
| **legalEntityReceivesMailAtAddressId** | `UUID` | Unique identifier linking the legal entity to the address for mail receipt |
| **datasetIds** | `JSON` | Collection of dataset identifiers associated with this relationship |
| **firstObservedDate** | `String` | Timestamp of initial observation of this address-entity association |
| **lastObservedDate** | `String` | Timestamp of most recent observation of this association |
| **rank** | `Int` | Ranking value for ordering or relevance |
| **internalId** | `String` | Internal system identifier |
| **internalLegalEntityReceivesMailAtAddressId** | `String` | Internal reference for the mail-receipt relationship |

## Relationships

This type functions as a member of the `AddressLegalEntityConnection` object, which manages paginated collections of address-to-legal-entity relationships.
