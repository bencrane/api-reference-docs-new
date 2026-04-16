# WebsiteContentWebsiteEdge

## Overview
A Relay edge containing a `WebsiteContentWebsite` and its cursor for pagination purposes.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `node` | [`Website`](/reference/graphql_api/objects/website) | — | The item at the end of the edge |
| `cursor` | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| `id` | [`ID`](/reference/graphql_api/scalars/id) | — | Unique identifier |
| `websiteServesWebsiteContentId` | [`UUID`](/reference/graphql_api/scalars/uuid) | — | UUID identifier for website-serves-website-content relationship |
| `datasetIds` | [`JSON`](/reference/graphql_api/scalars/json) | — | JSON data containing dataset identifiers |
| `firstObservedDate` | [`String`](/reference/graphql_api/scalars/string) | — | Initial observation date |
| `lastObservedDate` | [`String`](/reference/graphql_api/scalars/string) | — | Most recent observation date |
| `rank` | [`Int`](/reference/graphql_api/scalars/int) | — | Ranking value |
| `internalId` | [`String`](/reference/graphql_api/scalars/string) | — | Internal identifier |
| `internalWebsiteServesWebsiteContentId` | [`String`](/reference/graphql_api/scalars/string) | — | Internal identifier for relationship |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** [`WebsiteContentWebsiteConnection`](/reference/graphql_api/objects/website-content-website-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/website-content-website-edge
