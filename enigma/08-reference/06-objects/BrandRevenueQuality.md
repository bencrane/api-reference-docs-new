# BrandRevenueQuality

## Overview
Warnings and issues related to the revenue of a brand, including detection of unusual revenue patterns or quality concerns.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| id | UUID! | — | Unique identifier for the revenue quality record |
| firstObservedDate | String | — | Date when the revenue issue was first detected |
| lastObservedDate | String | — | Date of the most recent observation of the issue |
| issueReason | String | — | "The reason for the revenue quality issue" including scenarios like revenue drops to 0%, drops to 20%, or increases to 250% |
| issueSeverity | String | — | Classification of issue severity level (e.g., HIGH, MEDIUM) |
| issueDescription | String | — | "A description of the revenue quality issue" in human-readable format |
| internalId | String | — | Internal system identifier |
| internalBrandId | String | — | Internal brand reference identifier |
| count | Int | field: String!, conditions: Conditions | Count of records matching specified field and conditions |
| countDistinct | Int | field: String!, conditions: Conditions | Count of distinct values for a field |
| has | Boolean | field: String!, conditions: Conditions | Check if field exists under conditions |
| sum | Int | field: String!, conditions: Conditions | Sum of values for a field |
| min | Int | field: String!, conditions: Conditions | Minimum value for a field |
| max | Int | field: String!, conditions: Conditions | Maximum value for a field |
| avg | Float | field: String!, conditions: Conditions | Average value for a field |
| collect | String | field: String!, separator: String, conditions: Conditions | Collect and concatenate field values |
| minDateTime | DateTime | field: String!, conditions: Conditions | Minimum date/time value |
| maxDateTime | DateTime | field: String!, conditions: Conditions | Maximum date/time value |
| _fn | JSON | — | Internal function metadata |

## Interfaces Implemented
- NodeFunctions

## Type Membership
- **Member of Edge(s):** BrandRevenueQualityEdge
- **Member of Connection(s):** None directly listed
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source
https://documentation.enigma.com/reference/graphql_api/objects/brand-revenue-quality
