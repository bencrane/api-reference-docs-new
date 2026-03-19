# AddressWatchlistEntryConnection

## Overview

A GraphQL object type representing a paginated collection of watchlist entries associated with addresses.

## Fields

### pageInfo
- **Type**: `PageInfo!` (non-null)
- **Description**: Contains pagination metadata for navigating through the connection results.

### edges
- **Type**: `[AddressWatchlistEntryEdge]!` (non-null list)
- **Description**: Contains the individual watchlist entry nodes within this connection.

## Usage Context

This type is utilized by the `Address` object type to provide paginated access to associated watchlist entries.

## Related Types

- **Parent Type**: `Address`
- **Edge Type**: `AddressWatchlistEntryEdge`
- **Page Info Type**: `PageInfo`

---

*Documentation last updated March 11, 2026*
