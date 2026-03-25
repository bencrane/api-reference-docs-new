# Update Studio Project Content

This API endpoint allows you to update the content of an ElevenLabs Studio project using a POST request to `https://api.elevenlabs.io/v1/studio/projects/{project_id}/content`.

## Key Parameters

The endpoint accepts multipart/form-data with these optional fields:

- **from_url**: Extract content from a URL to initialize the project
- **from_document**: Upload a file (.epub, .pdf, .txt, etc.) to populate the project
- **from_content_json**: Provide structured content as JSON with chapters, blocks, and TTS nodes
- **auto_convert**: Boolean flag to automatically convert the project to audio

## Important Constraint

"If this is set, 'from_url' and 'from_content' must be null" - only one initialization method should be used at a time. If none are provided, the project initializes as blank.

## Response

The endpoint returns a successful 200 response containing an `EditProjectResponseModel` with complete project details including ID, name, voice settings, state, and caption configurations.

## Available SDKs

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to call this endpoint with your preferred language.
