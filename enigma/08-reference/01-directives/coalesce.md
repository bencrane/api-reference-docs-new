# coalesce Directive

## Overview

The `coalesce` directive selects the first non-null value from a list of referenced fields. This is useful when you want to provide fallback field options in your GraphQL queries.

## Syntax

```graphql
directive @coalesce(
  ref: String
  refs: [String!]
) on FIELD
```

## Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `ref` | `String` | A single field reference to evaluate |
| `refs` | `[String!]` | A list of field references to evaluate in order |

## Usage Example

According to the documentation, you can use this directive like: `_fn @coalesce(refs: ["a.aa", "b.bb"])` to return the value from field `a.aa` if it's non-null; otherwise, it returns the value from `b.bb`.

## Behavior

The directive evaluates references sequentially and returns the first value that is not null. This allows you to specify alternative fields as fallbacks in a single query.
