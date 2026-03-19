# AddressLegalEntityConnection

## Overview

A GraphQL object type that represents a paginated collection of legal entities associated with a specific address within the Enigma API.

## Type Definition

```graphql
type AddressLegalEntityConnection {
  pageInfo: PageInfo!
  edges: [AddressLegalEntityEdge]!
}
```

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null object)
- **Description:** Contains pagination metadata for navigating through the connection results, including cursor positions and availability of additional pages.

### edges
- **Type:** `[AddressLegalEntityEdge]!` (non-null list of objects)
- **Description:** An array of edge objects that wrap the actual legal entity nodes, providing access to both the data and cursor information for pagination.

## Relationships

This type is utilized by the [`Address`](/reference/graphql_api/objects/address) object as a field, allowing queries to retrieve all legal entities connected to a given address through a paginated connection pattern.

## Related Types

- **Previous:** [AddressDeliverability](/reference/graphql_api/objects/address-deliverability)
- **Next:** [AddressLegalEntityEdge](/reference/graphql_api/objects/address-legal-entity-edge)
