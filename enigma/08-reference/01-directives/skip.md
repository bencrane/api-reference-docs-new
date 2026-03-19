# skip Directive

## Overview

The `@skip` directive is used in GraphQL queries to conditionally exclude fields or fragments from execution based on a boolean condition.

## Signature

```graphql
directive @skip(if: Boolean!) on FIELD | FRAGMENT_SPREAD | INLINE_FRAGMENT
```

## Parameters

### `if` (required)
- **Type:** `Boolean!` (non-null boolean)
- **Description:** When set to `true`, the directive prevents the associated field or fragment from being processed in the query result.

## Usage Context

This directive can be applied to three locations within GraphQL queries:
- Individual fields
- Fragment spreads
- Inline fragments
