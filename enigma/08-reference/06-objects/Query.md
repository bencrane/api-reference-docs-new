# Query

> Source URL: https://documentation.enigma.com/reference/graphql_api/objects/query
> (The dedicated `Query` object type page returns the docs landing page rather than a type reference as of 2026-04-16. The fields below are synthesized from the individual query pages under `/reference/graphql_api/queries/`.)

## Overview

`Query` is the root operation type of the Enigma GraphQL API. It exposes the entry-point fields used to search, aggregate, and retrieve business data (accounts, background tasks, and list materializations).

## Fields

| Field Name | Type | Arguments | Description |
|---|---|---|---|
| `search` | `[SearchUnion]` | `searchInput: SearchInput!` | Search business entities; returns a list of `SearchUnion` results. |
| `aggregate` | `AggregateResult` | `searchInput: SearchInput!` | Run an aggregation over search results. |
| `backgroundTask` | `BackgroundTask` | `id: String!` | Retrieve a background task by its string identifier. |
| `account` | `Account` | (none) | Return the caller's `Account` object. |
| `listMaterialization` | `ListMaterialization` | `input: GetListMaterializationInput!` | Retrieve information about a materialized list. |

No descriptions are provided for these fields in the upstream documentation ("No description" is the literal upstream value for each).

## Interfaces Implemented

None.

## Type Membership

- **Member of Edge(s):** None
- **Member of Connection(s):** None
- **Member of Union(s):** None
- **Referenced by Input(s):** None
- **Referenced by Object(s):** Root operation type — referenced implicitly by every GraphQL query sent to `https://api.enigma.com/graphql`.

## Source

- https://documentation.enigma.com/reference/graphql_api/objects/query (landing page — no type reference content)
- Field sources:
  - https://documentation.enigma.com/reference/graphql_api/queries/search
  - https://documentation.enigma.com/reference/graphql_api/queries/aggregate
  - https://documentation.enigma.com/reference/graphql_api/queries/background-task
  - https://documentation.enigma.com/reference/graphql_api/queries/account
  - https://documentation.enigma.com/reference/graphql_api/queries/list-materialization
