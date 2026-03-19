# listMaterialization Query

## Overview

The `listMaterialization` query retrieves information about a materialized list from the Enigma GraphQL API.

## Signature

```graphql
listMaterialization(input: GetListMaterializationInput!): ListMaterialization
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `input` | `GetListMaterializationInput!` | Yes | Configuration object specifying which list materialization to retrieve |

## Return Type

Returns a `ListMaterialization` object containing details about the requested list materialization.

## Related Resources

- **Previous Query:** [enrich](/reference/graphql_api/queries/enrich)
- **Next Query:** [lists](/reference/graphql_api/queries/lists)
- **Related Input Type:** [GetListMaterializationInput](/reference/graphql_api/inputs/get-list-materialization-input)
- **Related Object Type:** [ListMaterialization](/reference/graphql_api/objects/list-materialization)

## Additional Information

- **Last Updated:** March 11, 2026
- **API Reference:** GraphQL API Reference
