# PhoneNumberRoleEdge

## Overview
A Relay edge containing a `PhoneNumberRole` and its cursor for use in paginated queries.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | Role | | The item at the end of the edge |
| cursor | String! | | A cursor for use in pagination |
| id | ID | | Identifier |
| roleIsAssociatedWithPhoneNumberId | UUID | | UUID of the associated phone number role |
| datasetIds | JSON | | Dataset identifiers |
| firstObservedDate | String | | Date when first observed |
| lastObservedDate | String | | Date when last observed |
| rank | Int | | Ranking value |
| internalId | String | | Internal identifier |
| internalRoleIsAssociatedWithPhoneNumberId | String | | Internal ID of associated phone number role |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** PhoneNumberRoleConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** PhoneNumberRoleConnection

## Source
https://documentation.enigma.com/reference/graphql_api/objects/phone-number-role-edge
