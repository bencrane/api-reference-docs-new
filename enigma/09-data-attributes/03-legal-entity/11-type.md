# Type

## Description
The Legal Entity Type attribute identifies the legal classification of an entity within the U.S. legal system. These are entities which U.S. law recognizes as having an identity and rights—either natural persons or artificial entities such as businesses and governmental bodies.

## Tier
Free

## Applies To
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| legalEntityType | String | The legal form of the entity |
| id | UUID | Unique identifier |
| firstObservedDate | String | When entity was first recorded |
| lastObservedDate | String | Most recent observation timestamp |

## Legal Entity Type Values
- Person
- Sole Proprietorship
- General Partnership
- Limited Partnership
- Corporation
- Professional Corporation
- Limited Liability Company
- Professional Limited Liability Company
- Non-profit Corporation
- Non-profit Limited Liability Company
- Non-profit Limited Partnership
- Co-operative
- Non-profit Co-operative
- Non-stock Co-operative
- Limited Cooperative Association
- Unincorporated Non-profit Association
- Unknown

## Key Distinction
Distinguishes between natural persons (individuals) and artificial business entities

## Sources
- https://documentation.enigma.com/reference/attributes/legal-entity-type
- https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-type

## Last Updated
March 11, 2026
