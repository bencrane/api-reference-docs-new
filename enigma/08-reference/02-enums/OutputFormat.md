# OutputFormat Enum

## Overview

`OutputFormat` is an enumeration used within Enigma's GraphQL API to specify the desired file format for data output operations.

## Values

- **PARQUET** — A columnar storage format optimized for analytical queries and data processing workflows
- **CSV** — A comma-separated values format for broad compatibility with spreadsheet applications and data analysis tools

## Usage

This enumeration is utilized as a field within the [`OutputSpec`](/reference/graphql_api/inputs/output-spec) input type, allowing clients to define their preferred output format when requesting data exports or materializations.

## Related References

- Previous: [ListType](/reference/graphql_api/enums/list-type)
- Next: [TinType](/reference/graphql_api/enums/tin-type)

---

*Documentation last updated: March 11, 2026*
