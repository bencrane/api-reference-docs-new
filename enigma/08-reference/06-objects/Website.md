# Website

## Overview

A website associated with a business.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `website` | `String` | — | The complete url of the website including protocol, subdomain and path |
| `firstObservedDate` | `String` | — | First observation date of the website |
| `id` | `UUID!` | — | Unique identifier |
| `lastObservedDate` | `String` | — | Most recent observation date of the website |
| `subdomain` | `String` | — | The subdomain component (e.g., "documentation" in documentation.enigma.com) |
| `domain` | `String` | — | The domain component (e.g., "enigma" in documentation.enigma.com) |
| `topLevelDomain` | `String` | — | The TLD component (e.g., "com" in documentation.enigma.com) |
| `path` | `String` | — | The path component of the website URL |
| `fragment` | `String` | — | The fragment component of the website URL |
| `internalId` | `String` | — | Internal identifier |
| `internalWebsiteId` | `String` | — | Internal website identifier |
| `brands` | `WebsiteBrandConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Brands associated with this website |
| `operatingLocations` | `WebsiteOperatingLocationConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Operating locations for this website |
| `websiteContents` | `WebsiteWebsiteContentConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Website content entries |
| `technologiesUseds` | `WebsiteTechnologiesUsedConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Technologies used on website |
| `onlinePresences` | `WebsiteOnlinePresenceConnection` | `first: Int = 3`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Online presence data |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count aggregation |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation function |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value aggregation |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value aggregation |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value aggregation |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect values with separator |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime aggregation |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime aggregation |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** `BrandWebsiteEdge`, `OperatingLocationWebsiteEdge`, `WebsiteContentWebsiteEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `BrandWebsiteEdge`, `OperatingLocationWebsiteEdge`, `WebsiteContentWebsiteEdge`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/website
