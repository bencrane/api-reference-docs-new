# Conditions Input Type

## Overview

The `Conditions` input type is used within GraphQL queries to specify filtering, sorting, pagination, and result limitation parameters.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `filter` | `JSON` scalar | Specifies filter criteria for narrowing query results |
| `orderBy` | `[String]` list scalar | Defines the fields and direction for sorting results |
| `limit` | `Int` scalar | Sets the maximum number of results to return |
| `pageToken` | `String` scalar | Token used for pagination to retrieve subsequent result pages |

## Usage Context

The `Conditions` input is a member of the [`SearchInput`](/reference/graphql_api/inputs/search-input) input type, making it available for use in search operations within the Enigma GraphQL API.

## Related Inputs

- **Previous**: [ColumnMappingInput](/reference/graphql_api/inputs/column-mapping-input)
- **Next**: [ConnectionConditions](/reference/graphql_api/inputs/connection-conditions)

*Last updated: March 11, 2026*
