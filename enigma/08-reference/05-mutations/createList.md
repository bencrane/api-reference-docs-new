# createList Mutation

## Overview

The `createList` mutation enables you to create a new list within the Enigma GraphQL API system.

## Signature

```graphql
createList(input: CreateListInput!): CreateList
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `input` | [`CreateListInput!`](/reference/graphql_api/inputs/create-list-input) | Yes | Configuration object containing the list creation parameters |

## Return Type

[`CreateList`](/reference/graphql_api/objects/create-list) object

The mutation returns a `CreateList` object containing the result of the list creation operation.

## Related Mutations

- [`createListMaterialization`](/reference/graphql_api/mutations/create-list-materialization) - Materialize a list
- [`updateList`](/reference/graphql_api/mutations/update-list) - Modify an existing list
- [`deleteList`](/reference/graphql_api/mutations/delete-list) - Remove a list
- [`cancelListMaterialization`](/reference/graphql_api/mutations/cancel-list-materialization) - Cancel a materialization process

---

*Documentation last updated: March 11, 2026*
