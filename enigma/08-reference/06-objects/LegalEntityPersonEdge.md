# LegalEntityPersonEdge

## Overview
A Relay edge containing a `LegalEntityPerson` and its cursor for use in pagination.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | `Person` | — | The item at the end of the edge |
| cursor | `String!` | — | A cursor for use in pagination |
| id | `ID` | — | Identifier for the edge |
| personIsInstanceOfLegalEntityId | `UUID` | — | UUID identifier linking person to legal entity |
| datasetIds | `JSON` | — | Dataset identifiers in JSON format |
| firstObservedDate | `String` | — | Date when the relationship was first observed |
| lastObservedDate | `String` | — | Date when the relationship was last observed |
| rank | `Int` | — | Ranking value for the relationship |
| internalId | `String` | — | Internal identifier for the edge |
| internalPersonIsInstanceOfLegalEntityId | `String` | — | Internal string identifier for person-entity link |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** `LegalEntityPersonConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-person-edge
