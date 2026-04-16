# WebsiteWebsiteContentEdge

## Overview
A Relay edge containing a `WebsiteWebsiteContent` and its cursor for pagination purposes.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | [`WebsiteContent`](/reference/graphql_api/objects/website-content) | — | The item at the end of the edge |
| cursor | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| id | [`ID`](/reference/graphql_api/scalars/id) | — | Identifier for the edge |
| websiteServesWebsiteContentId | [`UUID`](/reference/graphql_api/scalars/uuid) | — | Unique identifier for the website-serves-website-content relationship |
| datasetIds | [`JSON`](/reference/graphql_api/scalars/json) | — | Dataset identifiers associated with this edge |
| firstObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | Date when this relationship was first observed |
| lastObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | Date when this relationship was last observed |
| rank | [`Int`](/reference/graphql_api/scalars/int) | — | Ranking value for this edge |
| internalId | [`String`](/reference/graphql_api/scalars/string) | — | Internal identifier |
| internalWebsiteServesWebsiteContentId | [`String`](/reference/graphql_api/scalars/string) | — | Internal identifier for the relationship |

## Interfaces Implemented
None.

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** [`WebsiteWebsiteContentConnection`](/reference/graphql_api/objects/website-website-content-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/website-website-content-edge
