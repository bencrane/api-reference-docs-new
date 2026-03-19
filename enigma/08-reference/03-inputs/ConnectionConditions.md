# ConnectionConditions

## Overview

The `ConnectionConditions` input type is utilized within GraphQL API queries to specify filtering and sorting parameters for search operations.

## Fields

### filter
- **Type:** `JSON` scalar
- **Description:** Accepts a JSON object to filter results based on specified criteria

### orderBy
- **Type:** `[String]` (list of strings)
- **Description:** Specifies the fields and order in which results should be sorted

## Usage Context

`ConnectionConditions` serves as a parameter within the [`SearchListsInput`](/reference/graphql_api/inputs/search-lists-input) input type, enabling developers to customize list search queries with custom filtering logic and result ordering.

---

**Last Updated:** Mar 11, 2026
