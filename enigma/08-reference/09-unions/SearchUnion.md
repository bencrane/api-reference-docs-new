# SearchUnion

## Overview

The `SearchUnion` is a GraphQL union type that represents multiple possible entity types returned by search and enrichment operations within the Enigma API.

## Definition

```graphql
union SearchUnion = LegalEntity | Brand | OperatingLocation | Person | Address
```

## Possible Types

The `SearchUnion` can resolve to any of the following object types:

- **LegalEntity** - Represents a registered business entity with legal standing
- **Brand** - Represents a brand or trade name associated with a business
- **OperatingLocation** - Represents a physical location where a business operates
- **Person** - Represents an individual entity
- **Address** - Represents a physical street address

### Address Details

When an Address type is returned, it conforms to standards outlined in USPS Publication 28 where applicable. The address information may include:

- Specific street address with unit numbers (when available)
- Postal code or city/state combinations
- Distinct entries for multiple units within the same building

## Usage Context

### Returned By

The `SearchUnion` type is returned by:
- [`enrich`](/reference/graphql_api/queries/enrich) query
- [`search`](/reference/graphql_api/queries/search) query

### Member Of

This union is utilized within:
- `CreateList` object
- `UpdateList` object
