# SearchInput

## Overview

A GraphQL input type used for executing searches within the Enigma API. This input accepts multiple search criteria to find and match business entities.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `prompt` | String | Free-form search text |
| `fields` | [SearchFieldGroupInput] | Structured search field groups |
| `id` | String | Entity identifier |
| `name` | String | Business or entity name |
| `address` | AddressInput | Single address for matching |
| `addresses` | [AddressInput] | Multiple addresses for matching |
| `person` | PersonInput | Individual person details |
| `phoneNumber` | String | Contact phone number |
| `website` | String | Business website URL |
| `tin` | TinInput | Tax identification number |
| `conditions` | Conditions | Filter conditions for results |
| `matchThreshold` | Float | Confidence threshold for matches |
| `entityType` | EntityType | Enum specifying entity classification |
| `engine` | String | Search engine selection |
| `output` | OutputSpec | Output formatting specifications |
| `enrichmentIdsS3Path` | String | "S3 path to parquet file containing internal_id column for filtering" |

## Usage

`SearchInput` is utilized in the following operations:

- `aggregate` query
- `search` query
