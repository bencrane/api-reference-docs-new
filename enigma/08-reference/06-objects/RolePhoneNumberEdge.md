# RolePhoneNumberEdge

## Overview
A Relay edge containing a `RolePhoneNumber` and its cursor for pagination purposes within the Enigma GraphQL API.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | PhoneNumber | — | The item at the end of the edge |
| cursor | String! | — | A cursor for use in pagination |
| id | ID | — | Identifier for the edge |
| roleIsAssociatedWithPhoneNumberId | UUID | — | UUID identifying the role-phone number association |
| datasetIds | JSON | — | Dataset identifiers in JSON format |
| firstObservedDate | String | — | Date when the association was first observed |
| lastObservedDate | String | — | Date when the association was last observed |
| rank | Int | — | Ranking value for the association |
| internalId | String | — | Internal identifier |
| internalRoleIsAssociatedWithPhoneNumberId | String | — | Internal identifier for the role-phone number association |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** RolePhoneNumberConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/role-phone-number-edge
