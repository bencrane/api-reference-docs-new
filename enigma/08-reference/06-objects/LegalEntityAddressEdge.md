# LegalEntityAddressEdge

## Overview
A Relay edge containing a `LegalEntityAddress` and its cursor.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | [`Address`](/reference/graphql_api/objects/address) | — | The item at the end of the edge |
| cursor | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| id | [`ID`](/reference/graphql_api/scalars/id) | — | — |
| legalEntityReceivesMailAtAddressId | [`UUID`](/reference/graphql_api/scalars/uuid) | — | — |
| datasetIds | [`JSON`](/reference/graphql_api/scalars/json) | — | — |
| firstObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | — |
| lastObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | — |
| rank | [`Int`](/reference/graphql_api/scalars/int) | — | — |
| internalId | [`String`](/reference/graphql_api/scalars/string) | — | — |
| internalLegalEntityReceivesMailAtAddressId | [`String`](/reference/graphql_api/scalars/string) | — | — |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** [`LegalEntityAddressConnection`](/reference/graphql_api/objects/legal-entity-address-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-address-edge
