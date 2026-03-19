# UpdateListInput

## Overview

Input type used to modify an existing list in the Enigma GraphQL API.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `ID` | Yes | The unique identifier for the list being updated |
| `name` | `String` | No | The display name of the list |
| `description` | `String` | No | A text summary describing the list's purpose or contents |
| `searchInput` | `ListSearchInputInput` | No | Parameters that define the list's search and filtering criteria |
| `aliases` | `[FieldAliasInput]` | No | Array of field aliases for data mapping purposes |
| `columnOrdering` | `[String]` | No | List of column names specifying their display order |
| `columnMapping` | `[ColumnMappingInput]` | No | Array defining how source fields map to output columns |
| `columnMappings` | `[[ColumnMappingInput]]` | No | Nested array structure for multi-level column mapping configurations |

## Usage

This input type is utilized by the [`updateList`](/reference/graphql_api/mutations/update-list) mutation to modify list properties and configurations.
