# LegalEntityTinEdge

## Overview
A Relay edge containing a `LegalEntityTin` and its cursor for use in pagination.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | `Tin` | — | The item at the end of the edge |
| cursor | `String!` | — | A cursor for use in pagination |
| id | `ID` | — | Identifier |
| legalEntityFilesTaxesUsingTinId | `UUID` | — | Legal entity files taxes using TIN identifier |
| rank | `Int` | — | Ranking value |
| verificationStatus | `String` | — | Status of verification |
| verificationResult | `String` | — | Result of verification |
| datasetIds | `JSON` | — | Dataset identifiers |
| firstObservedDate | `String` | — | Date first observed |
| lastObservedDate | `String` | — | Date last observed |
| internalId | `String` | — | Internal identifier |
| internalLegalEntityFilesTaxesUsingTinId | `String` | — | Internal legal entity files taxes using TIN identifier |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** `LegalEntityTinConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `LegalEntityTinConnection`

## Source
https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-tin-edge
