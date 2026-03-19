# createListMaterialization Mutation

## Overview

The `createListMaterialization` mutation is a GraphQL operation within the Enigma API that enables users to materialize list data.

## Signature

```graphql
createListMaterialization(input: CreateListMaterializationInput!): CreateListMaterialization
```

## Parameters

### Input

- **Name:** `input`
- **Type:** `CreateListMaterializationInput!` (required)
- **Description:** Configuration object containing the necessary parameters for materializing a list

## Return Type

- **Type:** `CreateListMaterialization` object
- **Description:** Response object containing the result of the materialization operation

## Related Operations

This mutation is part of a suite of list management operations:
- [`cancelListMaterialization`](/reference/graphql_api/mutations/cancel-list-materialization) — Cancel an ongoing materialization
- [`createList`](/reference/graphql_api/mutations/create-list) — Create a new list
- [`updateListMaterialization`](/reference/graphql_api/mutations/update-list-materialization) — Modify materialization settings
- [`deleteList`](/reference/graphql_api/mutations/delete-list) — Remove a list

## Documentation Status

Last updated: March 11, 2026
