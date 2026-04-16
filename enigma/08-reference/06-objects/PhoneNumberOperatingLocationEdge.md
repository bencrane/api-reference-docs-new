# PhoneNumberOperatingLocationEdge

## Overview

A Relay edge containing a `PhoneNumberOperatingLocation` and its cursor for pagination purposes within the GraphQL API.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | [`OperatingLocation`](/reference/graphql_api/objects/operating-location) | — | The item at the end of the edge |
| cursor | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| id | [`ID`](/reference/graphql_api/scalars/id) | — | No description |
| operatingLocationCanBeCalledAtPhoneNumberId | [`UUID`](/reference/graphql_api/scalars/uuid) | — | No description |
| datasetIds | [`JSON`](/reference/graphql_api/scalars/json) | — | No description |
| firstObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| lastObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| rank | [`Int`](/reference/graphql_api/scalars/int) | — | No description |
| internalId | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| internalOperatingLocationCanBeCalledAtPhoneNumberId | [`String`](/reference/graphql_api/scalars/string) | — | No description |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** [`PhoneNumberOperatingLocationConnection`](/reference/graphql_api/objects/phone-number-operating-location-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/phone-number-operating-location-edge
