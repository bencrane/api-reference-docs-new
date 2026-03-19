# map Directive

## Overview

The `@map` directive extracts nested fields from array elements in GraphQL queries. It processes each item in an array and retrieves a specified nested value using dot-notation path syntax.

## Syntax

```graphql
directive @map(
  ref: String
  refs: [String!]
  field: String
) on FIELD
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ref` | String | Single reference path to an array field |
| `refs` | [String!] | Multiple reference paths to array fields |
| `field` | String | Dot-separated path to extract from each array element |

## Behavior

- **Field Extraction**: Uses dot notation (e.g., `"a.b.c"`) to access nested properties within array elements
- **Missing Paths**: Returns `null` for array items where the specified path does not exist
- **Default Behavior**: When `field` is omitted, the entire array element is returned unchanged

## Example Usage

```graphql
query {
  items @map(refs: ["items"], field: "a.b.c") {
    # Extracts the nested 'a.b.c' value from each item
  }
}
```
