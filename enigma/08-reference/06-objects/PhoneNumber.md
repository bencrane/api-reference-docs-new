# PhoneNumber

## Overview
The phone number for a particular business entity.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `phoneNumber` | `String` | — | Twelve-digit string representation of the complete phone number (NANP compliant). Format: "+1" prefix + 11 digits (area code, exchange number, line number). Must have valid U.S. area code. |
| `id` | `UUID!` | — | Unique identifier |
| `firstObservedDate` | `String` | — | Date when phone number was first observed |
| `lastObservedDate` | `String` | — | Date when phone number was most recently observed |
| `internalId` | `String` | — | Internal identifier |
| `internalPhoneNumberId` | `String` | — | Internal phone number identifier |
| `operatingLocations` | `PhoneNumberOperatingLocationConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Related operating locations |
| `roles` | `PhoneNumberRoleConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | Associated roles |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | Count of field values |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | Count of distinct field values |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | Check field existence |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | Sum of field values |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | Minimum field value |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | Maximum field value |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | Average of field values |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | Collect field values |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Minimum datetime value |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | Maximum datetime value |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented
- `NodeFunctions`

## Type Membership
- **Member of Edge(s):** `OperatingLocationPhoneNumberEdge`, `RolePhoneNumberEdge`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `OperatingLocation`, `Role`

## Source
https://documentation.enigma.com/reference/graphql_api/objects/phone-number
