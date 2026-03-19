# AddressOperatingLocationConnection

## Overview

A GraphQL object that represents a paginated collection of operating locations associated with an address in the Enigma API.

## Fields

### pageInfo
- **Type:** `PageInfo!` (non-null object)
- **Description:** "Pagination data for this connection."

### edges
- **Type:** `[AddressOperatingLocationEdge]!` (non-null list of objects)
- **Description:** "Contains the nodes in this connection."

## Relationships

This type is utilized as a member of the [`Address`](/reference/graphql_api/objects/address) object, enabling queries to retrieve paginated results of operating locations linked to a specific address.

## Usage Context

This connection type follows the standard GraphQL cursor-based pagination pattern, combining pagination metadata with a collection of edge objects that wrap the underlying operating location data and cursor information.
