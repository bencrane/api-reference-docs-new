# Phone Number

## Description
The Phones attribute contains phone number(s) linked to a business or specific business location.

## Tier
Core

## Applies To
- Brand
- Operating Location
- Legal Entity

## Format
Twelve-digit NANP-compliant format starting with "+1" (e.g., "+18005102856")

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| phoneNumber | String | Twelve-digit NANP-compliant phone number |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Coverage
- Business Level: 60%
- Business Locations: 69%

## Data Sources
- Card transaction panel
- Third-party verification services
- Public online directories

## Data Characteristics
- Current snapshot only (no historical tracking)
- Numbers ranked by prevalence across underlying sources
- Must have valid U.S. area code to be included

## Usage
- Primary phone number serves as verification tool for business identification
- Location-specific numbers for multi-location enterprises

## Sources
- https://developers.enigma.com/docs/phone-numbers
- https://documentation.enigma.com/reference/graphql_api/objects/phone-number
