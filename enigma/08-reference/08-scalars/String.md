# String Scalar Type

## Overview

The `String` scalar type is a fundamental GraphQL type used to represent textual data as UTF-8 character sequences. It serves as the primary GraphQL scalar for handling "free-form human-readable text."

## Definition

```graphql
scalar String
```

## Description

This scalar type handles all text-based data within the Enigma GraphQL API. It processes UTF-8 encoded character sequences and is widely utilized across the schema for representing various text fields.

## Usage Context

The `String` scalar appears extensively throughout the Enigma GraphQL schema, including:

- **Input Types**: Used in inputs like `AddressInput`, `PersonInput`, `SearchInput`, and various configuration objects
- **Object Fields**: Present in objects such as `Account`, `Address`, `Brand`, `LegalEntity`, and many entity-related types
- **Query Parameters**: Utilized in query arguments and search specifications
- **Directives**: Applied with directives like `coalesce`, `trim`, `upper`, `lower`, `join`, and `map` for text transformation and manipulation

## Common Applications

- Business names and entity identifiers
- Address components and location data
- Contact information (emails, phone numbers)
- Search queries and filter conditions
- Configuration and metadata fields
- Mapping and transformation specifications

## Related Documentation

- **Previous**: [JSONString scalar](/reference/graphql_api/scalars/jsonstring)
- **Next**: [UUID scalar](/reference/graphql_api/scalars/uuid)

---

*Last updated: March 11, 2026*
