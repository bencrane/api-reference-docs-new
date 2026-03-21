# Review Summary

## Description
Summary of publicly available customer reviews for this entity.

## Tier
Plus

## Applies To
- Operating Location

## Time Series Structure
- **Rank 0** = Most recent review summary
- **Higher ranks** = Older periods

## Data Sources
Publicly available customer assessments, refreshed at least monthly.

## Key Insight
"Healthy businesses will have a steadily increasing number of reviews overtime" - review velocity serves as a business health indicator.

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| firstReviewDate | String | Date of earliest available review (from sample of 100 reviews) |
| lastReviewDate | String | Date of latest review; may lag up to 3 months |
| reviewCount | Integer | Number of submitted reviews |
| reviewScoreAvg | Float | Weighted average of reviews submitted during location's lifetime |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/review-summary
