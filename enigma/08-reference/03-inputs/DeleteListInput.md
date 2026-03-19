# DeleteListInput

## Overview

Input type used to specify which list should be deleted from the Enigma GraphQL API.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `ID` | Yes | The unique identifier of the list to be removed |

## Usage

The `DeleteListInput` type is utilized by the `deleteList` mutation to remove an existing list by providing its identifier.

## Related Operations

- **Mutation**: [`deleteList`](/reference/graphql_api/mutations/delete-list)

---

*Documentation last updated: Mar 11, 2026*
