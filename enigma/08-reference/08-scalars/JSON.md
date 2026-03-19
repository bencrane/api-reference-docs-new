# JSON Scalar

## Overview

The `JSON` scalar type is a GraphQL scalar used within Enigma's API for handling arbitrary JSON data structures.

## Definition

```graphql
scalar JSON
```

## Usage

### Returned By

The `JSON` scalar is returned by:
- [`attributeGroups`](/reference/graphql_api/queries/attribute-groups) query

### Member Of

This scalar type appears as a field member across numerous objects and inputs within the Enigma GraphQL API, including:

**Common Objects:**
- Address-related types (`Address`, `AddressDeliverability`)
- Brand data (`Brand`, `BrandActivity`, `BrandName`)
- Entity information (`LegalEntity`, `LegalEntityName`, `LegalEntityType`)
- Location details (`OperatingLocation`, `OperatingLocationName`)
- Contact data (`EmailAddress`, `PhoneNumber`)
- Business registration (`RegisteredEntity`, `Registration`)
- Personnel (`Person`, `PersonName`)
- Additional entities (`Role`, `Website`, `WatchlistEntry`)

**Inputs:**
- `Conditions`
- `ConnectionConditions`
- `ListConditionsInput`
- `SuggestionInput`

## Purpose

The `JSON` scalar enables flexible representation of complex, nested data structures that don't fit neatly into standard GraphQL types, allowing the API to return variable-shaped objects while maintaining type safety.

---

*Last updated: Mar 11, 2026*
