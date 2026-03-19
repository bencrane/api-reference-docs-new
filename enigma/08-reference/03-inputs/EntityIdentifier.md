# EntityIdentifier

## Overview

The `EntityIdentifier` input type serves as a reference structure within the Enigma GraphQL API for identifying entities through a unique identifier and associated entity type classification.

## Structure

```graphql
input EntityIdentifier {
  id: String!
  type: EntityType!
}
```

## Fields

### `id`
- **Type:** `String!` (non-null)
- **Description:** A required unique identifier string for the entity being referenced.

### `type`
- **Type:** `EntityType!` (non-null enum)
- **Description:** A required enumeration value specifying the classification or category of the entity being identified.

## Usage

This input type functions as a component within the broader GraphQL schema and is specifically utilized by the `SuggestionInput` input type for entity reference purposes.

## Related References

- **Used By:** [`SuggestionInput`](/reference/graphql_api/inputs/suggestion-input)
- **See Also:** [`EntityType`](/reference/graphql_api/enums/entity-type) enum

---

*Last Updated: March 11, 2026*
