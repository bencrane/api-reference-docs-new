# EmailAddressRoleEdge

## Overview
A Relay edge containing an `EmailAddressRole` and its cursor for use in paginated queries.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | [`Role`](/reference/graphql_api/objects/role) | — | The item at the end of the edge |
| cursor | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| id | [`ID`](/reference/graphql_api/scalars/id) | — | (No description) |
| roleIsAssociatedWithEmailAddressId | [`UUID`](/reference/graphql_api/scalars/uuid) | — | (No description) |
| datasetIds | [`JSON`](/reference/graphql_api/scalars/json) | — | (No description) |
| firstObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | (No description) |
| lastObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | (No description) |
| rank | [`Int`](/reference/graphql_api/scalars/int) | — | (No description) |
| internalId | [`String`](/reference/graphql_api/scalars/string) | — | (No description) |
| internalRoleIsAssociatedWithEmailAddressId | [`String`](/reference/graphql_api/scalars/string) | — | (No description) |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** [`EmailAddressRoleConnection`](/reference/graphql_api/objects/email-address-role-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/email-address-role-edge
