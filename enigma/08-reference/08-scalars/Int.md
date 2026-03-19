# Int Scalar Type

## Overview

The `Int` scalar represents non-fractional signed whole numeric values in the Enigma GraphQL API.

## Specification

**Name:** `Int`

**Description:** Non-fractional signed whole numeric values

**Range:** -(2^31) to 2^31 - 1

This scalar adheres to standard GraphQL conventions for 32-bit signed integer representation.

## Usage

The `Int` type appears across numerous GraphQL objects and inputs throughout the Enigma schema, including:

- Core entity objects (Account, Address, LegalEntity, Brand, Person, etc.)
- Edge objects representing relationships between entities
- Input types for filtering and querying (ListConditionsInput, SearchListsInput, Conditions)
- Directives like `slice` for pagination
- Metadata and result objects (AttributeMetadata, AggregateResult, ColumnCount)

## Common Applications

- Pagination parameters (offsets, limits)
- Count fields (row counts, transaction quantities)
- Ranking and scoring metrics
- Numeric identifiers and indexes
- Quantity measurements in business data

## Related Scalar Types

- [`Float`](/reference/graphql_api/scalars/float) — for fractional numeric values
- [`String`](/reference/graphql_api/scalars/string) — for text data
- [`ID`](/reference/graphql_api/scalars/id) — for unique identifiers
