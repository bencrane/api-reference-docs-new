# Industry

## Overview
The industry within which a business operates. Multiple classification systems describe business activities (NAICS, GICS, MCC, etc.). Each system has advantages and drawbacks, so Enigma provides multiple classifications. "industry_type indicates the classification system" while "industry_code is the code of a particular industry" and "industry_desc is the human readable description for the industry_code". Additionally, Enigma provides a non-hierarchical enigma_industry_description offering colloquial indication of business primary activity.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| industryDesc | String | — | Human-readable description of the industry corresponding to industry_code per the classification system developer |
| industryCode | String | — | Numeric value of the industry code; null for certain classification systems |
| industryType | String | — | Classification system used (naics_2017_code, naics_2022_code, sic_code, mcc_code, enigma_industry_description) |
| id | UUID! | — | Unique identifier |
| firstObservedDate | String | — | Date when industry was first observed |
| lastObservedDate | String | — | Date when industry was last observed |
| internalId | String | — | Internal identifier |
| internalIndustryId | String | — | Internal industry identifier |
| brands | IndustryBrandConnection | first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions | Connection to related brands |
| parentIndustries | IndustryIndustryConnection | first: Int = 100, last: Int, after: String, before: String, conditions: ConnectionConditions | Connection to parent industries |
| count | Int | field: String!, conditions: Conditions | Count aggregation function |
| countDistinct | Int | field: String!, conditions: Conditions | Count distinct aggregation function |
| has | Boolean | field: String!, conditions: Conditions | Existence check function |
| sum | Int | field: String!, conditions: Conditions | Sum aggregation function |
| min | Int | field: String!, conditions: Conditions | Minimum aggregation function |
| max | Int | field: String!, conditions: Conditions | Maximum aggregation function |
| avg | Float | field: String!, conditions: Conditions | Average aggregation function |
| collect | String | field: String!, separator: String, conditions: Conditions | Collect aggregation function |
| minDateTime | DateTime | field: String!, conditions: Conditions | Minimum datetime aggregation function |
| maxDateTime | DateTime | field: String!, conditions: Conditions | Maximum datetime aggregation function |
| _fn | JSON | — | Internal function metadata |

## Interfaces Implemented
- NodeFunctions

## Type Membership
- **Member of Edge(s):** BrandIndustryEdge, IndustryIndustryEdge
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** IndustryBrandEdge, IndustryIndustryEdge

## Source
https://documentation.enigma.com/reference/graphql_api/objects/industry
