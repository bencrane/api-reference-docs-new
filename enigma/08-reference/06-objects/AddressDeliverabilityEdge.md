# AddressDeliverabilityEdge

## Overview

The `AddressDeliverabilityEdge` is a Relay-compliant edge type that encapsulates an individual `AddressDeliverability` node along with pagination metadata.

## Type Definition

```graphql
type AddressDeliverabilityEdge {
  node: AddressDeliverability
  cursor: String!
}
```

## Fields

### node
- **Type:** [`AddressDeliverability`](/reference/graphql_api/objects/address-deliverability)
- **Description:** The item at the end of the edge

### cursor
- **Type:** [`String!`](/reference/graphql_api/scalars/string) (non-null)
- **Description:** A cursor for use in pagination

## Relationships

**Used By:**
- [`AddressDeliverabilityConnection`](/reference/graphql_api/objects/address-deliverability-connection) — This edge type is a member of the connection object, enabling paginated queries over multiple address deliverability records.

---

**Last Updated:** March 11, 2026
