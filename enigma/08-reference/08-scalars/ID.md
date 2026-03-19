# ID Scalar Type

## Overview

The `ID` scalar represents a unique identifier in the Enigma GraphQL API. It functions as a mechanism for refetching objects or serving as a cache key within the system.

## Characteristics

**Format in Response:** Appears as a String in JSON responses, though it is not designed for human readability.

**Input Acceptance:** The API accepts multiple input formats:
- String values (e.g., `"4"`)
- Integer values (e.g., `4`)

Both formats are recognized as valid ID inputs.

## Technical Specification

```graphql
scalar ID
```

## Usage Context

The ID scalar is extensively used throughout the Enigma GraphQL schema as a member of numerous objects and inputs, including:

- Entity and account objects (Account, LegalEntity, Person, Brand)
- Edge objects for relationship traversal
- Input types for mutations and queries
- List and materialization operations

This scalar type provides a consistent mechanism for uniquely identifying and referencing entities across the API's complex data graph.

---

**Documentation Last Updated:** March 11, 2026
