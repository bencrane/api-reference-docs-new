# OperatingLocationRoleEdge

## Overview
A Relay edge containing an `OperatingLocationRole` and its cursor for use in paginated queries.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | Role | — | The item at the end of the edge |
| cursor | String! | — | A cursor for use in pagination |
| id | ID | — | — |
| roleIsPerformedAtOperatingLocationId | UUID | — | — |
| datasetIds | JSON | — | — |
| firstObservedDate | String | — | — |
| lastObservedDate | String | — | — |
| rank | Int | — | — |
| internalId | String | — | — |
| internalRoleIsPerformedAtOperatingLocationId | String | — | — |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** OperatingLocationRoleConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/operating-location-role-edge
