# trim Directive

## Overview

The `trim` directive removes leading and trailing whitespace from string values or string arrays in GraphQL queries.

## Syntax

```graphql
directive @trim(
  ref: String
  refs: [String!]
) on FIELD
```

## Description

This directive processes string data by stripping whitespace from the beginning and end of values. It accepts either a single reference or multiple references, making it useful for cleaning data before returning results.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ref` | `String` | A single field reference to trim |
| `refs` | `[String!]` list | Multiple field references to trim |

## Usage Example

```graphql
query {
  business {
    name @trim(ref: "name")
  }
}
```

In this example, the directive removes leading and trailing whitespace from the business name field before returning it in the response.
