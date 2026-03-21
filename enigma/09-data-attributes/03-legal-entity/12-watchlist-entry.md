# Watchlist Entry

## Description
The OFAC Watchlist Screens attribute enables screening of business entities against U.S. Office of Foreign Assets Control lists, checking individuals and addresses against sanctions databases.

## Tier
Premium

## Applies To
- Brand
- Operating Location
- Legal Entity

## Data Sources

### Specially Designated Nationals and Blocked Persons List (SDN)

### Consolidated Sanctions List (Non-SDN)
- Foreign Sanctions Evaders List (FSE)
- Sectoral Sanctions Identifications List (SSI)
- Palestinian Legislative Council List (PLC)
- Correspondent Account or Payable-Through Account Sanctions (CAPTA)
- Non-SDN Menu-Based Sanctions List (NS-MBS)
- Non-SDN Chinese Military-Industrial Complex Companies List (NS-CMIC)

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Unique identifier |
| watchlistName | String | Name designating which watchlist contains the entry |
| watchlists_match_count | Integer | Count of similarly-named OFAC entities |
| watchlists_match_confidence | Float | Match score (>0.85 threshold) |
| watchlist_entity_watchlist_name | String | Source list designation |
| watchlist_entity_full_name | String | Matching entity's full name |
| watchlist_entity_organization_name | String | Organization name if applicable |
| watchlist_entity_dob | Date | Date of birth when available |
| watchlist_entity_full_address | String | Legal address details |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Screening Process
- Extracts names and addresses from all registration objects tied to a business
- Processes user-supplied data via `persons_to_screen` input array
- Converts names into trigrams for comparison
- Calculates trigram overlap between submitted and watchlist entries
- Default threshold of >0.8 to balance accuracy and false positives

## Performance Metrics
- **With DOB data**: 99.97% true positive rate, 0.4% false positive rate
- **Without DOB data**: 99.97% true positive rate, 5% false positive rate

## Access Requirements
Optional add-on requiring separate activation via sales team. Retrieved using `attrs=watchlist` parameter in API requests.

## Sources
- https://developers.enigma.com/docs/ofac-watchlist-screens
- https://documentation.enigma.com/reference/graphql_api/objects/watchlist-entry
