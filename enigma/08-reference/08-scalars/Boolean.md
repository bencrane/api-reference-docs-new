# Boolean Scalar Type

## Overview

The `Boolean` scalar represents a logical value of either `true` or `false` within the Enigma GraphQL API.

## Definition

```graphql
scalar Boolean
```

## Description

This fundamental scalar type is used throughout the GraphQL schema to indicate binary or flag-type fields where a true/false evaluation is needed.

## Usage

The `Boolean` type appears as a member across numerous objects and directives in the Enigma API, including:

- **Objects**: Account, Address, Brand, EmailAddress, Person, Website, and many others
- **Directives**: `@include` and `@skip` for conditional field inclusion/exclusion in queries
- **Interfaces**: NodeFunctions

## Common Applications

Boolean fields are typically used for:
- Status indicators (e.g., is marketable, is active)
- Quality assurance flags (e.g., revenue quality validations)
- Conditional logic in API responses
- Query directives to control field resolution

---

**Last Updated**: March 11, 2026
