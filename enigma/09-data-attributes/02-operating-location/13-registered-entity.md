# Registered Entity

## Description
Businesses which have become legal entities by registering with a U.S. Secretary of State (SoS).

## Tier
Premium

## Applies To
- Legal Entity (through Operating Location relationships)

## Data Source
Each state's Secretary of State maintains the authoritative records.

## Approach
Consolidates registrations across states, joining domestic registrations (formed in one state) with foreign registrations (formed elsewhere but operating in other states).

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| name | String | Standardized entity name from registration records |
| registeredEntityType | String | Legal structure (e.g., Corporation, LLC) |
| formationDate | String | Earliest issue date (YYYY-MM-DD format) |
| formationYear | Integer | Year of earliest registration (YYYY) |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/registered-entity
