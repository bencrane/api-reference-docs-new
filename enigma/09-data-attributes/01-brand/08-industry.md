# Industry

## Description
The industry within which the business operates, using multiple classification systems.

## Tier
Core

## Classification Systems
- **NAICS** (2017, 2022) - North American Industry Classification System
- **SIC** - Standard Industrial Classification
- **MCC** - Merchant Category Code
- **GICS** - Global Industry Classification Standard
- **Enigma** - Proprietary industry descriptions

## Data Sources
- Company websites
- Industry associations
- Card transaction data

## Fields

| Field | Type | Description |
|-------|------|-------------|
| industryType | String | Classification system type (NAICS, SIC, MCC, GICS, Enigma) |
| industryCode | String | Industry code within the classification system |
| industryDesc | String | Human-readable industry description |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/industry
