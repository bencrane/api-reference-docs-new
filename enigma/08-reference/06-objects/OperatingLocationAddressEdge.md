# OperatingLocationAddressEdge

## Overview

A Relay edge containing an `OperatingLocationAddress` and its cursor for pagination purposes within the GraphQL API.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | `Address` | — | The item at the end of the edge |
| cursor | `String!` | — | A cursor for use in pagination |
| id | `ID` | — | No description |
| operatingLocationOperatesAtAddressId | `UUID` | — | No description |
| datasetIds | `JSON` | — | No description |
| firstObservedDate | `String` | — | No description |
| lastObservedDate | `String` | — | No description |
| rank | `Int` | — | No description |
| internalId | `String` | — | No description |
| internalOperatingLocationOperatesAtAddressId | `String` | — | No description |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** `OperatingLocationAddressConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `OperatingLocationAddressConnection`

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-address-edge
