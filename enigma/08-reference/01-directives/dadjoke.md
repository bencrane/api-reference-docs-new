# dadjoke Directive

## Overview

The `@dadjoke` directive is a utility function in Enigma's GraphQL API that returns a random dad joke while disregarding any input values.

## Syntax

```graphql
directive @dadjoke on FIELD
```

## Description

This directive generates a random dad joke and can be applied to any field. As noted in the documentation, it "ignores all input values" and is primarily useful for two purposes:

1. **Testing other directives** - Validate directive behavior without relying on actual data
2. **General amusement** - A lighthearted addition for developers between tasks

## Usage Context

The `@dadjoke` directive operates at the field level in GraphQL queries, making it a simple way to inject humor into API interactions while maintaining compatibility with other directive testing scenarios.
