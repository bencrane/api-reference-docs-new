# Watchlist Entry

## Description
Identifies entities appearing on watchlists maintained by the Office of Foreign Assets Control (OFAC).

## Tier
Premium

## Applies To
- Brand
- Operating Location
- Legal Entity

## Data Sources

### Specially Designated Nationals and Blocked Persons List (SDN)

### Consolidated Sanctions List (Non-SDN)
- Foreign Sanctions Evaders List
- Sectoral Sanctions Identifications List
- Palestinian Legislative Council List
- Correspondent account sanctions lists
- Non-SDN Menu-Based Sanctions List
- Non-SDN Chinese Military-Industrial Complex Companies List

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| watchlistName | String | Identifies which list (SDN or Non-SDN variants) |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/watchlist-entry
