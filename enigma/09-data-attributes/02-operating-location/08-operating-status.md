# Operating Status

## Description
Indicates whether a location is actively functioning ('Open'), out of operation ('Temporarily Closed', 'Closed'), or of uncertain status ('Unknown').

## Tier
Core

## Applies To
- Operating Location

## Status Values

| Status | Description |
|--------|-------------|
| Open | Verified as operational through credible evidence or manual validation |
| Temporarily Closed | Data confirms temporary cessation of operations |
| Closed | Confirmed permanent closure |
| Unknown | Insufficient information to determine operational status |

## Time Series Structure
Each entry represents a continuous period with the same status:
- **Rank 0** = Most recent observation
- **Higher ranks** = Older records

## Data Collection
At least quarterly, frequently more often.

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| operatingStatus | String | Current status (Open/Temporarily Closed/Closed/Unknown) |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/operating-location-operating-status
