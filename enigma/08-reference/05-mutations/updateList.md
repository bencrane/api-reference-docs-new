# updateList Mutation

## Overview

The `updateList` mutation is a GraphQL operation used to modify an existing list in the Enigma system.

## Signature

```graphql
updateList(input: UpdateListInput!): UpdateList
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `input` | `UpdateListInput` | Yes | The input object containing the list update details |

## Return Type

Returns an `UpdateList` object containing the result of the update operation.

## Usage

This mutation accepts a required input parameter of type `UpdateListInput` and processes the update request, returning an `UpdateList` response object with the operation results.

## Related Operations

- **Previous**: [`updateListMaterialization`](/reference/graphql_api/mutations/update-list-materialization)
- **Next**: [`Account`](/reference/graphql_api/objects/account)

## Additional Resources

For complete input and output object definitions, refer to:
- [`UpdateListInput`](/reference/graphql_api/inputs/update-list-input) - Input parameters
- [`UpdateList`](/reference/graphql_api/objects/update-list) - Response object

---

**Last Updated**: March 11, 2026
