# ListType Enum

## Overview

`ListType` is an enumeration used within the Enigma GraphQL API to specify the categorization of list operations.

## Definition

```graphql
enum ListType {
  LIST_GENERATION
  ENRICHMENT
}
```

## Values

| Value | Description |
|-------|-------------|
| `LIST_GENERATION` | Indicates a list created through generation processes |
| `ENRICHMENT` | Indicates a list created through enrichment operations |

## Usage

The `ListType` enum is utilized by the following GraphQL components:

- **Inputs**: [`CreateListInput`](/reference/graphql_api/inputs/create-list-input)
- **Objects**:
  - [`List`](/reference/graphql_api/objects/list)
  - [`ListMaterialization`](/reference/graphql_api/objects/list-materialization)

## Related Enumerations

- [EnrichmentProvider](/reference/graphql_api/enums/enrichment-provider)
- [EntityType](/reference/graphql_api/enums/entity-type)
- [ListSearchField](/reference/graphql_api/enums/list-search-field)
- [OutputFormat](/reference/graphql_api/enums/output-format)
- [TinType](/reference/graphql_api/enums/tin-type)

---

**Last Updated**: March 11, 2026
