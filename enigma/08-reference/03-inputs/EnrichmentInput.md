# EnrichmentInput

## Overview

The `EnrichmentInput` type represents configuration parameters for enriching entity data through the Enigma GraphQL API.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `s3Path` | String | Yes | S3 path reference for the enrichment data source |
| `entityType` | EntityType | No | Specifies the category of entity being enriched (e.g., business or individual) |
| `output` | OutputSpec | Yes | Configuration defining the output structure and format for enriched results |
| `sourceId` | String | Yes | Unique identifier for the data source being used in enrichment |
| `provider` | EnrichmentProvider | No | Designation of the enrichment data provider |
| `scoreThreshold` | Float | No | Minimum confidence score for including enriched data in results |

## Usage Context

The `EnrichmentInput` type is utilized as a parameter in the `enrich` query operation, enabling bulk data enrichment against Enigma's comprehensive database.

## Related References

- [OutputSpec](/reference/graphql_api/inputs/output-spec)
- [EntityType enum](/reference/graphql_api/enums/entity-type)
- [EnrichmentProvider enum](/reference/graphql_api/enums/enrichment-provider)
