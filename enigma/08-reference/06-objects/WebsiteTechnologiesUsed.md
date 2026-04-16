# WebsiteTechnologiesUsed

## Overview
Indicates third-party technologies used by a website. Data is sourced from private vendors and independently verified. Currently identifies payment-related technologies including Adyen, Braintree, PayPal, Shopify, and Stripe through website scraping and content analysis.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | Initial observation date of technology usage |
| `lastObservedDate` | `String` | — | Most recent observation date |
| `technology` | `String` | — | Specific third-party technology name |
| `category` | `String` | — | Technology category (e.g., "payments") |
| `internalId` | `String` | — | Internal identifier |
| `internalWebsiteId` | `String` | — | Internal website reference |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Distinct count aggregation |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Field existence check |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum aggregation |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum aggregation |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average aggregation |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collection aggregation |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented
- `NodeFunctions`

## Type Membership
- **Member of Edge(s):** `WebsiteTechnologiesUsedEdge`
- **Member of Connection(s):** `WebsiteTechnologiesUsedConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `OperatingLocationTechnologiesUsed`

## Source
https://documentation.enigma.com/reference/graphql_api/objects/website-technologies-used
