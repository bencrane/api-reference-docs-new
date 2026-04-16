# OperatingLocationWebsiteEdge

## Overview

A Relay edge containing an `OperatingLocationWebsite` and its cursor for use in paginated queries.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `node` | [`Website`](/reference/graphql_api/objects/website) | — | The item at the end of the edge |
| `cursor` | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| `id` | [`ID`](/reference/graphql_api/scalars/id) | — | Identifier for this edge instance |
| `operatingLocationOperatesWebsiteWebsiteId` | [`UUID`](/reference/graphql_api/scalars/uuid) | — | UUID of the website operated by the location |
| `datasetIds` | [`JSON`](/reference/graphql_api/scalars/json) | — | Dataset identifiers associated with this edge |
| `firstObservedDate` | [`String`](/reference/graphql_api/scalars/string) | — | Date when the relationship was first observed |
| `lastObservedDate` | [`String`](/reference/graphql_api/scalars/string) | — | Date when the relationship was last observed |
| `rank` | [`Int`](/reference/graphql_api/scalars/int) | — | Rank or priority value |
| `internalId` | [`String`](/reference/graphql_api/scalars/string) | — | Internal identifier |
| `internalOperatingLocationOperatesWebsiteWebsiteId` | [`String`](/reference/graphql_api/scalars/string) | — | Internal website identifier for the relationship |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** [`OperatingLocationWebsiteConnection`](/reference/graphql_api/objects/operating-location-website-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-website-edge
