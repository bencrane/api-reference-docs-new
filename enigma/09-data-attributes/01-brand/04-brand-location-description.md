# Brand Location Description

## Description
Human-readable geographic summary showing top states (multi-location) or specific city/state (single location).

## Tier
Core

## Logic
Shows up to 5 states alphabetically for brands with:
- >10% of locations in that state, OR
- 5+ locations in that state

## Fields

| Field | Type | Description |
|-------|------|-------------|
| locationDescription | String | Geographic summary text |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/brand-location-description
