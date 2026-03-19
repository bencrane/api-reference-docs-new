# createSuggestion Mutation

## Overview

The `createSuggestion` mutation allows you to submit a suggestion through the Enigma GraphQL API.

## Signature

```graphql
createSuggestion(suggestion: SuggestionInput!): CreateSuggestion
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `suggestion` | `SuggestionInput` | Yes | The suggestion data to be submitted |

## Return Type

Returns a [`CreateSuggestion`](/reference/graphql_api/objects/create-suggestion) object containing the result of the mutation.

## Usage

This mutation accepts a required `SuggestionInput` object and processes it to create a new suggestion record in the system.

---

**Last Updated:** March 11, 2026
