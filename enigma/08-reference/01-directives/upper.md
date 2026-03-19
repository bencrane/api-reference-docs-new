# upper Directive

## Overview

The `@upper` directive transforms string values to uppercase. It can process a single string field or multiple string fields within a GraphQL query.

## Syntax

```graphql
directive @upper(
  ref: String
  refs: [String!]
) on FIELD
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ref` | `String` | Specifies a single field name to convert to uppercase |
| `refs` | `[String!]` | Specifies multiple field names to convert to uppercase |

## Usage

Apply the directive to a field in your GraphQL query to automatically convert the returned string value(s) to uppercase:

```graphql
query {
  business {
    name @upper(ref: "name")
  }
}
```

The directive converts the output to all capital letters. This is useful for standardizing text formatting in API responses or preparing data for downstream processing.
