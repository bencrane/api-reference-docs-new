# Registration

## Overview

Business registrations filed with a Secretary of State (or equivalent) in a U.S. state or territory. These registrations either create a legal entity in that state ("domestic" registrations) or allow an existing entity to do business in that state ("foreign" registrations). They are a source of truth about that business.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `id` | `UUID!` | — | — |
| `firstObservedDate` | `String` | — | — |
| `lastObservedDate` | `String` | — | — |
| `registrationType` | `String` | — | The legal form of the registered entity, as given by the registering jurisdiction's Secretary of State. |
| `expirationDate` | `Date` | — | The registration's expiration, if any. |
| `registrationState` | `String` | — | The US state where the registration was filed. |
| `jurisdictionType` | `String` | — | `foreign` if the registration is for any state other than the business's home state; otherwise, `domestic`. |
| `homeJurisdictionState` | `String` | — | Two-letter abbreviation for the state jurisdiction of the business. |
| `registeredName` | `String` | — | Business name as on the registration filing. |
| `fileNumber` | `String` | — | File number of the registration filing. |
| `issueDate` | `Date` | — | Issue date of the registration filing, formatted YYYY/MM/DD. |
| `status` | `String` | — | Status field indicating whether the registration is active or inactive. |
| `subStatus` | `String` | — | Normalized sub-status for the business. Values: good_standing, not_good_standing, pending_active, pending_inactive, unknown, null. |
| `statusDetail` | `String` | — | Official filing status message provided by the state, if available. |
| `internalId` | `String` | — | — |
| `internalRegistrationId` | `String` | — | — |
| `addresses` | `RegistrationAddressConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `roles` | `RegistrationRoleConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `registeredEntities` | `RegistrationRegisteredEntityConnection` | `first: Int = 100`, `last: Int`, `after: String`, `before: String`, `conditions: ConnectionConditions` | — |
| `count` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `countDistinct` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `has` | `Boolean` | `field: String!`, `conditions: Conditions` | — |
| `sum` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `min` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `max` | `Int` | `field: String!`, `conditions: Conditions` | — |
| `avg` | `Float` | `field: String!`, `conditions: Conditions` | — |
| `collect` | `String` | `field: String!`, `separator: String`, `conditions: Conditions` | — |
| `minDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | — |
| `maxDateTime` | `DateTime` | `field: String!`, `conditions: Conditions` | — |
| `_fn` | `JSON` | — | — |

## Interfaces Implemented

- `NodeFunctions`

## Type Membership

- **Member of Edge(s):** AddressRegistrationEdge, RegisteredEntityRegistrationEdge, RoleRegistrationEdge
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** RegistrationAddressConnection, RegistrationRoleConnection, RegistrationRegisteredEntityConnection

## Source

https://documentation.enigma.com/reference/graphql_api/objects/registration
