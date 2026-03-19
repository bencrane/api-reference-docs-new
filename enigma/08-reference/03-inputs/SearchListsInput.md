# SearchListsInput

## Overview

This GraphQL input type is used for searching and filtering lists within the Enigma API.

## Fields

| Field | Type | Purpose |
|-------|------|---------|
| `id` | ID | Identifier for targeting a specific list |
| `name` | String | Name-based filtering for lists |
| `conditions` | ConnectionConditions | Advanced filtering criteria |
| `first` | Int | Pagination parameter for limiting initial results |
| `after` | String | Cursor-based pagination for forward navigation |
| `last` | Int | Pagination parameter for limiting trailing results |
| `before` | String | Cursor-based pagination for backward navigation |

## Usage Context

SearchListsInput serves as a parameter for:
- The `lists` query operation
- The deprecated `searchLists` query operation

## Pagination

This input supports cursor-based pagination through the `after`/`before` string parameters and limit-based pagination via `first`/`last` integer parameters, enabling flexible result set navigation.
