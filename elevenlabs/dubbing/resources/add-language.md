# Add Language to Resource

## Endpoint Overview

This API endpoint allows you to add a language to an existing dubbing resource. According to the documentation, it "Adds the given ElevenLab Turbo V2/V2.5 language code to the resource."

**Method:** POST
**URL:** `https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/language`

## Key Details

The endpoint accepts a dubbing project ID as a path parameter and requires a language code in the request body. It's important to note that this operation "Does not automatically generate transcripts/translations/audio."

## Request Structure

The request body contains a single property:
- **language** (string): The target language for dubbing

## Response

On successful completion, the API returns a 201 status with a response containing:
- **version** (integer): The version number of the updated resource

## Available Implementations

The documentation provides code examples across multiple programming languages including TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to integrate this endpoint into various applications.
