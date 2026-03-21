# Attribute: Is Marketable (Brand)

**Entity Types:** Brand  
**Tier:** Core

## Description
Contains a boolean value indicating whether the brand is marketable.

## Data Sources
A brand is considered marketable if it meets certain criteria, like:
- Having open locations
- Revenue in the last 12 months
- Reviews in the last 12 months

## Data Fields

| FIELD NAME         | LABEL               | DESCRIPTION                                                              | DATA TYPE | TIER |
|-------------------|---------------------|--------------------------------------------------------------------------|-----------|------|
| firstObservedDate | First Observed Date |                                                                          | String    | Core |
| id                | ID                  |                                                                          | UUID!     | Core |
| isMarketable      | Is Marketable       | Boolean indicating whether the brand is marketable.                      | Boolean   | Core |
| lastObservedDate  | Last Observed Date  |                                                                          | String    | Core |