# join Directive

## Overview

The `@join` directive concatenates array elements into a single string using a specified separator. This is useful for combining multiple values into a formatted output.

## Syntax

```graphql
directive @join(
  ref: String
  refs: [String!]
  sep: String
) on FIELD
```

## Description

This directive merges array elements into one string. As noted in the documentation, "Joins array elements into a single string using the 'sep' separator (defaults to empty string)." Null values are converted to empty strings, and non-string values are automatically converted to strings.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ref` | `String` | Single reference field to join |
| `refs` | `[String!]` | Multiple reference fields to join |
| `sep` | `String` | Separator between joined elements (defaults to empty string) |

## Example

```graphql
query {
  business {
    locations @join(refs: ["city", "state"], sep: ", ")
  }
}
```

In this example, if `city` is "New York" and `state` is "NY", the result would be "New York, NY".

## Behavior Notes

- **Null handling**: Null values become empty strings
- **Type conversion**: Non-string values (integers, etc.) are automatically stringified
- **Default separator**: When `sep` is omitted, elements join with no space between them
