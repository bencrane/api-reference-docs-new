# RoleRegistrationEdge

## Overview

A Relay edge containing a `RoleRegistration` and its cursor for pagination purposes within the Enigma GraphQL API.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | Registration | — | The item at the end of the edge |
| cursor | String! | — | A cursor for use in pagination |
| id | ID | — | Unique identifier |
| registrationRecordedRoleId | UUID | — | UUID of the registration recorded role |
| datasetIds | JSON | — | Dataset identifiers in JSON format |
| firstObservedDate | String | — | Date when first observed |
| lastObservedDate | String | — | Date when last observed |
| rank | Int | — | Ranking value |
| internalId | String | — | Internal identifier |
| internalRegistrationRecordedRoleId | String | — | Internal registration recorded role identifier |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** RoleRegistrationConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** RoleRegistrationConnection

## Source

https://documentation.enigma.com/reference/graphql_api/objects/role-registration-edge
