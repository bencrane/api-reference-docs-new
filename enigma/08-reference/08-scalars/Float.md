# Float Scalar Type

## Overview

The `Float` scalar type represents signed double-precision fractional values as defined by the [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point) standard.

## Definition

```graphql
scalar Float
```

## Description

This scalar type is used to represent floating-point numbers in GraphQL queries and responses. It accommodates the full range of values specified by the IEEE 754 double-precision format, making it suitable for representing decimal values, percentages, coordinates, and other fractional measurements.

## Usage

The `Float` scalar is employed across numerous objects and inputs throughout the Enigma GraphQL API, including but not limited to:

- **Data Objects**: Address, Brand, LegalEntity, OperatingLocation, Person, and Website entities
- **Input Types**: EnrichmentInput, ListSearchInputInput, and SearchInput
- **Interface Types**: NodeFunctions interface
- **Specialized Fields**: Coordinates, rankings, revenue metrics, quality scores, and transaction values

## Related Scalars

- [Boolean](/reference/graphql_api/scalars/boolean)
- [DateTime](/reference/graphql_api/scalars/date-time)
- [Date](/reference/graphql_api/scalars/date)
- [ID](/reference/graphql_api/scalars/id)
- [Int](/reference/graphql_api/scalars/int)
- [String](/reference/graphql_api/scalars/string)
