# OutputSpec

## Overview

The `OutputSpec` input type defines configuration for output formatting and storage when performing queries or enrichment operations through the Enigma GraphQL API.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `filename` | `String` | The name to assign to the output file |
| `format` | `OutputFormat` | The desired output format for the results |
| `s3Path` | `String` | The S3 path where output should be stored |

## Usage

This input type is utilized by the following operations:

- **EnrichmentInput** — For specifying output configuration during data enrichment requests
- **SearchInput** — For configuring output parameters in search queries

## Related Resources

- [OutputFormat Enum](/reference/graphql_api/enums/output-format)
- [EnrichmentInput](/reference/graphql_api/inputs/enrichment-input)
- [SearchInput](/reference/graphql_api/inputs/search-input)
