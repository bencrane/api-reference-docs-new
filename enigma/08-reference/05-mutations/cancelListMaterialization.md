# cancelListMaterialization

## Overview

The `cancelListMaterialization` mutation is a GraphQL operation available in the Enigma API that allows you to cancel an ongoing list materialization process.

## Signature

```graphql
cancelListMaterialization(input: CancelListMaterializationInput!): CancelListMaterialization
```

## Parameters

### Input

- **input** (`CancelListMaterializationInput!`, required): An input object containing the parameters needed to identify and cancel a specific list materialization operation.

## Return Type

- **CancelListMaterialization** (object): The response object containing the result of the cancellation request.

## Details

This mutation enables you to stop an active list materialization that is currently in progress. The operation requires a properly formatted input object specifying which materialization to cancel.

## Related Mutations

- [`createListMaterialization`](/reference/graphql_api/mutations/create-list-materialization) - Initiates a new list materialization
- [`updateListMaterialization`](/reference/graphql_api/mutations/update-list-materialization) - Modifies an existing list materialization

---

**Last Updated**: March 11, 2026
