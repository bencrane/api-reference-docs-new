# EntityType Enum

## Overview

`EntityType` is an enumeration used in the Enigma GraphQL API to classify different types of entities within the system.

## Definition

```graphql
enum EntityType {
  BRAND
  OPERATING_LOCATION
  LEGAL_ENTITY
  PERSON
  ADDRESS
}
```

## Values

The enumeration includes five possible values:

- **BRAND** - Represents a brand entity
- **OPERATING_LOCATION** - Represents a physical or operational location
- **LEGAL_ENTITY** - Represents a legally recognized business entity
- **PERSON** - Represents an individual person
- **ADDRESS** - Represents a physical address

## Usage

The `EntityType` enum is used as a member of several GraphQL components:

- `attributeGroups` query
- `EnrichmentInput` input type
- `EntityIdentifier` input type
- `ListSearchInput` object
- `ListSearchInputInput` input type
- `SearchInput` input type

This enum enables precise categorization when querying or filtering entities within the Enigma data platform.
