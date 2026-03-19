# TinInput

## Overview

The `TinInput` type is a GraphQL input object used to specify Tax Identification Number (TIN) information when querying the Enigma API.

## Fields

### `tin`
- **Type:** `String`
- **Description:** The Tax Identification Number value

### `tinType`
- **Type:** `TinType` enum
- **Description:** The category or classification of the TIN being provided

## Usage Context

This input type is utilized as a component within several parent input objects:

- `PersonInput` — for individual person identification
- `SearchFieldGroupInput` — for advanced search field configurations
- `SearchInput` — for primary search operations

## Notes

The `TinInput` structure enables API users to provide both the identification number itself and specify what variety of TIN is being submitted, ensuring accurate matching and verification processes.
