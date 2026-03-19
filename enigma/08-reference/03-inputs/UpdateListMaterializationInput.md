# UpdateListMaterializationInput

## Overview

The `UpdateListMaterializationInput` is a GraphQL input type used to modify an existing list materialization within the Enigma API.

## Fields

### id
- **Type:** `ID!` (non-null scalar)
- **Description:** The unique identifier for the list materialization to be updated. This field is required.

### status
- **Type:** `String` (scalar)
- **Description:** The new status value for the list materialization. This field is optional.

## Usage

This input type is utilized by the `updateListMaterialization` mutation to apply changes to a previously created list materialization. Callers must provide the materialization's identifier, and may optionally specify a new status value.

---

**Last Updated:** Mar 11, 2026
