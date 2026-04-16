# ReviewSummaryOperatingLocationEdge

## Overview
A Relay edge containing a `ReviewSummaryOperatingLocation` and its cursor for pagination purposes.

## Fields
| Field Name | Type | Arguments | Description |
|---|---|---|---|
| node | OperatingLocation | — | The item at the end of the edge |
| cursor | String! | — | A cursor for use in pagination |
| id | ID | — | Identifier for the edge |
| operatingLocationIsSubjectOfReviewSummaryId | UUID | — | UUID identifier linking operating location to review summary |
| datasetIds | JSON | — | Collection of dataset identifiers in JSON format |
| firstObservedDate | String | — | Date when the record was first observed |
| lastObservedDate | String | — | Date when the record was most recently observed |
| rank | Int | — | Ranking value for the operating location |
| internalId | String | — | Internal identifier for the edge |
| internalOperatingLocationIsSubjectOfReviewSummaryId | String | — | Internal identifier for the relationship |

## Interfaces Implemented
None

## Type Membership
- **Member of Edge(s):** None
- **Member of Connection(s):** ReviewSummaryOperatingLocationConnection
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/review-summary-operating-location-edge
