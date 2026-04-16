# OperatingLocationBrandEdge

## Overview

A Relay edge containing an `OperatingLocationBrand` and its cursor for pagination purposes within the Enigma GraphQL API.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | Brand | | The item at the end of the edge |
| cursor | String! | | A cursor for use in pagination |
| id | ID | | Identifier for the edge |
| brandOperatesAtOperatingLocationId | UUID | | Unique identifier for the brand-operating location relationship |
| datasetIds | JSON | | Dataset identifiers associated with the relationship |
| firstObservedDate | String | | Date when the relationship was first observed |
| lastObservedDate | String | | Date when the relationship was most recently observed |
| rank | Int | | Ranking value for the relationship |
| internalId | String | | Internal identifier for the edge |
| internalBrandOperatesAtOperatingLocationId | String | | Internal identifier for the brand-operating location relationship |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** `OperatingLocationBrandConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `OperatingLocationBrandConnection`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-brand-edge
