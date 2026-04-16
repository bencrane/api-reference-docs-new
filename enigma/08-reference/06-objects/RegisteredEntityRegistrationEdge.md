# RegisteredEntityRegistrationEdge

## Overview
A Relay edge containing a `RegisteredEntityRegistration` and its cursor for use in pagination.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `node` | `Registration` | — | The item at the end of the edge |
| `cursor` | `String!` | — | A cursor for use in pagination |
| `id` | `ID` | — | Identifier |
| `registrationRegisteredRegisteredEntityId` | `UUID` | — | UUID of the registered entity registration relationship |
| `datasetIds` | `JSON` | — | Dataset identifiers |
| `firstObservedDate` | `String` | — | Initial observation date |
| `lastObservedDate` | `String` | — | Most recent observation date |
| `rank` | `Int` | — | Ranking value |
| `internalId` | `String` | — | Internal identifier |
| `internalRegistrationRegisteredRegisteredEntityId` | `String` | — | Internal ID for the registered entity registration relationship |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** `RegisteredEntityRegistrationConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/registered-entity-registration-edge
