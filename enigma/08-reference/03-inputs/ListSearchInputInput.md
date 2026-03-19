# ListSearchInputInput

## Overview

An input type used for searching within lists in the Enigma GraphQL API.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `entityType` | [`EntityType`](/reference/graphql_api/enums/entity-type) enum | Specifies the category of entity to search for |
| `conditions` | [`ListConditionsInput`](/reference/graphql_api/inputs/list-conditions-input) input | Filtering criteria to apply to the search |
| `prompt` | [`String`](/reference/graphql_api/scalars/string) scalar | Search query text |
| `matchThreshold` | [`Float`](/reference/graphql_api/scalars/float) scalar | Confidence level requirement for matching results |

## Usage

This input type is utilized by:

- [`CreateListInput`](/reference/graphql_api/inputs/create-list-input)
- [`UpdateListInput`](/reference/graphql_api/inputs/update-list-input)

---

**Last Updated:** March 11, 2026
