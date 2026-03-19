# lower Directive

## Overview

The `lower` directive transforms string values to lowercase format within GraphQL queries.

## Description

"Converts a string or each string in an array to lowercase." For example, using `@lower(ref: "name")` will return the lowercased version of the name field value.

## Syntax

```graphql
directive @lower(
  ref: String
  refs: [String!]
) on FIELD
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ref` | `String` | Single field reference to convert to lowercase |
| `refs` | `[String!]` | Array of field references to convert to lowercase |

## Usage

Apply this directive to any field that returns string data to automatically convert the output to lowercase characters. It can process either a single field reference or multiple field references simultaneously.
