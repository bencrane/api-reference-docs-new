# Role

## Overview
These are roles which people (and other legal entities) hold at U.S. businesses.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `externalId` | `JSON` | — | External identifier |
| `externalUrl` | `String` | — | External URL reference |
| `id` | `UUID!` | — | Unique identifier (required) |
| `firstObservedDate` | `String` | — | Date role was first observed |
| `lastObservedDate` | `String` | — | Date role was last observed |
| `jobTitle` | `String` | — | Standardized job title with normalization applied (lowercase, expanded abbreviations, accents removed) |
| `jobFunction` | `String` | — | Standardized job function/description (e.g., "Accounting", "Contracts") in lowercase |
| `managementLevel` | `String` | — | Standardized management level: governance roles (owner, founder, board of directors) or functional roles (head, c-suite, director-level, vp-level, manager, non-manager), or null |
| `internalId` | `String` | — | Internal identifier |
| `internalRoleId` | `String` | — | Internal role identifier |
| `operatingLocations` | `RoleOperatingLocationConnection` | `first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions` | Related operating locations |
| `phoneNumbers` | `RolePhoneNumberConnection` | `first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions` | Associated phone numbers |
| `emailAddresses` | `RoleEmailAddressConnection` | `first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions` | Associated email addresses |
| `legalEntities` | `RoleLegalEntityConnection` | `first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions` | Related legal entities |
| `registrations` | `RoleRegistrationConnection` | `first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions` | Associated registrations |
| `brands` | `RoleBrandConnection` | `first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions` | Related brands |
| `count` | `Int` | `field: String!, conditions: Conditions` | Count aggregation function |
| `countDistinct` | `Int` | `field: String!, conditions: Conditions` | Count distinct aggregation function |
| `has` | `Boolean` | `field: String!, conditions: Conditions` | Check field existence |
| `sum` | `Int` | `field: String!, conditions: Conditions` | Sum aggregation function |
| `min` | `Int` | `field: String!, conditions: Conditions` | Minimum aggregation function |
| `max` | `Int` | `field: String!, conditions: Conditions` | Maximum aggregation function |
| `avg` | `Float` | `field: String!, conditions: Conditions` | Average aggregation function |
| `collect` | `String` | `field: String!, separator: String, conditions: Conditions` | Collect values with separator |
| `minDateTime` | `DateTime` | `field: String!, conditions: Conditions` | Minimum datetime aggregation |
| `maxDateTime` | `DateTime` | `field: String!, conditions: Conditions` | Maximum datetime aggregation |
| `_fn` | `JSON` | — | Function metadata |

## Interfaces Implemented
- `NodeFunctions`

## Type Membership
- **Member of Edge(s):** `BrandRoleEdge`, `EmailAddressRoleEdge`, `LegalEntityRoleEdge`, `OperatingLocationRoleEdge`, `PhoneNumberRoleEdge`, `RegistrationRoleEdge`
- **Member of Connection(s):** None explicitly documented
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** Various connection/edge types

## Source
https://documentation.enigma.com/reference/graphql_api/objects/role
