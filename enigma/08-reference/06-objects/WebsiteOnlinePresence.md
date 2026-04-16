# WebsiteOnlinePresence

## Overview
Indicates whether a website is an e-commerce website that sells products directly online. Enigma analyzes key indicators suggesting online shopping capabilities to identify e-commerce websites.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | Initial observation date |
| `lastObservedDate` | `String` | — | Most recent observation date |
| `hasOnlineSales` | `String` | — | "Yes" indicates e-commerce capability; null indicates insufficient data |
| `internalId` | `String` | — | Internal identifier |
| `internalWebsiteId` | `String` | — | Internal website identifier |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count values in field |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Count distinct values |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Check field existence |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum field values |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average value |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect field values |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Earliest datetime |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Latest datetime |
| `_fn` | `JSON` | — | Internal function field |

## Interfaces Implemented
- `NodeFunctions`

## Type Membership
- **Member of Edge(s):** `WebsiteOnlinePresenceEdge`
- **Member of Connection(s):** `WebsiteOnlinePresenceConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `Website`

## Source
https://documentation.enigma.com/reference/graphql_api/objects/website-online-presence
