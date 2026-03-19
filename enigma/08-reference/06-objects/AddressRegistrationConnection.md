# AddressRegistrationConnection

## Overview

The `AddressRegistrationConnection` is a GraphQL object type used for paginated access to registration data associated with addresses within the Enigma API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null)
- **Description:** Supplies pagination metadata for navigating through the connection results.

### edges
- **Type:** `[AddressRegistrationEdge]!` (non-null list)
- **Description:** Holds the collection of nodes contained in this connection.

## Relationships

This object serves as a connection type that is utilized by the [`Address`](/reference/graphql_api/objects/address) object type.

## Purpose

`AddressRegistrationConnection` implements the standard GraphQL cursor-based pagination pattern, allowing clients to efficiently retrieve registration information linked to specific addresses in paginated batches.
