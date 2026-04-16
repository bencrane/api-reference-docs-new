# RoleLegalEntityEdge

## Overview
A Relay edge containing a `RoleLegalEntity` and its cursor, used for pagination in GraphQL queries.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | LegalEntity | — | The item at the end of the edge |
| cursor | String! | — | A cursor for use in pagination |
| id | ID | — | Identifier field |
| legalEntityPerformsRoleId | UUID | — | Unique identifier for the legal entity performing role relationship |
| datasetIds | JSON | — | Collection of dataset identifiers |
| firstObservedDate | String | — | Date when the relationship was first observed |
| lastObservedDate | String | — | Date when the relationship was last observed |
| rank | Int | — | Ranking value |
| internalId | String | — | Internal identifier |
| internalLegalEntityPerformsRoleId | String | — | Internal identifier for the legal entity performing role |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** RoleLegalEntityConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** RoleLegalEntityConnection

## Source
https://documentation.enigma.com/reference/graphql_api/objects/role-legal-entity-edge
