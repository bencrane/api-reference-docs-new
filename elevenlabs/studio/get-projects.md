# List Studio Projects

## Endpoint Overview

The **GET /v1/studio/projects** endpoint retrieves a collection of your Studio projects with associated metadata. This is accessible via multiple regional servers including the standard US endpoint and EU residency options.

## Key Parameters

The endpoint accepts an optional `xi-api-key` header parameter for authentication. No required query parameters are specified in the OpenAPI definition.

## Response Structure

The successful 200 response returns a `GetProjectsResponse` object containing:

- **projects**: An array of `ProjectResponse` objects, each including:
  - Basic metadata (project_id, name, creation dates)
  - Voice configuration (default title and paragraph voice IDs)
  - Content details (title, author, description, genres)
  - Processing state and access level information
  - Caption and chapter enablement settings
  - Agent-related configuration options

## Required Response Fields

Essential project properties include project identifier, name, creation timestamp, voice IDs, model ID, download capability, volume normalization status, project state, access permissions, and quality check settings.

## Error Handling

A 422 response indicates validation errors, returning an `HTTPValidationError` object with detailed error information including location, message, and error type.

## Implementation Examples

The documentation provides SDK implementations for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, with the simplest being: `client.studio.projects.list()` in both TypeScript and Python.
