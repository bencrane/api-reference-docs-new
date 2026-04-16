# OperatingLocationLegalEntityEdge

## Overview

A Relay edge implementation that encapsulates a `LegalEntity` node along with pagination cursor information, used within the GraphQL API's operating location to legal entity relationship queries.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | LegalEntity | — | The item at the end of the edge |
| cursor | String! | — | A cursor for use in pagination |
| id | ID | — | Identifier for the edge |
| legalEntityOwnsLocationOperatingLocationId | UUID | — | UUID identifying the legal entity's ownership relationship to an operating location |
| datasetIds | JSON | — | JSON representation of associated dataset identifiers |
| firstObservedDate | String | — | Date when this relationship was first observed |
| lastObservedDate | String | — | Date of the most recent observation of this relationship |
| rank | Int | — | Numeric ranking value for the relationship |
| internalId | String | — | Internal identifier for the edge |
| internalLegalEntityOwnsLocationOperatingLocationId | String | — | Internal string identifier for the ownership relationship |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** `OperatingLocationLegalEntityConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `OperatingLocationLegalEntityConnection`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-legal-entity-edge
