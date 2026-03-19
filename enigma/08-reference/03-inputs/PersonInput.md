# PersonInput

## Overview

`PersonInput` is a GraphQL input type used to provide personal information for search and verification operations within the Enigma API.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `firstName` | `String` | The person's first name |
| `lastName` | `String` | The person's surname |
| `dateOfBirth` | `String` | The person's date of birth |
| `address` | [`AddressInput`](/reference/graphql_api/inputs/address-input) | Residential or mailing address details |
| `tin` | [`TinInput`](/reference/graphql_api/inputs/tin-input) | Tax identification number information |

## Usage

This input type is utilized by the following GraphQL inputs:

- [`SearchFieldGroupInput`](/reference/graphql_api/inputs/search-field-group-input)
- [`SearchInput`](/reference/graphql_api/inputs/search-input)

These parent inputs allow you to incorporate personal identifying information into broader search and query operations.

---

**Last Updated:** March 11, 2026
