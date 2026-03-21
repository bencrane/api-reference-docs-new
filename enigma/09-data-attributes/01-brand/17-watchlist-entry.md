# Watchlist Entry

## Description
Entities flagged by OFAC (Office of Foreign Assets Control).

## Tier
Premium

## Data Sources
- **SDN List** (Specially Designated Nationals)
- **Consolidated Sanctions List**:
  - FSE (Foreign Sanctions Evaders)
  - SSI (Sectoral Sanctions Identifications)
  - PLC (Palestinian Legislative Council)
  - CAPTA (Correspondent Account or Payable-Through Account)
  - NS-MBS (Non-SDN Menu-Based Sanctions)
  - NS-CMIC (Non-SDN Chinese Military-Industrial Complex)

## Fields

| Field | Type | Description |
|-------|------|-------------|
| watchlistName | String | Name of the watchlist |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/watchlist-entry
