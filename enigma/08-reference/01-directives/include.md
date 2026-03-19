# include Directive

## Overview

The `@include` directive is a GraphQL directive that conditionally includes fields or fragments in query results based on a boolean condition.

## Syntax

```graphql
directive @include(if: Boolean!) on FIELD | FRAGMENT_SPREAD | INLINE_FRAGMENT
```

## Description

This directive instructs the GraphQL executor to "include this field or fragment only when the `if` argument is true." It provides conditional control over which fields are returned in API responses.

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `if` | Boolean | Yes | Controls whether the field or fragment is included; when true, the field is returned |

## Applicable Locations

The `@include` directive can be applied to:
- **FIELD** — Individual fields in a query
- **FRAGMENT_SPREAD** — Named fragment spreads
- **INLINE_FRAGMENT** — Inline fragments

## Use Cases

This directive is commonly used to:
- Dynamically control which fields are fetched based on application logic
- Reduce response payload size by excluding unnecessary data
- Create flexible, reusable queries with conditional field selection
