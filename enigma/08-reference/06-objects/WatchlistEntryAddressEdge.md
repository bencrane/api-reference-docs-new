# WatchlistEntryAddressEdge

## Overview

A Relay edge containing a `WatchlistEntryAddress` and its cursor for pagination purposes.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | [`Address`](/reference/graphql_api/objects/address) | None | The item at the end of the edge |
| cursor | [`String!`](/reference/graphql_api/scalars/string) | None | A cursor for use in pagination |
| id | [`ID`](/reference/graphql_api/scalars/id) | None | No description |
| addressAppearsOnWatchlistEntryId | [`UUID`](/reference/graphql_api/scalars/uuid) | None | No description |
| datasetIds | [`JSON`](/reference/graphql_api/scalars/json) | None | No description |
| firstObservedDate | [`String`](/reference/graphql_api/scalars/string) | None | No description |
| lastObservedDate | [`String`](/reference/graphql_api/scalars/string) | None | No description |
| rank | [`Int`](/reference/graphql_api/scalars/int) | None | No description |
| internalId | [`String`](/reference/graphql_api/scalars/string) | None | No description |
| internalAddressAppearsOnWatchlistEntryId | [`String`](/reference/graphql_api/scalars/string) | None | No description |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** [`WatchlistEntryAddressConnection`](/reference/graphql_api/objects/watchlist-entry-address-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/watchlist-entry-address-edge
