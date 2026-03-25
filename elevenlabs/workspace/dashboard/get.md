# Get Dashboard Settings

**GET** `https://api.elevenlabs.io/v1/convai/settings/dashboard`

Retrieves Convai dashboard settings for the workspace.

## Overview

This endpoint provides access to dashboard configuration settings within the Eleven Labs Conversational AI platform. It requires no path parameters and accepts an optional API key header.

## Parameters

- **xi-api-key** (header, optional): Authentication token for the request

## Response Schema

The successful response (HTTP 200) returns an object containing a `charts` array. Each chart item can be one of three types:

1. **call_success** - Contains `type` and `name`
2. **criteria** - Contains `type`, `name`, and `criteria_id`
3. **data_collection** - Contains `type`, `name`, and `data_collection_id`

## Available Servers

- `https://api.elevenlabs.io`
- `https://api.us.elevenlabs.io`
- `https://api.eu.residency.elevenlabs.io`
- `https://api.in.residency.elevenlabs.io`

## SDK Examples

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to call this endpoint using official client libraries or native HTTP tools.
