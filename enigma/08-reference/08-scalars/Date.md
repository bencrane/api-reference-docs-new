# Date Scalar Type

## Overview

The `Date` scalar represents a date value following the ISO 8601 standard for date formatting.

## Definition

```graphql
scalar Date
```

## Format

This scalar adheres to the "ISO 8601" specification for representing dates in a standardized, internationally-recognized format.

## Usage

The `Date` scalar is employed across multiple GraphQL object types within the Enigma API, including:

- Brand
- BrandCardTransaction
- LegalEntityBankruptcy
- OperatingLocationCardTransaction
- OperatingLocationRank
- RegisteredEntity
- Registration
- ReviewSummary

## Related Scalars

- **DateTime** - For timestamp values including both date and time components
- **String** - For general text data
- **Int** - For numeric integer values

---

**Last Updated:** March 11, 2026
