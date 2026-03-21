# Registered Entity

## Description
Businesses which have become legal entities by registering with a U.S. Secretary of State (SoS). Legal entities must file a registration with each U.S. state where they operate.

## Tier
Premium

## Applies To
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| name | String | Standardized name of the entity from registration |
| registeredEntityType | String | Standardized legal form of the entity |
| formationDate | Date | Earliest non-null issue date from registrations (YYYY-MM-DD) |
| formationYear | Integer | Year (YYYY) of earliest issue date |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Registered Entity Types
- Limited Partnership
- LLC
- Corporation
- Professional Corporation
- Non-profit Corporation
- Sole Proprietorship
- General Partnership
- And others

## Coverage
Enigma sources and standardizes legal entity registrations from all applicable U.S. jurisdictions:
- All 50 states
- District of Columbia
- Puerto Rico

## Default Behavior
By default, up to one registered entity is returned, but more can be returned via the `top_n` parameter

## Data Source
Secretary of State office for each state/region

## Sources
- https://developers.enigma.com/docs/legal-entity
- https://developers.enigma.com/docs/registered-agents
- https://documentation.enigma.com/reference/graphql_api/objects/registered-entity
