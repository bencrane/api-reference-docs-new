# deleteList Mutation

## Overview
The `deleteList` mutation enables the removal of a list from the Enigma GraphQL API.

## Signature
```graphql
deleteList(input: DeleteListInput!): DeleteList
```

## Parameters

### Input
- **input** (`DeleteListInput!`) - Required. The input object containing the parameters needed to delete a list.

## Return Type
- **DeleteList** - The response object returned after executing the deletion operation.

## Usage
This mutation accepts a required `DeleteListInput` parameter and returns a `DeleteList` object containing the result of the deletion operation.

## Related Mutations
- [`createList`](/reference/graphql_api/mutations/create-list) - Create a new list
- [`updateList`](/reference/graphql_api/mutations/update-list) - Modify an existing list
- [`createListMaterialization`](/reference/graphql_api/mutations/create-list-materialization) - Materialize a list

---

**Last Updated:** March 11, 2026
