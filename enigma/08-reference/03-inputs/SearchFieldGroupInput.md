# SearchFieldGroupInput

## Overview

`SearchFieldGroupInput` is a GraphQL input type used for constructing search queries within the Enigma API. It aggregates multiple data fields to enable comprehensive entity searches.

## Fields

| Field | Type | Purpose |
|-------|------|---------|
| `name` | String | Business or entity name |
| `address` | AddressInput | Physical location details |
| `person` | PersonInput | Individual contact information |
| `phoneNumber` | String | Contact telephone number |
| `website` | String | Web domain or URL |
| `tin` | TinInput | Tax identification number |
| `id` | String | Unique identifier |

## Schema Definition

```graphql
input SearchFieldGroupInput {
  name: String
  address: AddressInput
  person: PersonInput
  phoneNumber: String
  website: String
  tin: TinInput
  id: String
}
```

## Usage Context

This input type serves as a component within the `SearchInput` type, enabling structured queries across Enigma's business and identity data sources.

## Related Types

- **AddressInput** — Handles geographical location data
- **PersonInput** — Manages individual/contact details
- **TinInput** — Processes tax identification information
- **SearchInput** — Parent input type containing this field group
