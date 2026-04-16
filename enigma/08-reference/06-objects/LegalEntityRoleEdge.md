# LegalEntityRoleEdge

## Overview
A Relay edge containing a `LegalEntityRole` and its cursor for pagination purposes.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | Role | None | The item at the end of the edge |
| cursor | String! | None | A cursor for use in pagination |
| id | ID | None | No description |
| legalEntityPerformsRoleId | UUID | None | No description |
| datasetIds | JSON | None | No description |
| firstObservedDate | String | None | No description |
| lastObservedDate | String | None | No description |
| rank | Int | None | No description |
| internalId | String | None | No description |
| internalLegalEntityPerformsRoleId | String | None | No description |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** LegalEntityRoleConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** LegalEntityRoleConnection

## Source
https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-role-edge
