# RoleOperatingLocationEdge

## Overview
A Relay edge containing a `RoleOperatingLocation` and its cursor for pagination purposes in the Enigma GraphQL API.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | OperatingLocation | — | The item at the end of the edge |
| cursor | String! | — | A cursor for use in pagination |
| id | ID | — | Identifier for the edge |
| roleIsPerformedAtOperatingLocationId | UUID | — | Unique identifier for the role-operating location relationship |
| datasetIds | JSON | — | Collection of dataset identifiers |
| firstObservedDate | String | — | Initial observation date of the relationship |
| lastObservedDate | String | — | Most recent observation date of the relationship |
| rank | Int | — | Ranking value for the relationship |
| internalId | String | — | Internal system identifier |
| internalRoleIsPerformedAtOperatingLocationId | String | — | Internal identifier for the role-operating location relationship |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** RoleOperatingLocationConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** RoleOperatingLocationConnection

## Source
https://documentation.enigma.com/reference/graphql_api/objects/role-operating-location-edge
