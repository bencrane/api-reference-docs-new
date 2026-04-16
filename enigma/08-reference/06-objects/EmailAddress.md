# EmailAddress

## Overview
An email address for the business or a person associated with the business.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `emailAddress` | `String` | — | The email address which consists of a user name, @ symbol, sub domain (optional) and domain. |
| `id` | `UUID!` | — | Unique identifier. |
| `firstObservedDate` | `String` | — | Date when the email address was first observed. |
| `lastObservedDate` | `String` | — | Date when the email address was last observed. |
| `internalId` | `String` | — | Internal identifier. |
| `internalEmailAddressId` | `String` | — | Internal email address identifier. |
| `roles` | `EmailAddressRoleConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Connection to associated roles. |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count aggregation function. |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Count distinct aggregation function. |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Boolean check for field presence. |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum aggregation function. |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum aggregation function. |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum aggregation function. |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average aggregation function. |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect values with optional separator. |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime aggregation function. |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime aggregation function. |
| `_fn` | `JSON` | — | Function metadata. |

## Interfaces Implemented
- `NodeFunctions`

## Type Membership
- **Member of Edge(s):** `RoleEmailAddressEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/email-address
