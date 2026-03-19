# BackgroundTask

## Overview

The `BackgroundTask` type represents an asynchronous task being executed within the Enigma system, tracking its lifecycle from creation through completion.

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | `UUID!` | Unique identifier for the background task |
| `apiKeyId` | `String!` | Associated API key identifier |
| `backgroundTaskType` | `String!` | Category or classification of the task |
| `status` | `String!` | Current execution status |
| `args` | `JSON` | Input arguments provided to the task |
| `result` | `JSON` | Task output or results upon completion |
| `progressPercentComplete` | `Float` | Completion percentage (0-100) |
| `progressMessage` | `String` | Human-readable progress update |
| `lastError` | `String` | Most recent error message, if any |
| `executionAttempts` | `Int!` | Number of execution attempts made |
| `etag` | `String!` | Entity tag for optimistic concurrency control |
| `createdTimestamp` | `DateTime!` | Task creation timestamp |
| `updatedTimestamp` | `DateTime!` | Most recent modification timestamp |
| `lastExecutionTimestamp` | `DateTime` | Timestamp of most recent execution attempt |
| `nextExecutionTimestamp` | `DateTime!` | Scheduled time for next execution attempt |

## Usage

This type is returned by the [`backgroundTask`](/reference/graphql_api/queries/background-task) query, allowing you to monitor long-running operations and retrieve their results or error states.
