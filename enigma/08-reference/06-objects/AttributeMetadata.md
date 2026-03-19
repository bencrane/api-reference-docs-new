# AttributeMetadata

## Overview

`AttributeMetadata` is a GraphQL object type used within the Enigma API to provide metadata information about attributes.

## Fields

### rank
- **Type:** `Int` (scalar)
- **Description:** Numeric ranking value for the attribute

### matched
- **Type:** `String` (scalar)
- **Description:** String indicating match status or matched value information

## Relationships

This type serves as a field within the [`Searchmetadata`](/reference/graphql_api/objects/searchmetadata) object, providing supplementary data context during search operations.

## Usage Context

`AttributeMetadata` is employed within Enigma's GraphQL API to convey ranking and matching details about data attributes, typically appearing as part of broader metadata responses in search scenarios.

---

**Last Updated:** March 11, 2026
