# compact Directive

## Overview

The `@compact` directive eliminates null values from arrays in GraphQL queries. When applied to an array field, it filters out any null entries, returning only non-null values.

## Syntax

```graphql
directive @compact(
  ref: String
  refs: [String!]
) on FIELD
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ref` | `String` | Single reference string for the compact operation |
| `refs` | `[String!]` | Array of reference strings for the compact operation |

## Usage Example

When you apply this directive to an array containing mixed null and non-null values, it returns only the populated entries:

```graphql
query {
  fieldName @compact(refs: ["a", "b", "c"])
}
```

The directive processes the specified references and strips away any null values from the result set.
