# LegalEntityRegisteredEntityEdge

## Overview
A Relay edge containing a `LegalEntityRegisteredEntity` and its cursor for pagination purposes in the GraphQL API.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `node` | `RegisteredEntity` | — | The item at the end of the edge |
| `cursor` | `String!` | — | A cursor for use in pagination |
| `id` | `ID` | — | Identifier for the edge |
| `registeredEntityIsInstanceOfLegalEntityId` | `UUID` | — | UUID linking registered entity to legal entity instance |
| `datasetIds` | `JSON` | — | JSON data containing dataset identifiers |
| `firstObservedDate` | `String` | — | Date when the relationship was first observed |
| `lastObservedDate` | `String` | — | Date when the relationship was last observed |
| `rank` | `Int` | — | Ranking value for the relationship |
| `internalId` | `String` | — | Internal identifier |
| `internalRegisteredEntityIsInstanceOfLegalEntityId` | `String` | — | Internal identifier linking entities |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** `LegalEntityRegisteredEntityConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-registered-entity-edge
