# CreateListInput

## Overview

A GraphQL input type used for creating lists within the Enigma API system.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | `String` | The name identifier for the list being created |
| `listType` | `ListType` | Enum specifying the classification of the list |
| `description` | `String` | Optional textual summary of the list's purpose |
| `searchInput` | `ListSearchInputInput` | Search parameters and query criteria for list generation |
| `fileFormat` | `String` | Specification of the input file's data format |
| `aliases` | `[FieldAliasInput]` | Array of field name mappings for alternate identifiers |
| `columnOrdering` | `[String]` | Sequence defining how columns should be arranged |
| `columnMapping` | `[ColumnMappingInput]` | Single set of column-to-field associations |
| `columnMappings` | `[[ColumnMappingInput]]` | Multiple sets of column mapping configurations |
| `inputFileUri` | `String` | Resource location reference for the source data file |

## Usage Context

This input is utilized by the `createList` mutation to define and initialize new lists within the Enigma GraphQL API.
