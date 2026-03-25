# Convert Studio Project

**Endpoint:** POST https://api.elevenlabs.io/v1/studio/projects/{project_id}/convert

## Description

This endpoint initiates conversion of a Studio project along with all associated chapters.

## Parameters

- **project_id** (path, required): The project identifier needed for the conversion operation. Use the List projects endpoint to retrieve available projects.
- **xi-api-key** (header, optional): Authentication key for API access

## Response

**Success (200):**
Returns a JSON object with a `status` field. A successful conversion yields status value 'ok'.

**Validation Error (422):**
Returns validation error details in JSON format.

## SDK Examples

The API supports multiple languages:

- **TypeScript/JavaScript:** Uses `client.studio.projects.convert("21m00Tcm4TlvDq8ikWAM")`
- **Python:** Uses `client.studio.projects.convert(project_id="21m00Tcm4TlvDq8ikWAM")`
- **Go, Ruby, Java, PHP, C#, Swift:** HTTP POST request implementations available

## Additional Reference

Full API documentation available at: https://elevenlabs.io/docs/api-reference/studio/convert-project
