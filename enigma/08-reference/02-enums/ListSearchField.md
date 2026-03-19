# ListSearchField Enum

## Overview

`ListSearchField` is an enumeration that defines the available fields for searching within lists in the Enigma GraphQL API.

## Values

The enum provides the following search field options:

- **NAME** - Search by entity name
- **PERSON_FIRST_NAME** - Search by a person's first name
- **PERSON_LAST_NAME** - Search by a person's last name
- **WEBSITE** - Search by website URL
- **ADDRESS_STREET1** - Search by primary street address
- **ADDRESS_STREET2** - Search by secondary street address
- **ADDRESS_CITY** - Search by city
- **ADDRESS_STATE** - Search by state
- **ADDRESS_POSTAL_CODE** - Search by postal/ZIP code
- **BRAND_ID** - Search by brand identifier
- **OPERATING_LOCATION_ID** - Search by operating location identifier
- **LEGAL_ENTITY_ID** - Search by legal entity identifier
- **PHONE_NUMBER** - Search by phone number

## Usage Context

This enumeration is utilized by:

- `ColumnMapping` object
- `ColumnMappingInput` input type

These components enable configuration of how data fields map to searchable attributes when working with Enigma's list functionality.
