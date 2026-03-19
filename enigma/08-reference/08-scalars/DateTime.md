# DateTime Scalar Type

## Overview

The `DateTime` scalar represents temporal values formatted according to the ISO 8601 standard for date and time representation.

## Definition

```graphql
scalar DateTime
```

## Format

This scalar accepts and returns datetime values compliant with the "ISO 8601" specification, which defines a standardized approach to representing dates and times in a machine-readable format.

## Usage

The `DateTime` scalar is widely used across the Enigma GraphQL API as a field type in numerous objects and interfaces, including:

- Entity records (Address, Person, LegalEntity, Brand, etc.)
- Temporal tracking fields (creation dates, modification dates, activity timestamps)
- Transaction data (BrandCardTransaction, OperatingLocationCardTransaction)
- Background processing (BackgroundTask timestamps)
- List operations (List, ListMaterialization)
- Watchlist entries and suggestions

## Related Scalars

- **Date** — For date-only values without time components
- **String** — For unstructured text representations

---

**Last Updated:** March 11, 2026
