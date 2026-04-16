# WatchlistEntryIsFlaggedByLegalEntityEdge

## Overview
A Relay edge containing a `WatchlistEntryIsFlaggedByLegalEntity` and its cursor for pagination support.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | [`LegalEntity`](/reference/graphql_api/objects/legal-entity) | — | The item at the end of the edge |
| cursor | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| id | [`ID`](/reference/graphql_api/scalars/id) | — | — |
| legalEntityIsFlaggedByWatchlistEntryId | [`UUID`](/reference/graphql_api/scalars/uuid) | — | — |
| datasetIds | [`JSON`](/reference/graphql_api/scalars/json) | — | — |
| firstObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | — |
| lastObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | — |
| rank | [`Int`](/reference/graphql_api/scalars/int) | — | — |
| confidence | [`Float`](/reference/graphql_api/scalars/float) | — | — |
| confidenceFields | [`String`](/reference/graphql_api/scalars/string) | — | — |
| internalId | [`String`](/reference/graphql_api/scalars/string) | — | — |
| internalLegalEntityIsFlaggedByWatchlistEntryId | [`String`](/reference/graphql_api/scalars/string) | — | — |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** [`WatchlistEntryIsFlaggedByLegalEntityConnection`](/reference/graphql_api/objects/watchlist-entry-is-flagged-by-legal-entity-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/watchlist-entry-is-flagged-by-legal-entity-edge
