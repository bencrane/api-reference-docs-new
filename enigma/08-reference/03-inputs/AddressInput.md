# AddressInput

## Overview

`AddressInput` is a GraphQL input type used to specify address information within the Enigma API.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | `ID` | Unique identifier for the address |
| `street1` | `String` | Primary street address line |
| `street2` | `String` | Secondary street address line (e.g., suite or apartment number) |
| `city` | `String` | City name |
| `state` | `String` | State or province code |
| `postalCode` | `String` | Postal or ZIP code |

## Usage Context

`AddressInput` serves as a component within the following input types:

- `PersonInput` — for specifying individual address details
- `SearchFieldGroupInput` — for address-based search parameters
- `SearchInput` — for general search operations involving address data

## Schema Definition

```graphql
input AddressInput {
  id: ID
  street1: String
  street2: String
  city: String
  state: String
  postalCode: String
}
```
