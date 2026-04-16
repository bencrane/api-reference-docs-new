# RegistrationAddressEdge

## Overview

A Relay edge containing a `RegistrationAddress` and its cursor for pagination purposes.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `node` | `Address` | — | The item at the end of the edge |
| `cursor` | `String!` | — | A cursor for use in pagination |
| `registrationRecordedAddressId` | `UUID` | — | Unique identifier for the registration recorded address |
| `addressType` | `String` | — | Type classification of the address |
| `rank` | `Int` | — | Ranking value for the address |
| `id` | `ID` | — | Unique identifier |
| `datasetIds` | `JSON` | — | Dataset identifiers associated with the record |
| `firstObservedDate` | `String` | — | Date when the address was first observed |
| `lastObservedDate` | `String` | — | Date when the address was most recently observed |
| `internalId` | `String` | — | Internal system identifier |
| `internalRegistrationRecordedAddressId` | `String` | — | Internal identifier for registration recorded address |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** `RegistrationAddressConnection`
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/registration-address-edge
