# Operating Location Revenue Quality

## Description
Warnings and issues related to the revenue of this operating location.

## Tier
Plus

## Applies To
- Operating Location

## Issue Categories

### High Severity
- Revenue extrapolation exceeding 100x multiplier thresholds
- Complete revenue drops despite open operating status
- Closed locations still showing positive transactions
- Extreme revenue spikes (250%+ increases)
- Revenue substantially exceeding peer location benchmarks

### Medium Severity
- Significant revenue concentration
- Revenue drops with unknown location status
- Performance exceeding 99th percentile within industry classification

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| issueDescription | String | Explanation of the specific revenue quality problem |
| issueReason | String | Categorical reason for the issue |
| issueSeverity | String | High or medium severity classification |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/operating-location-revenue-quality
