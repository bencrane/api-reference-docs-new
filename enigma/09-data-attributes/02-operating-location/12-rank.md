# Rank

## Description
Indicates how the card revenue of this operating location compares to other operating locations of the same enigma industry within the geographical area.

## Tier
Plus

## Applies To
- Operating Location

## Geographic Definition
Rankings determined within an H3 index at resolution 4.

## Example
Position of 5 with cohort size of 17 means four nearby pizza restaurants have higher card revenue while twelve have lower revenue.

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| position | Integer | Absolute ranking within the cohort |
| cohortSize | Integer | Total operating locations in comparison group |
| periodStartDate | Date | Start date of ranking period |
| periodEndDate | Date | End date of ranking period |
| period | String | Time window for ranking (currently 12 months) |
| quantityType | String | Metric used for ranking (card revenue) |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Limitations
Rank data unavailable when card revenue cannot be determined or when fewer than ten nearby businesses in the same industry exist locally.

## Source
https://documentation.enigma.com/reference/attributes/operating-location-rank
