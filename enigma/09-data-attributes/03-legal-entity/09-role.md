# Role

## Description
The Role object represents positions held by people and other legal entities at U.S. businesses. It identifies individuals connected to a business or business location along with their organizational roles.

## Tier
Plus

## Applies To
- Brand
- Operating Location
- Legal Entity

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier |
| name | String | Full name of the person associated with the business |
| jobTitle | String | A job title observed in datasets of roles and employee contacts |
| jobFunction | String | Standardized job category (e.g., Accounting, Contracts) |
| managementLevel | String | Hierarchical position level (e.g., "C-level") |
| department | String | Functional area (e.g., "C-Suite") |
| externalId | JSON | External reference identifier |
| externalUrl | String | External URL reference |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Coverage
- Business level: 44%
- Business Location level: 44%

## Data Sources
- Secretary of State corporate filings
- Third-party verification services
- Public business directories

## Methodology
Individuals ranked by prevalence across data sources and by number of titles, helping identify key decision-makers

## Time Structure
Current snapshot only (no historical tracking)

## Sources
- https://developers.enigma.com/docs/associated-people
- https://documentation.enigma.com/reference/graphql_api/objects/role
