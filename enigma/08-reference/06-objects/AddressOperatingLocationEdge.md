# AddressOperatingLocationEdge

## Overview

The `AddressOperatingLocationEdge` represents a Relay edge that wraps an operating location entity along with pagination information, specifically for connections between addresses and operating locations.

## Description

"A Relay edge containing a `AddressOperatingLocation` and its cursor."

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `node` | [`OperatingLocation`](/reference/graphql_api/objects/operating-location) | The item at the end of the edge |
| `cursor` | `String!` | A cursor for use in pagination |
| `id` | `ID` | Identifier for the edge |
| `operatingLocationOperatesAtAddressId` | `UUID` | UUID reference to the operating location-address relationship |
| `datasetIds` | `JSON` | Dataset identifiers associated with the edge |
| `firstObservedDate` | `String` | Initial observation date of the relationship |
| `lastObservedDate` | `String` | Most recent observation date of the relationship |
| `rank` | `Int` | Ranking value for the edge |
| `internalId` | `String` | Internal identifier for the edge |
| `internalOperatingLocationOperatesAtAddressId` | `String` | Internal reference to the location-address relationship |

## Related Types

This object is a member of:
- [`AddressOperatingLocationConnection`](/reference/graphql_api/objects/address-operating-location-connection)

## Usage Context

This edge type is used within pagination results to provide both the operating location data and cursor information needed for traversing address-to-operating-location relationships in the Enigma GraphQL API.
