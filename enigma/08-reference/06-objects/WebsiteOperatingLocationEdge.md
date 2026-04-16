# WebsiteOperatingLocationEdge

## Overview
A Relay edge containing a `WebsiteOperatingLocation` and its cursor for pagination purposes.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `node` | `OperatingLocation` | — | The item at the end of the edge |
| `cursor` | `String!` | — | A cursor for use in pagination |
| `id` | `ID` | — | Identifier field |
| `operatingLocationOperatesWebsiteWebsiteId` | `UUID` | — | Website identifier for the operating location relationship |
| `datasetIds` | `JSON` | — | Dataset identifiers in JSON format |
| `firstObservedDate` | `String` | — | Date when relationship was first observed |
| `lastObservedDate` | `String` | — | Date when relationship was last observed |
| `rank` | `Int` | — | Ranking value |
| `internalId` | `String` | — | Internal identifier |
| `internalOperatingLocationOperatesWebsiteWebsiteId` | `String` | — | Internal website identifier for the operating location relationship |

## Interfaces Implemented
None.

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** `WebsiteOperatingLocationConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `WebsiteOperatingLocationConnection`

## Source
https://documentation.enigma.com/reference/graphql_api/objects/website-operating-location-edge
