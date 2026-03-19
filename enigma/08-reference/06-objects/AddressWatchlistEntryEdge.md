# AddressWatchlistEntryEdge

## Overview

The `AddressWatchlistEntryEdge` is a Relay edge type that encapsulates a `WatchlistEntry` object along with pagination cursor information. It follows the Relay cursor connections specification for implementing efficient pagination in GraphQL queries.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `node` | `WatchlistEntry` | The watchlist entry data at this edge |
| `cursor` | `String!` | Pagination cursor for use in subsequent queries |
| `id` | `ID` | Unique identifier for the edge |
| `addressAppearsOnWatchlistEntryId` | `UUID` | UUID linking the address to its watchlist entry |
| `datasetIds` | `JSON` | Collection of dataset identifiers associated with this entry |
| `firstObservedDate` | `String` | Initial observation timestamp for this record |
| `lastObservedDate` | `String` | Most recent observation timestamp for this record |
| `rank` | `Int` | Ranking or priority value for the watchlist entry |
| `internalId` | `String` | Internal system identifier |
| `internalAddressAppearsOnWatchlistEntryId` | `String` | Internal system ID for the relationship |

## Usage Context

This type appears as a member of the `AddressWatchlistEntryConnection` object, which manages collections of watchlist entries tied to specific addresses. The edge pattern enables efficient pagination through large datasets using cursor-based navigation.
