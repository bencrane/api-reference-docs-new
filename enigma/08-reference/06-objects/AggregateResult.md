# AggregateResult

## Overview

The `AggregateResult` type is a GraphQL object that provides aggregation functionality for querying data within the Enigma GraphQL API.

## Fields

### `count`

**Type:** `Int`

Returns an integer count based on the specified field and optional conditions.

#### Parameters

- **`field`** (`String!`) - A required string parameter that specifies which field to count
- **`conditions`** (`Conditions`) - An optional input object for filtering the count results based on specific conditions

## Usage

The `AggregateResult` type is returned by the [`aggregate`](/reference/graphql_api/queries/aggregate) query, enabling users to perform counting operations on Enigma data with optional filtering capabilities.
