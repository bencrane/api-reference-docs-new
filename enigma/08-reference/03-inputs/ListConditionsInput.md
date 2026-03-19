# ListConditionsInput

## Overview

A GraphQL input type used to specify filtering, ordering, and limiting parameters for list operations.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `filter` | `JSON` | Filtering criteria applied to list results |
| `orderBy` | `[String]` | List of field names used to sort results |
| `limit` | `Int` | Maximum number of results to return |

## Usage

This input type is utilized by the `ListSearchInputInput` input to configure constraints and sorting behavior when querying lists within the GraphQL API.

## Related Types

- **Used by:** `ListSearchInputInput`
