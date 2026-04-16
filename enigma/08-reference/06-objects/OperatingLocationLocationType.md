# OperatingLocationLocationType

## Overview

The location type categorization of an operating location within the Enigma data model. This type represents the functional classification of a specific business location, distinguishing between different operational purposes such as retail establishments, office spaces, headquarters, or service facilities.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| id | UUID! | — | Unique identifier for the location type record |
| firstObservedDate | String | — | Date when this location type was first observed |
| lastObservedDate | String | — | Date when this location type was most recently observed |
| locationType | String | — | "The type of the operating location" |
| internalId | String | — | Internal system identifier |
| internalOperatingLocationId | String | — | Internal reference to parent operating location |
| count | Int | field: String!, conditions: Conditions | Count records matching specified field and conditions |
| countDistinct | Int | field: String!, conditions: Conditions | Count distinct values for specified field |
| has | Boolean | field: String!, conditions: Conditions | Check field existence under conditions |
| sum | Int | field: String!, conditions: Conditions | Sum numeric field values |
| min | Int | field: String!, conditions: Conditions | Find minimum field value |
| max | Int | field: String!, conditions: Conditions | Find maximum field value |
| avg | Float | field: String!, conditions: Conditions | Calculate average field value |
| collect | String | field: String!, separator: String, conditions: Conditions | Aggregate field values into delimited string |
| minDateTime | DateTime | field: String!, conditions: Conditions | Find earliest datetime value |
| maxDateTime | DateTime | field: String!, conditions: Conditions | Find latest datetime value |
| _fn | JSON | — | Function metadata |

## Interfaces Implemented

- NodeFunctions

## Type Membership

- **Member of Edge(s):** OperatingLocationLocationTypeEdge
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** None

## Source

https://documentation.enigma.com/reference/graphql_api/objects/operating-location-location-type
