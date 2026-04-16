# LegalEntityAppearsOnWatchlistEntryEdge

## Overview

A Relay edge containing a `LegalEntityAppearsOnWatchlistEntry` and its cursor for use in paginated queries.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | [`WatchlistEntry`](/reference/graphql_api/objects/watchlist-entry) | — | The item at the end of the edge |
| cursor | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| id | [`ID`](/reference/graphql_api/scalars/id) | — | No description |
| legalEntityAppearsOnWatchlistEntryId | [`UUID`](/reference/graphql_api/scalars/uuid) | — | No description |
| datasetIds | [`JSON`](/reference/graphql_api/scalars/json) | — | No description |
| firstObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| lastObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| rank | [`Int`](/reference/graphql_api/scalars/int) | — | No description |
| internalId | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| internalLegalEntityAppearsOnWatchlistEntryId | [`String`](/reference/graphql_api/scalars/string) | — | No description |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** [`LegalEntityAppearsOnWatchlistEntryConnection`](/reference/graphql_api/objects/legal-entity-appears-on-watchlist-entry-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-appears-on-watchlist-entry-edge
