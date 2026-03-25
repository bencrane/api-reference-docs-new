# Duplicate Agent API Documentation

## Endpoint Overview

The Duplicate Agent endpoint allows developers to create a new agent by copying an existing one. It's a POST request to `https://api.elevenlabs.io/v1/convai/agents/{agent_id}/duplicate`.

## Key Parameters

The endpoint requires an `agent_id` path parameter identifying which agent to copy. An optional `name` field in the request body allows customization of the duplicated agent.

## Response Structure

A successful request returns a `CreateAgentResponseModel` containing the newly created `agent_id` as a string. The operation responds with a 200 status on success or 422 for validation errors.

## Available Server URLs

The API supports multiple regional endpoints including the primary US endpoint, EU residency option, and India residency option for compliance purposes.

## SDK Implementation Examples

The documentation provides code samples across eight programming languages: TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift. Each example demonstrates the basic duplication process with minimal configuration required.

## Header Requirements

The `xi-api-key` header is optional but typically needed for authentication when calling the endpoint directly via HTTP.
