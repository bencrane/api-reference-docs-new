# TinLegalEntityEdge

## Overview

A Relay edge containing a `TinLegalEntity` and its cursor.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | [`LegalEntity`](/reference/graphql_api/objects/legal-entity) | — | The item at the end of the edge |
| cursor | [`String!`](/reference/graphql_api/scalars/string) | — | A cursor for use in pagination |
| id | [`ID`](/reference/graphql_api/scalars/id) | — | No description |
| legalEntityFilesTaxesUsingTinId | [`UUID`](/reference/graphql_api/scalars/uuid) | — | No description |
| rank | [`Int`](/reference/graphql_api/scalars/int) | — | No description |
| verificationStatus | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| verificationResult | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| datasetIds | [`JSON`](/reference/graphql_api/scalars/json) | — | No description |
| firstObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| lastObservedDate | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| internalId | [`String`](/reference/graphql_api/scalars/string) | — | No description |
| internalLegalEntityFilesTaxesUsingTinId | [`String`](/reference/graphql_api/scalars/string) | — | No description |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** [`TinLegalEntityConnection`](/reference/graphql_api/objects/tin-legal-entity-connection)
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/tin-legal-entity-edge
