# Name

## Description
The Legal Entity Name attribute identifies entities which U.S. law recognizes as having an identity and rights, encompassing both natural persons and artificial entities such as businesses and governmental bodies.

## Tier
Free

## Applies To
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| name | String | The legal entity's name |
| legalEntityType | String | Describes the entity's legal structure |
| id | UUID | Unique identifier |
| firstObservedDate | String | When entity name was initially documented |
| lastObservedDate | String | Most recent observation |

## Legal Entity Type Values
- "Person" for individuals
- Various business/organizational legal forms (Corporation, LLC, etc.)

## Sources
- https://documentation.enigma.com/reference/attributes/legal-entity-name
- https://documentation.enigma.com/reference/graphql_api/objects/legal-entity-name

## Last Updated
March 11, 2026
