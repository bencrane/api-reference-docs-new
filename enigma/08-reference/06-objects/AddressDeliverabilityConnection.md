# AddressDeliverabilityConnection

## Overview

This is a GraphQL object type used for handling paginated collections of address deliverability data within the Enigma API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null)
- **Description:** "Pagination data for this connection."

### edges
- **Type:** `[AddressDeliverabilityEdge]!` (non-null list)
- **Description:** "Contains the nodes in this connection."

## Relationships

This object serves as a connection type and is utilized by the `Address` GraphQL object, allowing consumers to retrieve paginated sets of address deliverability information alongside navigation metadata.

## Implementation Notes

As a connection object, `AddressDeliverabilityConnection` follows the standard GraphQL Relay cursor-based pagination pattern, pairing edge nodes with pagination context to enable efficient data traversal across large datasets.
