# Operating Location Location Type

## Description
The location type of the operating location, categorizing the operational purpose of a business location.

## Tier
Core

## Applies To
- Operating Location

## Purpose
Distinguishes the business function of physical locations operated by the same entity.

**Example:** Target may have "retail" for customer-facing stores and "office" for employee workspaces.

## Possible Values (15+)
- professional service
- retail
- civic organization
- hospitality
- real estate
- public venue
- headquarters
- office
- trade service
- business service
- scientific
- educational
- supplier
- government
- residential
- manufacturing
- religious
- agriculture
- medical

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| locationType | String | Type of location |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/operating-location-location-type
