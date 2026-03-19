# UUID Scalar Type

## Overview

The UUID scalar type provides native UUID object support within the Enigma GraphQL API. It leverages Python's internal UUID implementation (`uuid.UUID`) to handle universally unique identifiers in fields, resolvers, and input parameters.

## Definition

```graphql
scalar UUID
```

## Description

This scalar enables seamless handling of UUID values throughout GraphQL operations. The implementation uses Python's native UUID module to ensure proper validation and serialization of UUID objects.

## Usage

The UUID scalar is utilized across numerous entity types and edge definitions within the Enigma GraphQL schema, including:

- Entity objects (Address, Brand, LegalEntity, OperatingLocation, Person, etc.)
- Edge relationships (connecting related entities)
- Supporting objects (PhoneNumber, EmailAddress, Website, etc.)
- Background tasks and watchlist entries

## Integration Points

UUID fields appear throughout the GraphQL API as unique identifiers for resources, enabling reliable reference and retrieval of specific entities and their relationships across the Enigma data platform.

---

**Last Updated:** March 11, 2026
