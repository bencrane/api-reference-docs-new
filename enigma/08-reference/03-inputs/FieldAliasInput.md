# FieldAliasInput

## Overview

A GraphQL input type used to define field aliases within the Enigma API system.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fullyQualifiedName` | String | Yes | The complete, qualified name of the field being aliased |
| `aliasName` | String | Yes | The alias name to assign to the specified field |

## Usage

The `FieldAliasInput` type is utilized by the following input types to configure field mappings:

- **CreateListInput** – Used when creating new lists with custom field aliases
- **UpdateListInput** – Used when modifying existing lists and their field configurations

## Purpose

This input enables users to map existing data fields to custom alias names, facilitating flexible field naming conventions within list operations and data transformations.
