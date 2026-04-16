# OperatingLocationReviewSummaryEdge

## Overview

A Relay edge containing an `OperatingLocationReviewSummary` and its cursor for pagination purposes.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `node` | `ReviewSummary` | — | The item at the end of the edge |
| `cursor` | `String!` | — | A cursor for use in pagination |
| `id` | `ID` | — | No description |
| `operatingLocationIsSubjectOfReviewSummaryId` | `UUID` | — | No description |
| `datasetIds` | `JSON` | — | No description |
| `firstObservedDate` | `String` | — | No description |
| `lastObservedDate` | `String` | — | No description |
| `rank` | `Int` | — | No description |
| `internalId` | `String` | — | No description |
| `internalOperatingLocationIsSubjectOfReviewSummaryId` | `String` | — | No description |

## Interfaces Implemented

None

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** `OperatingLocationReviewSummaryConnection`
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-review-summary-edge
