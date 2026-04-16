# LegalEntityOperatingLocationEdge

## Overview
A Relay edge containing an `OperatingLocation` node and its associated cursor for pagination purposes within the GraphQL API.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | OperatingLocation | — | The item at the end of the edge |
| cursor | String! | — | A cursor for use in pagination |
| id | ID | — | Identifier for the edge |
| legalEntityOwnsLocationOperatingLocationId | UUID | — | UUID identifier for the legal entity-operating location relationship |
| datasetIds | JSON | — | JSON data containing dataset identifiers |
| firstObservedDate | String | — | Date when the relationship was first observed |
| lastObservedDate | String | — | Date when the relationship was last observed |
| rank | Int | — | Ranking value for the operating location |
| internalId | String | — | Internal identifier for the edge |
| internalLegalEntityOwnsLocationOperatingLocationId | String | — | Internal string identifier for the relationship |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** LegalEntityOperatingLocationConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-operating-location-edge
