# ExternalMutation

> Source URL: https://documentation.enigma.com/reference/graphql_api/objects/external-mutation
> (The dedicated type page returned the generic docs overview on 2026-04-16. The fields below are synthesized from the individual mutation pages under `/reference/graphql_api/mutations/` and from references to `ExternalMutation` surfaced via the docs search.)

## Overview

`ExternalMutation` groups the list-management and suggestion mutations exposed externally by the Enigma GraphQL API. Each field wraps a single mutation operation, takes a dedicated `Input!` object, and returns a corresponding result payload type.

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `createList` | `CreateList` | `input: CreateListInput!` | Create a new list. |
| `updateList` | `UpdateList` | `input: UpdateListInput!` | Update an existing list. |
| `deleteList` | `DeleteList` | `input: DeleteListInput!` | Delete a list. |
| `createListMaterialization` | `CreateListMaterialization` | `input: CreateListMaterializationInput!` | Begin materializing a list. |
| `cancelListMaterialization` | `CancelListMaterialization` | `input: CancelListMaterializationInput!` | Cancel an in-progress list materialization. |
| `createSuggestion` | `CreateSuggestion` | `suggestion: SuggestionInput!` | Submit a data-quality suggestion. |

No field descriptions are provided in the upstream documentation.

## Interfaces Implemented

None documented.

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** `Mutation` (root) — exposed as the `externalMutation` entry point on the `Mutation` root type.

## Source

- https://documentation.enigma.com/reference/graphql_api/objects/external-mutation (returned overview page — no type reference content)
- Field sources:
  - https://documentation.enigma.com/reference/graphql_api/mutations/create-list
  - https://documentation.enigma.com/reference/graphql_api/mutations/update-list
  - https://documentation.enigma.com/reference/graphql_api/mutations/delete-list
  - https://documentation.enigma.com/reference/graphql_api/mutations/create-list-materialization
  - https://documentation.enigma.com/reference/graphql_api/mutations/cancel-list-materialization
  - https://documentation.enigma.com/reference/graphql_api/mutations/create-suggestion
