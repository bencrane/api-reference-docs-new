# JSONString Scalar Type

## Overview

The `JSONString` scalar type represents JSON data encoded as a string within the Enigma GraphQL API.

## Definition

```graphql
scalar JSONString
```

## Description

This scalar type handles JSON data that is serialized as a string value. Unlike the `JSON` scalar which accepts structured JSON objects directly, `JSONString` requires the JSON data to be encoded as a string representation.

## Usage

The `JSONString` scalar is used throughout the Enigma GraphQL API for fields that need to store or transmit JSON data in string-encoded format, providing flexibility for complex data structures while maintaining string-based serialization.

## Related Scalars

- **JSON** — For structured JSON objects without string encoding
- **String** — For general text data

---

*Last updated: Mar 11, 2026*
