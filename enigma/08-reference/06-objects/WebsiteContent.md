# WebsiteContent

## Overview

The state of a website at a particular time. Enigma makes requests to each website in its database at least every ninety days, with each WebsiteContent object representing findings from one such request. The object uses a rank property to track historical changes, where rank 0 contains the most recent data and higher ranks represent earlier observations.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | Initial observation timestamp |
| `lastObservedDate` | `String` | — | Most recent observation timestamp |
| `httpStatusCode` | `String` | — | HTTP response code (e.g., 200, 404) |
| `faviconUrl` | `String` | — | URL serving the website's favicon |
| `faviconImage` | `String` | — | Binary representation of favicon from HTTP response |
| `websiteAvailability` | `String` | — | Availability status |
| `internalId` | `String` | — | Internal identifier |
| `internalWebsiteContentId` | `String` | — | Internal content identifier |
| `websites` | `WebsiteContentWebsiteConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Connected websites |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Field value count |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct value count |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Field sum |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Aggregated values |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Earliest datetime |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Latest datetime |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `WebsiteWebsiteContentEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `WebsiteWebsiteContentConnection`, `Website`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/website-content
