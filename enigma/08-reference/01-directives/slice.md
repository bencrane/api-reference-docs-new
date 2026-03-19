# slice Directive

## Overview

The `@slice` directive extracts a contiguous subset from an array or string using start and end indices. It supports negative indexing for reverse-position selections.

## Syntax

```graphql
directive @slice(
  start: Int
  end: Int
) on FIELD
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `start` | Int | The beginning index (inclusive) for the slice operation |
| `end` | Int | The ending index (exclusive) for the slice operation |

## Example Usage

The directive returns the first two elements when applied to an array:

```graphql
_fn @array(refs: ["a", "b", "c"]) @slice(start: 0, end: 2)
```

Result: `["a", "b"]`

## Key Features

- Works with both arrays and strings
- Supports negative indices for counting from the end
- End index is exclusive (not included in the result)
