# SuggestionInput

## Overview

An input type used within the Enigma GraphQL API for submitting suggestion data.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `suggestedByUserId` | `ID` | Optional identifier for the user submitting the suggestion |
| `suggestedByEmail` | `String!` | Required email address of the user making the suggestion |
| `payload` | `JSON!` | Required JSON payload containing the suggestion data |
| `suggestedValue` | `JSON` | Optional JSON value representing the suggested data |
| `ancestorIdentifier` | `[EntityIdentifier]` | Optional list of entity identifiers for parent entities |
| `suggestedEntityIdentifier` | `EntityIdentifier` | Optional entity identifier for the suggested entity |
| `field` | `String` | Optional field name associated with the suggestion |

## Usage

This input type is used with the [`createSuggestion`](/reference/graphql_api/mutations/create-suggestion) mutation to submit user-generated suggestions within the Enigma system.
